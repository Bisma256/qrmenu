from django.db import models
##from menuqrcodes.models import Menuqrcodes
from .product import Product
from .customer import Customer
import datetime

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    ##table = models.ForeignKey(Menuqrcodes, on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.datetime.today())
    status = models.BooleanField(default=False)

    @staticmethod
    def getByCustomer(cust_id):
        return Order.objects.filter(customer = cust_id).order_by('-date')

