# api/urls.py
from django.urls import path
from .views import ProductSearchAPIView

urlpatterns = [
    path('products/search/', ProductSearchAPIView.as_view(), name='product-search'),
]