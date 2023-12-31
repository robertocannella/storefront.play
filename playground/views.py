from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product
from store.models import Collection
from store.models import Customer
from store.models import Order
from store.models import OrderItem


def say_hello(request, name=None):
    return render(request, 'hello.html', {'name': name})


def get_all_products(request):
    query_set = Product.objects.all()
    return render(request, 'hello.html', {'name': 'Roberto', 'products': list(query_set)})


def get_all_customers(request):
    query_set = Customer.objects.all()
    return render(request, 'hello.html', {'name': 'Roberto', 'customers': list(query_set)})


def get_all_product_by_id(request, id):
    query_set = Product.objects.filter(pk=id)
    return render(request, 'product_show.html', {'product' : query_set[0]})


def get_products_by_price(request, unit_price):
    query_set = Product.objects.filter(unit_price=unit_price)
    return render(request, 'list_items.html', {'items': list(query_set)})


def get_products_by_price_range(request, min_price, max_price):
    products = Product.objects.filter(unit_price__gte=min_price, unit_price__lte=max_price)
    return render(request, 'list_items.html', {'items' : list(products)})
