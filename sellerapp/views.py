from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CustomerSerializer, ProductSerializer , CategorySerializer
from .models import Customer, Product, Category, Order
import requests

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

def CallbackView(request):
    code = request.GET.get('code')
    if not code:
           return JsonResponse({"error": "Missing authorization code"}, status=400)

    token_url = 'http://localhost:8000/auth/token/'
    client_id = 'zZ8mnCqVK5oaxZGs0zYfu08nJHPCkLbA3AC9QnMe'
    client_secret = 'pbkdf2_sha256$870000$QeTmagQSOqIWtfjBuxnsIc$WddVjlc6GDA/vaCApZyeJqwyaFyl8DQ+BYZG6eCCNBM='
    redirect_uri = 'http://localhost:8000/auth/callback/'
    data = {
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': redirect_uri,
        'client_id': client_id,
        'client_secret': client_secret
    }

    response = requests.post(token_url, data=data)
    if response.status_code != 200:
        return JsonResponse({"error":"Failed to get token"}, status=response.status_code)

    tokenAccess = response.json().get('access_token')
    tokenID = response.json().get('id_token')

    return JsonResponse({
        'id_token': id_token,
        'access_token': access_token,
        'token_type': token_json.get('token_type'),
        'expires_in': token_json.get('expires_in'),
    })






