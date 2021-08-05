from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny

from backend.api.board.models import Post
from backend.api.board.serializers import PostSerializer


class PostsForHome(ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = PostSerializer

    def get_queryset(self):
        return self.get_four_post_by_order()

    def get_four_post_by_order(self):
        queryset = Post.objects.order_by('-%s' % self.kwargs.get('order'))
        queryset = queryset[:4]
        return queryset
