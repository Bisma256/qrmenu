from django.shortcuts import render
from .models import Menuqrcodes

# Create your views here.

def home_view(request):
    name = "Welcome to"

    obj = Menuqrcodes.objects.all()
    context = {
        'name': name,
        'obj': obj,
    }

    return render(request, 'qrcodes.html', context)

