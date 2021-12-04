from django import forms
from .models import Tag, Category, Post
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Profile Form


class ProfileForm(forms.ModelForm):

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
        ]


# Sign Up Form
class SignUpForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=30, required=False, help_text='Optional')
    last_name = forms.CharField(
        max_length=30, required=False, help_text='Optional')
    email = forms.EmailField(
        max_length=254, help_text='Enter a valid email address')

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        ]


class SimpleModelForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = '__all__'
        labels = {
            # 'title':'نام دسته بندی',
            # 'parent':'دسته پدر'
            # 'title': _('TITLE')
        }
        # widgets = {
        #     'name': Textarea(attrs={'cols': 80, 'rows': 20}),
        # }


class LoginForm(forms.Form):
    username = forms.CharField(label='username', max_length=255)
    password = forms.CharField(label='password', widget=forms.PasswordInput)


class TagForm(forms.ModelForm):

    class Meta:
        model = Tag
        fields = '__all__'


class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = '__all__'


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = '__all__'
