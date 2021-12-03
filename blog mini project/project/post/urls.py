from django.urls import path
# from .views import post_list
from post.views import PostsListView, PostDetailView, category_list, category_posts_list, Login, Logout, SignUpView, ProfileView

urlpatterns = [

    # path('login', user_login, name='login'),
    path('login', Login.as_view(), name='login'),
    path('logout', Logout.as_view(), name='logout'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('signup/', SignUpView.as_view(), name='signup'),

    path('post-list', PostsListView.as_view(), name='postlist'),
    path('category-list', category_list),
    path('category-posts-list/<int:id>/',
         category_posts_list, name='category_post'),
    path('post-detail/<slug>/', PostDetailView.as_view(), name='postdetail'),
]
