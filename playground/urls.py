from django.urls import path
from . import views

# URLConf
urlpatterns = [

    path('hello/', views.say_hello),
    path('hello/<str:name>/', views.say_hello),
    path('products/', views.get_all_products),
    path('products/<str:id>/',views.get_all_product_by_id),
    path('products/price/<int:unit_price>/', views.get_products_by_price),
    path('products/price/<int:min_price>/<int:max_price>/', views.get_products_by_price_range),
    path('customers/', views.get_all_customers),

]

