from post.models import Post, Comment, Category
from rest_framework.decorators import api_view
from rest_framework.response import Response
from post.serializers import PostSerializer, PostDetailSerializer, CommentSerializer, CommentDetailSerializer, CategorySerializer, CategoryDetailSerializer
from rest_framework.generics import get_object_or_404


@api_view(['GET'])
def comment_list(request):
    if request.method == 'GET':
        posts = Comment.objects.all()
        serializer = CommentSerializer(posts, many=True)
        return Response(data=serializer.data, status=200)
    return Response(status=406)


@api_view(['GET'])
def comment_detail(request, id):
    comment = get_object_or_404(Comment, id=id)
    serializer = CommentDetailSerializer(comment)
    return Response(data=serializer.data, status=200)


@api_view(['GET'])
def post_list(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(data=serializer.data, status=200)
    return Response(status=406)


@api_view(['GET'])
def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    serializer = PostDetailSerializer(post)
    return Response(data=serializer.data, status=200)


@api_view(['GET'])
def category_list(request):
    if request.method == 'GET':
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return Response(data=serializer.data, status=200)
    return Response(status=406)


@api_view(['GET'])
def category_detail(request, id):
    category = get_object_or_404(Category, id=id)
    serializer = CategoryDetailSerializer(category)
    return Response(data=serializer.data, status=200)
