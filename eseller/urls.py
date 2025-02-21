from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('sellerapp.urls')),
    path('auth/', include("oauth2_provider.urls", namespace="oauth2_provider")),
    path("accounts/login/", auth_views.LoginView.as_view(), name="login")
]
