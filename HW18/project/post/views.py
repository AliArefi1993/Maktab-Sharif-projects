from post.models import Post, Comment, Category
from rest_framework.decorators import api_view
from rest_framework.response import Response
from post.serializers import PostSerializer, PostDetailSerializer, CommentSerializer,\
    CommentDetailSerializer, CategorySerializer, CategoryDetailSerializer, PostUpdateSerializer, PostCreateSerializer
from rest_framework.generics import get_object_or_404


@api_view(['GET', 'POST'])
def post_list_create(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(data=serializer.data, status=200)

    elif request.method == 'POST':
        serializer = PostCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['owner'] = request.user
        post = serializer.save()
        resp_serializer = PostSerializer(post)
        return Response(data=resp_serializer.data, status=201)


@api_view(['GET', 'PUT', 'DELETE'])
def post_detail_update_delete(request, id):

    post = get_object_or_404(Post, id=id)

    if request.method == "GET":
        serializer = PostDetailSerializer(post)
        return Response(data=serializer.data, status=200)

    elif request.method == 'PUT':
        if post.owner != request.user:
            return Response(data={'msg': 'this post owned by another user'}, status=400)

        serializer = PostUpdateSerializer(post, data=request.data)
        serializer.is_valid(raise_exception=True)
        updated_post = serializer.save()
        resp_serializer = PostDetailSerializer(updated_post)
        return Response(resp_serializer.data, status=200)

    elif request.method == 'DELETE':
        print(post.owner)
        print(request.user)
        if post.owner != request.user:
            return Response(data={'msg': 'this post owned by another user'}, status=400)
        post.delete()

        return Response(status=204)


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
