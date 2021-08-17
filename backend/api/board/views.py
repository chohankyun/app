# -*- coding: utf-8 -*-
import logging
from collections import OrderedDict

from bs4 import BeautifulSoup
from django.db.models import F
from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from backend.api.board.models import Category, Post, Reply, Recommend
from backend.api.board.serializers import CategorySerializer, PostSerializer, ReplySerializer, RecommendSerializer

logger = logging.getLogger(__name__)


class Categories(ListAPIView):
    permission_classes = (AllowAny,)
    queryset = Category.objects.order_by('priority')
    serializer_class = CategorySerializer


class HtmlContent:
    @staticmethod
    def add_content(request):
        obj_content = BeautifulSoup(request.data['content'], 'html.parser')
        request.data['text_content'] = obj_content.get_text()
        return request

    @staticmethod
    def add_content_with_image(request):
        obj_content = BeautifulSoup(request.data['content'], 'html.parser')
        request.data['text_content'] = obj_content.get_text()
        image = obj_content.img
        request.data['first_image_source'] = image['src'] if image else ''
        return request


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def create(self, request, *args, **kwargs):
        request.data['user'] = request.user.id
        request = HtmlContent.add_content_with_image(request)
        return super(PostViewSet, self).create(request, *args, **kwargs)

    def increase_click_count(self):
        post = Post.objects.get(pk=self.kwargs.get('pk'))
        post.click_count = F('click_count') + 1
        post.save()

    def retrieve(self, request, *args, **kwargs):
        self.increase_click_count()
        return super(PostViewSet, self).retrieve(request, *args, **kwargs)


class PostListPagination(PageNumberPagination):
    page_size = 16

    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('page', self.page.number),
            ('total', self.page.paginator.count),
            ('page_size', self.page_size),
            ('results', data)
        ]))


class PostsByCategoryNOrder(ListAPIView):
    permission_classes = (AllowAny,)
    pagination_class = PostListPagination
    serializer_class = PostSerializer

    def get_queryset(self):
        return self.get_post_by_category_and_order()

    def get_post_by_category_and_order(self):
        queryset = Post.objects.order_by('-%s' % self.kwargs.get('order'))
        if 'all' != self.kwargs.get('category'):
            queryset = queryset.filter(category=self.kwargs.get('category'))
        return queryset


class ReplyCount:
    @staticmethod
    def save(post_id):
        post = Post.objects.get(pk=post_id)
        post.reply_count = Reply.objects.filter(post=post_id).count()
        post.save()


class ReplyViewSet(ModelViewSet):
    queryset = Reply.objects.all()
    serializer_class = ReplySerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def create(self, request, *args, **kwargs):
        request.data['user'] = request.user.id
        request = HtmlContent.add_content(request)
        return super(ReplyViewSet, self).create(request, *args, **kwargs)

    def get_success_headers(self, data):
        ReplyCount.save(data.get('post'))
        return super(ReplyViewSet, self).get_success_headers(data)


class RepliesInPost(ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = ReplySerializer

    def get_queryset(self):
        return self.get_reply_by_post()

    def get_reply_by_post(self):
        queryset = Reply.objects.filter(post=self.kwargs.get('id'))
        queryset = queryset.order_by('-updated_datetime')
        return queryset


class RecommendCount:
    @staticmethod
    def save(post_id):
        post = Post.objects.get(pk=post_id)
        post.recommend_count = Recommend.objects.filter(post=post_id).count()
        post.save()


class RecommendCountNOwner(RetrieveAPIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        queryset = Recommend.objects.filter(post=self.kwargs.get('post_id'))
        recommend_count = queryset.count()
        is_recommend = queryset.filter(user=request.user.id).exists()
        return Response({'recommend_count': recommend_count, 'is_recommend': is_recommend})


class RecommendViewSet(ModelViewSet):
    queryset = Recommend.objects.all()
    serializer_class = RecommendSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def create(self, request, *args, **kwargs):
        request.data['user'] = request.user.id
        return super(RecommendViewSet, self).create(request, *args, **kwargs)

    def get_success_headers(self, data):
        RecommendCount.save(data.get('post'))
        return super(RecommendViewSet, self).get_success_headers(data)

    def destroy(self, request, *args, **kwargs):
        queryset = Recommend.objects.filter(user=request.user.id)
        queryset = queryset.filter(post=self.kwargs.get('pk'))
        instance = queryset.first()
        self.perform_destroy(instance)
        RecommendCount.save(self.kwargs.get('pk'))
        return Response(status=status.HTTP_204_NO_CONTENT)

