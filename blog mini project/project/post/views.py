from django.http.response import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment, Category, Tag
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.views import View
from post.forms import LoginForm, SignUpForm, ProfileForm, TagForm, CategoryForm, PostForm, CommentForm
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.db.models.query_utils import Q


class ProfileView(UpdateView):
    model = User
    form_class = ProfileForm
    success_url = reverse_lazy('login')
    template_name = 'post/profile.html'


class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'post/signup.html'


class SuccedLogin(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'post/success_login.html', {'form': self.form})


class Login(View):
    form = LoginForm()

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                messages.add_message(
                    request, messages.SUCCESS, 'Login Succed.')
                next = request.GET.get('next')

                if next:
                    return redirect(request.GET.get('next'))
                return HttpResponseRedirect('/blog/dashboard')

            return HttpResponseRedirect('/blog/login')

    def get(self, request, *args, **kwargs):
        return render(request, 'post/login.html', {'form': self.form})


class Logout(View):

    def get(self, request, *args, **kwargs):
        logout(request)
        messages.add_message(
            request, messages.SUCCESS, 'User Logged out.')
        return redirect('login')


class AuthorCreateView(SuccessMessageMixin, CreateView):
    model = Post
    success_url = '/success/'
    success_message = "%(name)s was logged in successfully"


class DashboardView(LoginRequiredMixin, ListView):
    login_url = 'login'
    model = Post
    template_name = 'post/dashboard.html'

    def get_queryset(self, *args, **kwargs):
        return self.model.objects.filter(owner=self.request.user)


class PostCreateView(LoginRequiredMixin, CreateView):
    'This class view is for creating a Tag'
    login_url = 'login'
    form_class = PostForm
    success_url = reverse_lazy('dashboard')
    template_name = 'post/post_create.html'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.owner = self.request.user
        return super(PostCreateView, self).form_valid(form)


class PostsListView(ListView):
    'This view is for showing all posts to any client'
    model = Post


class PostDetailView(DetailView):
    'This view is for showing any post to any client'
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = CommentForm()
        context['comment_list'] = Comment.objects.filter(post=context['post'])
        context['form'] = form
        if self.request.user != 'AnonymousUser':
            context['user'] = self.request.user
        return context


class CommentView(LoginRequiredMixin, CreateView):
    form_class = CommentForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        self.current_post = Post.objects.get(slug=self.kwargs['slug'])
        obj.post = self.current_post
        return super(CommentView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('postdetail', kwargs={'slug': self.kwargs['slug']})


class PostCommentView(View):
    def get(self, request, *args, **kwargs):
        view = PostDetailView.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = CommentView.as_view()
        return view(request, *args, **kwargs)


class CategoryListView(LoginRequiredMixin, ListView):
    login_url = 'login'
    model = Category


class CategoryPostListView(LoginRequiredMixin, ListView):
    login_url = 'login'
    model = Post

    def get_queryset(self, *args, **kwargs):
        return self.model.objects.filter(category=self.kwargs['id'])


class CategoryEditView(UpdateView):
    'This class view is for editing a Category '
    model = Category
    form_class = TagForm
    success_url = reverse_lazy('category_list')


class CategoryDeleteView(DeleteView):
    'This class delete the selected Category from database'
    model = Category
    success_url = reverse_lazy('category_list')


class CategoryCreateView(CreateView):
    'This class view is for creating a Category'
    form_class = CategoryForm
    success_url = reverse_lazy('category_list')
    template_name = 'post/category_create.html'


class TagListView(LoginRequiredMixin, ListView):
    'This class shows the list of available tag'
    login_url = 'login'
    model = Tag


class TagPostListView(LoginRequiredMixin, ListView):
    login_url = 'login'
    model = Post

    def get_queryset(self, *args, **kwargs):
        return self.model.objects.filter(tag=self.kwargs['id'])


class TagEditView(UpdateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy('tag_list')


class TagDeleteView(DeleteView):
    'This class delete the selected tag from database'
    model = Tag
    success_url = reverse_lazy('tag_list')


class TagCreateView(CreateView):
    'This class view is for creating a Tag'
    form_class = TagForm
    success_url = reverse_lazy('tag_list')
    template_name = 'post/tag_create.html'


class SearchView(ListView):
    model = Post

    def get_queryset(self, *args, **kwargs):
        print(self.args)
        search_query = self.request.GET.get('search_box', None)
        posts = Post.objects.filter(Q(title__icontains=search_query) | Q(
            description__icontains=search_query))
        return posts
