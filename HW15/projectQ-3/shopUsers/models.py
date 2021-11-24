from django.db import models
# from django.db.models.base import Model


class User(models.Model):
    user_name = models.CharField(max_length=200)
    password = models.CharField(max_length=200)  # Search
    email = models.EmailField()
    user_type = models.CharField(max_length=200)
    phone = models.CharField(max_length=13)

    def __str__(self):
        return self.user_name


class Customer(models.Model):
    customer_name = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.customer_name


class Supplier(models.Model):
    supplier_name = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.supplier_name


class Comment(models.Model):
    Description = models.CharField(max_length=250)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.Description[0:10]


class EmailToSupplier(models.Model):
    order_item = models.ForeignKey('OrderItem', on_delete=models.CASCADE)
    status = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.order_item_id} : {self.status}'


class EmailToCustomer(models.Model):
    order = models.ForeignKey('Order', on_delete=models.CASCADE)
    status = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.order_id} : {self.status}'


class Category(models.Model):
    category_name = models.CharField(max_length=200)
    category_id = models.ForeignKey(
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


class Tag(models.Model):
    name = models.CharField(max_length=50)
    product = models.ManyToManyField('Product')

    def __str__(self):
        return self.name
