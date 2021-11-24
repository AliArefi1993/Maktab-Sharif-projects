from django.db import models
from django.db.models.fields import CharField

# Create your models here.


class AvailableProductsManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='available')


# class AvailableProductsManager(models.QuerySet):
#     def get_queryset(self):
#         return super().get_queryset().filter(status='available')

class NonAvailableProductsManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='non_available')


class Product(models.Model):
    name = models.CharField(max_length=20)
    brand = models.CharField(max_length=50)
    status = models.CharField(max_length=15)  # select
    people = models.Manager()
    available = AvailableProductsManager()
    non_available = NonAvailableProductsManager()
