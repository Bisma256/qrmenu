from django.contrib import admin
from .models import Menuqrcodes


class Adminqrcode(admin.ModelAdmin):
    list_display = ['id', 'name', 'qr_code']

# Register your models here.
admin.site.register(Menuqrcodes, Adminqrcode)
