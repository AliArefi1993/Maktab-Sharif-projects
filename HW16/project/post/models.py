from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import DO_NOTHING
from django.db.models.fields import BLANK_CHOICE_DASH
from django.template.defaultfilters import slugify
from django.template.defaultfilters import slugify
import random
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    owner = models.ForeignKey(User, on_delete=DO_NOTHING)
    pub_date = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=100, unique=True)

    def random_number_generator(self):

        return str(random.randint(1000, 9999))

    def save(self, *args, **kwargs):

        if not self.slug:
            self.slug = slugify(self.title)
        while Post.objects.filter(slug=self.slug):
            self.slug = slugify(self.title)
            self.slug += self.random_number_generator()
        return super().save(*args, **kwargs)


def __str__(self) -> str:
    return self.title


class Comment(models.Model):
    text = models.CharField(max_length=200)
    post = models.ForeignKey(Post, on_delete=DO_NOTHING)
    user = models.ForeignKey(User, on_delete=DO_NOTHING)

    def __str__(self) -> str:
        return self.text[:10]


class Category(models.Model):
    name = models.CharField(max_length=50)
    post = models.ManyToManyField(Post)

    def __str__(self) -> str:
        return self.name
