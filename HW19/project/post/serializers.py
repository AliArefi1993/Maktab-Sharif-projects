from django.contrib.auth import get_user_model
from rest_framework import serializers
from post.models import Post, Tag, Category, Comment

User = get_user_model()


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ['id', 'owner', 'title', 'description']


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'


class PostDetailSerializer(serializers.ModelSerializer):
    tag = TagSerializer(many=True)
    category = CategorySerializer(many=True)
    owner = UserSerializer()
    comments = CommentSerializer(source='comments_post', many=True)

    class Meta:
        model = Post
        fields = '__all__'


class PostCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = '__all__'


# class CategoryDetailSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Category
#         fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class CommentDetailSerializer(serializers.ModelSerializer):
    post = PostSerializer()
    user = UserSerializer()

    class Meta:
        model = Comment
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    post = PostSerializer()
    user = UserSerializer()

    class Meta:
        model = Comment
        fields = '__all__'


class PostUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ['title', 'tag', 'owner', 'published', 'description']


class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'tag', 'owner', 'published', 'description']
