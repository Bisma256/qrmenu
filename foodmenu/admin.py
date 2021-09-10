from django.contrib import admin
from .models.product import Product
from .models.category import Category
from .models.customer import Customer
from .models.orders import Order

class AdminProducts(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'category', 'image']

class AdminCategory(admin.ModelAdmin):
    list_display = ['id', 'name']

class AdminCustomer(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'phone']

class CustomerOrder(admin.ModelAdmin):
    list_display = ['id', 'product', 'customer', 'price', 'quantity', 'date', 'status']

# Register your models here.
admin.site.register(Product, AdminProducts)
admin.site.register(Category, AdminCategory)
admin.site.register(Customer, AdminCustomer)
admin.site.register(Order, CustomerOrder)