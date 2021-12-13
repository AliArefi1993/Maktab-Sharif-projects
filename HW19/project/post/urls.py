from django.urls import path
from post.views import PostList, PostDetailUpdateDelete

urlpatterns = [

    path('post/', PostList.as_view(), name='post_list'),
    # path('post/<int:id>/', PostList.as_view(), name='post_list'),
    path('post/<int:pk>/', PostDetailUpdateDelete.as_view(), name='post_detail')
]
