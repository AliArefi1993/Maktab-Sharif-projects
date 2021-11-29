from django import forms
from django.forms import fields
from shopUsers.models import Tag, Comment
from django.forms.fields import ChoiceField


class NameForm(forms.Form):
    your_name1 = forms.CharField(label='name', max_length=30, help_text='help')
    your_name2 = forms.CharField(label='your_name', max_length=30)
    your_name3 = forms.CharField(label='your_name', max_length=30)
    your_name4 = forms.CharField(label='your_name', max_length=30)
    text = forms.CharField(label='question', widget=forms.Textarea)
    phone = forms.IntegerField()
    password = forms.CharField(widget=forms.PasswordInput)
    tags = forms.ModelChoiceField(
        label='model choice', queryset=Tag.objects.all())


class CommentMethodForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['text']
