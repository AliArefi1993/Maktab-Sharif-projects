from django.shortcuts import render
from .models import Post, Comment, Category
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


class PostsListView(ListView):
    model = Post


class PostDetailView(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_list'] = Comment.objects.filter(post=context['post'])
        return context


def category_list(request):
    category_obj = Category.objects.all()
    return render(request, 'post/category_list.html', {'categories': category_obj})


def category_posts_list(request, id):
    posts_obj = Post.objects.filter(category__id=id)
    return render(request, 'post/posts-category_list.html', {'posts': posts_obj})
