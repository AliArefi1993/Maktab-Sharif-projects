from django.http.response import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment, Category
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import CreateView
from django.urls import reverse_lazy

from django.views import View
from post.forms import LoginForm, SignUpForm, ProfileForm
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User


# Edit Profile View
class ProfileView(UpdateView):
    model = User
    form_class = ProfileForm
    success_url = reverse_lazy('login')
    template_name = 'post/profile.html'


# Sign Up View
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
                return render(request, 'post/success_login.html', {'username': user.get_username})
                # return HttpResponseRedirect('/blog/succed')
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


# def user_login(request):
#     # if this is a POST request we need to process the form data
#     if request.method == 'POST':
#         # create a form instance and populate it with data from the request:
#         form = LoginForm(request.POST)
#         # check whether it's valid:
#         if form.is_valid():
#             user = authenticate(
#                 request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
#             if user is not None:
#                 login(request, user)
#                 messages.add_message(
#                     request, messages.SUCCESS, 'Hello world.')
#                 messages.add_message(
#                     request, messages.SUCCESS, 'Hello world.', extra_tags='alert-danger')
#                 next = request.GET.get('next')
#                 print()
#                 print()
#                 print(next)
#                 if next:
#                     return redirect(request.GET.get('next'))
#                 return HttpResponseRedirect('/blog/login')
#                 # return redirect(reverse('post:sec'))
#             # else:
#             #     print('not found user')
#             # return HttpResponseRedirect('/thaks/')

#     # if a GET (or any other method) we'll create a blank form
#     else:
#         form = LoginForm()
#     return render(request, 'post/login.html', {'form': form})


class PostsListView(LoginRequiredMixin, ListView):
    login_url = 'login'
    model = Post


class PostDetailView(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_list'] = Comment.objects.filter(post=context['post'])
        return context


def category_list(request):
    category_obj = list(Category.objects.all())
    return render(request, 'post/category_list.html', {'categories': category_obj})


def category_posts_list(request, id):
    posts_obj = list(Post.objects.filter(category__id=id))
    return render(request, 'post/posts-category_list.html', {'posts': posts_obj})
