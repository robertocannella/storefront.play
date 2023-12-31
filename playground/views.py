from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product
from store.models import Collection
from store.models import Customer
from store.models import Order
from store.models import OrderItem


def say_hello(request, name=None):
    return render(request, 'hello.html', {'name': name})


# PRODUCTS

def get_all_products(request):
    query_set = Product.objects.all()
    return render(request, 'hello.html', {'name': 'Roberto', 'products': list(query_set)})


def get_all_product_by_id(request, id):
    query_set = Product.objects.filter(pk=id)
    return render(request, 'product_show.html', {'product': query_set[0]})


def get_products_by_price(request, unit_price):
    query_set = Product.objects.filter(unit_price=unit_price)
    return render(request, 'list_products.html', {'products': list(query_set)})


def get_products_by_price_range(request, min_price, max_price):
    products = Product.objects.filter(unit_price__range=(min_price, max_price))
    return render(request, 'list_products.html', {'products': list(products)})


def search_product_title(request, query):
    products = Product.objects.filter(title__icontains=query)
    return render(request, 'list_products.html', {'products': list(products)})


# CUSTOMERS
def get_all_customers(request):
    query_set = Customer.objects.all()
    return render(request, 'list_customers.html', {'customers': list(query_set)})


def search_customer_by_email(request, email_query):
    query_set = Customer.objects.filter(email__icontains=email_query)
    return render(request, 'list_customers.html', {'customers': list(query_set)})


# COLLECTIONS
def get_all_collections(request):
    query_set = Collection.objects.all()
    return render(request, 'list_collections.html', {'collections': list(query_set)})


def get_all_collections_without_featured_product(request):
    query_set = Collection.objects.filter(featured_product__isnull=True)
    return render(request, 'list_collections.html', {'collections': list(query_set)})


# ORDERS
def get_orders_by_customer_id(request, customer_id):
    query_set = Order.objects.filter(customer_id=customer_id)
    return render(request, 'list_orders.html', {'orders': list(query_set)})
