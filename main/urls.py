from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.products, name='products'),
    path('product/<int:id>/', views.product_detail, name='product_detail'),
    path('search_suggestions/', views.search_suggestions, name='search_suggestions'),
]
