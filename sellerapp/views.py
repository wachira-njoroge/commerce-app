from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CustomerSerializer, ProductSerializer , CategorySerializer
from .models import Customer, Product, Category, Order

class CustomerCreateAPIView(generics.CreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerListAPIView(generics.ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

# The below view is used to create a new product 
class ProductCreateAPIView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CategoryCreateAPIView(APIView):
    # queryset = Category.objects.all()
    # serializer_class = CategorySerializer
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











