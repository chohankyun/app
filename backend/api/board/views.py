
# -*- coding: utf-8 -*-
import logging

from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny

from backend.api.board.models import Category
from backend.api.board.serializers import CategorySerializer

logger = logging.getLogger(__name__)


class CategoryList(ListAPIView):
    permission_classes = (AllowAny,)
    queryset = Category.objects.order_by('priority')
    serializer_class = CategorySerializer
