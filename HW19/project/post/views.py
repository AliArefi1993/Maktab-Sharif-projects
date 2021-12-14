from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from post.models import Post, Category, Tag, Comment
from post.filter import PostListFilter
from rest_framework.response import Response
from rest_framework import generics
from post.serializers import PostSerializer, PostDetailSerializer, PostCreateSerializer, PostUpdateSerializer, CategorySerializer, TagSerializer,\
    CommentSerializer, CommentDetailSerializer


class PostList(generics.ListCreateAPIView):
    """list and create view class for post"""

    queryset = Post.objects.all()
    permission_classes = (IsAuthenticated,)
    filterset_class = PostListFilter

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return PostSerializer
        elif self.request.method == 'POST':
            return PostCreateSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        post = self.perform_create(serializer)
        resp_serializer = PostSerializer(post)
        headers = self.get_success_headers(serializer.data)
        return Response(resp_serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        return serializer.save()

    # def get_serializer_context(self):
    #     """
    #     Extra context provided to the serializer class.
    #     """
    #     return {
    #         'request': self.request,
    #         'format': self.format_kwarg,
    #         'view': self,
    #         'owner': self.request.user
    #     }


class PostDetailUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    """Retrieve Update Delete view class for post"""

    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        if self.request.method == 'GET':
            return Post.objects.all()
        else:
            return Post.objects.filter(owner=self.request.user.id)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return PostDetailSerializer
        else:
            return PostUpdateSerializer


class CategoryList(generics.ListCreateAPIView):
    """list and create view class for Category"""

    queryset = Category.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = CategorySerializer


class CategoryDetailUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    """Retrieve Update Delete view class for Category"""

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAdminUser,)


class TagList(generics.ListCreateAPIView):
    """list and create view class for Tag"""

    queryset = Tag.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = TagSerializer


class TagDetailUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    """Retrieve Update Delete view class for Tag"""

    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = (IsAdminUser,)


class CommentList(generics.ListCreateAPIView):
    """list and create view class for Comment"""

    queryset = Comment.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = CommentSerializer


class CommentDetailUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    """Retrieve Update Delete view class for Comment"""

    queryset = Comment.objects.all()
    serializer_class = CommentDetailSerializer
    permission_classes = (IsAdminUser,)
