from django.db import models
from shopUsers.models import Supplier, User, Customer
# Create your models here.


class Category(models.Model):
    category_name = models.CharField(max_length=200)
    category = models.ForeignKey(
        'self', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.category_name


class Product(models.Model):
    product_name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    unit_price = models.DecimalField(decimal_places=2, max_digits=11)
    is_discontinued = models.BooleanField()
    favourit_user_product = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return self.product_name


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)
    order_number = models.CharField(max_length=20)
    order_date = models.DateField()
    total_amount = models.IntegerField()

    def __str__(self):
        return self.order_number


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    unit_price = models.IntegerField()
    quantity = models.IntegerField()

    def __str__(self):
        return f'{self.product_id} : {self.quantity} '
