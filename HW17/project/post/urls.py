from django.urls import path
from post.views import post_list, post_detail, comment_list, comment_detail, category_list, category_detail

urlpatterns = [
    path('post/', post_list, name='post_list'),
    path('post/<int:id>', post_detail, name='post_detail'),

    path('comment/', comment_list, name='comment_list'),
    path('comment/<int:id>', comment_detail, name='comment_detail'),

    path('category/', category_list, name='category_list'),
    path('category/<int:id>', category_detail, name='category_detail'),

]
