from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.product_list, name='products'),
    path('cart/', views.cart_view, name='cart'),
    path('add/<int:id>/', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:id>/', views.remove_from_cart, name='remove'),
    path('checkout/', views.checkout, name='checkout'),
    path('order-confirmed/', views.order_confirmed, name='order_confirmed'),
]