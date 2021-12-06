from django.urls import path
from post.views import comment_list, comment_detail, category_list, category_detail, post_list_create, post_detail_update_delete

urlpatterns = [
    path('post/', post_list_create, name='post_list_create'),
    path('post/<int:id>', post_detail_update_delete,
         name='post_detail_update_delete'),
    path('comment/', comment_list, name='comment_list'),
    path('comment/<int:id>', comment_detail, name='comment_detail'),
    path('category/', category_list, name='category_list'),
    path('category/<int:id>', category_detail, name='category_detail'),

]
