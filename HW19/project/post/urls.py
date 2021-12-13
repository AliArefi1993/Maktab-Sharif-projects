from django.urls import path
from post.views import PostList, PostDetailUpdateDelete, CategoryList, CategoryDetailUpdateDelete

urlpatterns = [

    path('post/', PostList.as_view(), name='post_list'),
    path('post/<int:pk>/', PostDetailUpdateDelete.as_view(), name='post_detail'),

    path('category/', CategoryList.as_view(), name='category_list'),
    path('category/<int:pk>/', CategoryDetailUpdateDelete.as_view(),
         name='category_detail'),


]
