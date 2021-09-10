from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models.product import Product
from .models.category import Category
from .models.customer import Customer
from menuqrcodes.models import Menuqrcodes
from .models.orders import Order
from django.views import View
from django.contrib.auth.decorators import login_required


# Create your views here.
class Index(View):
    def post(self, request):
        if request.session.get('customer'):
            product = request.POST.get('prodId')
            remove = request.POST.get('remove')
            cart = request.session.get('cart')
            if cart:
                quantity = cart.get(product)
                if quantity:
                    if remove:
                        if quantity <= 1:
                            cart.pop(product)
                        else:
                            cart[product] = quantity - 1
                    else:
                        cart[product] = quantity + 1
                else:
                    cart[product] = 1
            else:
                cart = {}
                cart[product] = 1
            request.session['cart'] = cart
            print(request.session['cart'])
            return redirect('menuindex')
        else:
            return redirect('signup')

    def get(self, request):
        if request.session.get('customer'):
            cart = request.session.get('cart')
            if not cart:
                request.session['cart'] = {}
            prod = None
            cat = Category.getAllCategory()
            cat_id = request.GET.get('category')
            if cat_id:
                prod = Product.getAllProductsByCategoryId(cat_id)
            else:
                prod = Product.getAllProducts()
            data = {}
            data['products'] = prod
            data['category'] = cat
            return render(request, 'index.html', data)
        else:
            return redirect('signup')


def signup(request):
    ##cust = Customer.getAllCustomer()
    if request.method == 'GET':
        return render(request, 'signup.html')  ##, cust)
    else:
        postData = request.POST
        cname = postData.get('cname')
        cemail = postData.get('cemail')
        cphone = postData.get('cphone')
        ##tname = postData.get('tname')

        value = {
            'name': cname,
            'email': cemail,
            'phone': cphone
        }

        error_msg = None

        if (not cname):
            error_msg = "Name Required!"
        elif len(cname) < 5:
            error_msg = "Name cannot be less than 5 characters!"
        if (not cemail):
            error_msg = "Email Required!"
        if (not cphone):
            error_msg = "Phone Number Required!"
        elif len(cphone) < 11:
            error_msg = "Phone number cannot be less than 11 numbers!"

        if (not error_msg):
            customer = Customer(name=cname, email=cemail, phone=cphone)  ##tablename = tname)
            customer.register()
            ##request.session['tableName'] = tname
            request.session['customerName'] = cname
            request.session['customer'] = customer.id
            return redirect('menuindex')

        else:
            data = {
                'error': error_msg,
                'values': value
            }

            return render(request, 'signup.html', data)


def logout(request):
    request.session.clear()
    return redirect('signup')


class Cart(View):
    def get(self, request):
        ids = list(request.session.get('cart').keys())
        products = Product.getById(ids)
        return render(request, 'cart.html', {'product': products})

class Checkout(View):
    def post(self, request):
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        products = Product.getById(list(cart.keys()))
        ##table = Menuqrcodes.getByQrId(cart.keys())

        for prod in products:
            order = Order(customer = Customer(id = customer),

                          product = prod,
                          price = prod.price,
                          quantity = cart.get(str(prod.id))
                          ##table = Menuqrcodes(id = table)
                          )
            order.save()
        request.session['cart'] = {}
        return redirect('cart')

class Orders(View):
    def get(self, request):
        customer = request.session.get('customer')
        orders = Order.getByCustomer(customer)
        return render(request, 'orders.html', {'order': orders})
