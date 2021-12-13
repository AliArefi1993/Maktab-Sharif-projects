
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated

from post.models import Post

from rest_framework.decorators import api_view, authentication_classes
from rest_framework.response import Response
from rest_framework import generics, mixins

from post.serializers import PostSerializer, PostDetailSerializer, PostCreateSerializer, PostUpdateSerializer


class PostList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    """list and create view class for post"""

    queryset = Post.objects.filter(published=True).all()
    permission_classes = (IsAuthenticated,)

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
