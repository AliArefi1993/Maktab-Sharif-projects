from django.urls import path
# from .views import post_list
from post.views import PostsListView, PostDetailView, category_list, category_posts_list

urlpatterns = [
    path('post-list', PostsListView.as_view(), name='postlist'),
    path('category-list', category_list),
    path('category-posts-list/<int:id>/',
         category_posts_list, name='category_post'),
    path('post-detail/<slug>/', PostDetailView.as_view(), name='postdetail'),
]
