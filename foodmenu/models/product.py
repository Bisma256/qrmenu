from django.db import models
from .category import Category

class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to='uploads/product/')

    @staticmethod
    def getById(ids):
        return Product.objects.filter(id__in=ids)

    @staticmethod
    def getAllProducts():
        return Product.objects.all()

    @staticmethod
    def getAllProductsByCategoryId(category_id):
        if category_id:
            return Product.objects.filter(category = category_id)
        else:
            return Product.getAllProducts()

    def __str__(self):
        return self.name