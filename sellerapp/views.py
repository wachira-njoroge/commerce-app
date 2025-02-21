from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CustomerSerializer, ProductSerializer , CategorySerializer, OrderSerializer
from .models import Customer, Product, Category, Order
import requests

class CustomerCreateAPIView(generics.CreateAPIView):
    serializer_class = CustomerSerializer
    http_method_names = ['post']

class CustomerListAPIView(generics.ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# The below view is used to create a new product 
class ProductCreateAPIView(generics.CreateAPIView):
    serializer_class = ProductSerializer

class CategoryCreateAPIView(generics.CreateAPIView):
    serializer_class = CategorySerializer
    def post(self, request):
        data = request.data.get('categories', [])

        for category_data in data:
            parent_name = category_data.get('parent')
            category_name = category_data.get('name')
            products_data = category_data.get('products', [])

            # Get or create parent category
            parent_category, _ = Category.objects.get_or_create(name=parent_name, defaults={'parent': None})

            # Get or create the category
            category, _ = Category.objects.get_or_create(name=category_name, parent=parent_category)

            # Create associated products
            for product_data in products_data:
                Product.objects.get_or_create(category=category, **product_data)

        return Response({"message": "Categories and products created successfully"}, status=status.HTTP_201_CREATED)

class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()   
    serializer_class = CategorySerializer

class OrderCreateAPIView(generics.CreateAPIView):
    serializer_class = OrderSerializer
    http_method_names = ['post']

class OrderListAPIView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer






