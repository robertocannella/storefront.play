from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product
from store.models import Collection
from store.models import Customer
from store.models import Order
from store.models import OrderItem


def say_hello(request):
    query_set = Product.objects.all()
    return render(request, 'hello.html', {'name': 'Roberto', 'products': list(query_set)})
