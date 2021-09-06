# -*- coding: utf-8 -*-
import logging

from django.db.models import Q, F
from django.utils.translation import ugettext_lazy as _
from rest_framework.exceptions import ParseError
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny

from backend.api.board.models import Post
from backend.api.search.serializers import SearchSerializer

logger = logging.getLogger(__name__)


class Posts(ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = SearchSerializer

    def get_queryset(self):
        search_word = self.get_search_word()

        queryset = Post.objects.filter(
            Q(subject__icontains=search_word) |
            Q(text_content__icontains=search_word) |
            Q(reply__text_content__icontains=search_word))

        queryset = queryset.order_by('-%s' % self.request.query_params.get('order'))
        queryset = queryset.annotate(reply_content=F('reply__content'))
        return queryset

    def get_search_word(self):
        search_word = self.request.query_params.get('search_word')

        if not search_word and len(search_word) < 2:
            raise ParseError(detail=_('Please enter at least 2 characters.'))

        return search_word

