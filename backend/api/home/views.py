from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny

from backend.api.board.models import Post
from backend.api.board.serializers import PostSerializer


class Posts(ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = PostSerializer

    def get_queryset(self):
        queryset = Post.objects.order_by('-%s' % self.request.query_params.get('order'))
        queryset = queryset[:4]
        return queryset

