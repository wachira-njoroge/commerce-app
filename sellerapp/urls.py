from django.urls import path
from .views import(
    CustomerCreateAPIView,
    CustomerListAPIView,
    ProductCreateAPIView,
    CategoryCreateAPIView,
    CategoryListAPIView,
    ProductListAPIView,
    OrderCreateAPIView,
    OrderListAPIView
)

# Added URL patterns for creating and listing customers

urlpatterns = [
    path('customer/create/', CustomerCreateAPIView.as_view(), name='customer-create'),
    path('customer/list/', CustomerListAPIView.as_view(), name='customer-list'),
    path('product/create/', ProductCreateAPIView.as_view(), name='product-create'),
    path('product/list/', ProductListAPIView.as_view(), name='product-list'),
    path('category/create/', CategoryCreateAPIView.as_view(), name='category-create'),
    path('category/list/', CategoryListAPIView.as_view(), name='category-list'),
    path('order/create/', OrderCreateAPIView.as_view(), name='order-create'),
    path('order/list/', OrderListAPIView.as_view(), name='order-list')
]