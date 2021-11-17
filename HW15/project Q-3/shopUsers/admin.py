from django.contrib import admin
from .models import User, Customer, Supplier, Comment, EmailToCustomer, EmailToSupplier,  Category, Product, Order, OrderItem, Tag
# Register your models here.
admin.site.register(User)
admin.site.register(Customer)
admin.site.register(Supplier)
admin.site.register(Comment)
admin.site.register(EmailToSupplier)
admin.site.register(EmailToCustomer)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(OrderItem)
admin.site.register(Order)
admin.site.register(Tag)
