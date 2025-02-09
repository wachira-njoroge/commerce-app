from django.urls import path
from .views import(
    CustomerCreateAPIView,
    CustomerListAPIView,
    ProductCreateAPIView,
    CategoryCreateAPIView
)

# Added URL patterns for creating and listing customers

urlpatterns = [
    path('customer/create/', CustomerCreateAPIView.as_view(), name='customer-create'),
    path('customer/list/', CustomerListAPIView.as_view(), name='customer-list'),
    path('product/create/', ProductCreateAPIView.as_view(), name='product-create'),
    path('category/create/', CategoryCreateAPIView.as_view(), name='category-create')
]