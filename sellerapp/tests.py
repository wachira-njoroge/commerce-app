import unittest
import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'eseller.settings')
django.setup()
from sellerapp.models import Customer, Category
from django.urls import reverse
from sellerapp.views import CustomerCreateAPIView, CategoryCreateAPIView
from django.test import TestCase, Client

class TestCases(TestCase):
    def setUp(self):
        self.client = Client()
    
    def test_customer_create(self):
        response = self.client.post('customer-create', {
            'name': 'Wafula',
            'email': 'wafula@gmail.com'
            })
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['name'], 'Wafula')

    def test_category_create(self):
        response = self.client.post('/category/create/', {
            'categories': [
                {
                    'name': 'Furniture',
                    'products': [
                        {
                            'name': 'Table',
                            'price': 5000,
                            'description': 'Coffee Table'
                        }
                    ]
                }
            ]
        })
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['message'], 'Categories and products created successfully')

        if __name__ == '__main__':
            unittest.main()