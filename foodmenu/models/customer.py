from django.db import models
from menuqrcodes.models import Menuqrcodes

class Customer(models.Model):
    name = models.CharField(max_length=100)
    ## qrtable = models.ForeignKey(Menuqrcodes, on_delete=models.CASCADE)
    ## tablename = models.CharField(Menuqrcodes.name, max_length=50)
    phone = models.CharField(max_length=11)
    email = models.EmailField()

    def register(self):
        return self.save()

    def __str__(self):
        return self.name



    ##@staticmethod
    ##def getAllCustomer():
      ##  return Customer.objects.tablename()