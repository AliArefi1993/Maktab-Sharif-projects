from django.db import models
# # from shopProduct.models import Product, OrderItem, Order

# # from django.db.models.base import Model


# class User(models.Model):
#     user_name = models.CharField(max_length=200)
#     password = models.CharField(max_length=200)  # Search
#     email = models.EmailField()
#     user_type = models.CharField(max_length=200)
#     phone = models.CharField(max_length=13)

#     def __str__(self):
#         return self.user_name


# class Customer(models.Model):
#     customer_name = models.CharField(max_length=200)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.customer_name


# class Supplier(models.Model):
#     supplier_name = models.CharField(max_length=200)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.supplier_name

# class Comment(models.Model):
#     Description = models.CharField(max_length=250)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.Description[0:10]


# class EmailToSupplier(models.Model):
#     order_item = models.ForeignKey(OrderItem, on_delete=models.CASCADE)
#     status = models.CharField(max_length=10)

#     def __str__(self):
#         return f'{self.order_item_id} : {self.status}'


# class EmailToCustomer(models.Model):
#     order = models.ForeignKey(Order, on_delete=models.CASCADE)
#     status = models.CharField(max_length=10)

#     def __str__(self):
#         return f'{self.order_id} : {self.status}'
