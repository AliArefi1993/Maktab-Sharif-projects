from django import forms
from .models import Tag, Category, Post
from django.contrib.auth.models import User


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
