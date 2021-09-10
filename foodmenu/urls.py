from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name="menuindex"),
    path('signup', views.signup, name="signup"),
    path('logout', views.logout, name="logout"),
    path('cart', views.Cart.as_view(), name="cart"),
    path('checkout', views.Checkout.as_view(), name="checkout"),
    path('orders', views.Orders.as_view(), name="orders"),
]
