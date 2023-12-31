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
    # Get all products
    query_set = Product.objects.all()

    # Get all products, sort by unit price (ASC) then by title (DESC),
    query_set = Product.objects.order_by('unit_price', '-title')

    # Reverse the order
    query_set = Product.objects.order_by('unit_price', '-title').reverse()

    # Take first 5 elements
    query_set = Product.objects.order_by('unit_price', '-title').reverse()[:5]

    # Take the next 5 elements
    query_set = Product.objects.order_by('unit_price', '-title').reverse()[5:10]

    # Get only certain values from the database
    query_set = Product.objects.values('id', 'unit_price', 'title')

    # Get related table properties
    query_set = Product.objects.values('id', 'unit_price', 'title', 'collection__title')

    return render(request, 'list_products.html', {'products': list(query_set)})


def get_all_product_by_id(request, id):
    query_set = Product.objects.filter(pk=id)
    return render(request, 'product_show.html', {'product': query_set[0]})


def get_products_by_price(request, unit_price):
    query_set = Product.objects.filter(unit_price=unit_price)
    return render(request, 'list_products.html', {'products': list(query_set)})


def get_products_by_price_range(request, min_price, max_price):
    products = Product.objects.filter(unit_price__range=(min_price, max_price))
    return render(request, 'list_products.html', {'products': list(products)})


def get_ordered_products(request):
    # Get IDs of distinct products that have been ordered
    distinct_product_ids = OrderItem.objects.values_list('product_id').distinct()

    # Get products with those IDs, ordered by title
    products = Product.objects.filter(id__in=distinct_product_ids).order_by('title')

    return render(request, 'list_products.html', {'products': products})


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


# ORDER ITEMS
def get_order_items_by_collection_id(request, collection_id):
    query_set = OrderItem.objects.filter(product_id__collection_id=collection_id)
    return render(request, 'list_order_items.html', {'orderItems': list(query_set)})
