from django.urls import path
from post.views import PostList, PostDetailUpdateDelete, CategoryList, CategoryDetailUpdateDelete, CommentList,\
    CommentDetailUpdateDelete, TagList, TagDetailUpdateDelete

urlpatterns = [

    path('post/', PostList.as_view(), name='post_list'),
    path('post/<int:pk>/', PostDetailUpdateDelete.as_view(), name='post_detail'),

    path('commetn/', CommentList.as_view(), name='comment_list'),
    path('commetn/<int:pk>/', CommentDetailUpdateDelete.as_view(),
         name='comment_detail'),

    path('category/', CategoryList.as_view(), name='category_list'),
    path('category/<int:pk>/', CategoryDetailUpdateDelete.as_view(),
         name='category_detail'),
    path('tag/', TagList.as_view(), name='tag_list'),
    path('tag/<int:pk>/', TagDetailUpdateDelete.as_view(),
         name='tag_detail'),

]
