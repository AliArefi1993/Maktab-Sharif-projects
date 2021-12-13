from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from post.models import Post, Category, Tag
from post.filter import PostListFilter
from rest_framework.response import Response
from rest_framework import generics
from post.serializers import PostSerializer, PostDetailSerializer, PostCreateSerializer, PostUpdateSerializer, CategorySerializer, TagSerializer


class PostList(generics.ListCreateAPIView):
    """list and create view class for post"""

    queryset = Post.objects.filter(published=True).all()
    permission_classes = (IsAuthenticated,)
    filterset_class = PostListFilter
    paginate_by = 10

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

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

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class CategoryList(generics.ListCreateAPIView):
    """list and create view class for Category"""

    queryset = Category.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = CategorySerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class CategoryDetailUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    """Retrieve Update Delete view class for Category"""

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAdminUser,)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class TagList(generics.ListCreateAPIView):
    """list and create view class for Tag"""

    queryset = Tag.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = CategorySerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class TagDetailUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    """Retrieve Update Delete view class for Tag"""

    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = (IsAdminUser,)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
