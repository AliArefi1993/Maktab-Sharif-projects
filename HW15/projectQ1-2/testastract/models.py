from django.db import models

# Create your models here.


class CommonInfo(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)

    class Meta:
        abstract = True


class Restaurant(CommonInfo):
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)
