from rest_framework import serializers
from .models import Customer, Product, Order, Category

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['name', 'email', 'phone', 'region']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description']

class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)
    class Meta:
        model = Category
        fields = ['name', 'parent', 'products']

    def create(self, validated_data):
        products = validated_data.pop('products')
        parent = validated_data.pop('parent')
        parent_category = None

        if parent:
            parent_category = Category.objects.get(name=parent)

        category = Category.objects.create(parent = parent_category, **validated_data)

        for product_data in products:
            Product.objects.create(category=category, **product_data)
            
        return category