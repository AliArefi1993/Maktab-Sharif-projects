from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.deletion import DO_NOTHING
from django.db.models.fields import BLANK_CHOICE_DASH
from django.template.defaultfilters import slugify
from django.template.defaultfilters import slugify
import random

User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    owner = models.ForeignKey(User, on_delete=DO_NOTHING)
    pub_date = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=100, unique=True)
    image = models.ImageField(blank=True, null=True)
    tag = models.ManyToManyField(Tag, blank=True, null=True)
    category = models.ManyToManyField(Category, blank=True, null=True)

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
    post = models.ForeignKey(Post, on_delete=DO_NOTHING,
                             related_name='comments_post')
    user = models.ForeignKey(User, on_delete=DO_NOTHING)

    def __str__(self) -> str:
        return self.text[:10]
