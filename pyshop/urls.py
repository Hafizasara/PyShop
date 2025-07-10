from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # optional if using Allauth fully
    path('accounts/', include('accounts.urls')),              # your custom accounts app
    path('accounts/', include('allauth.urls')),               # ✅ Required for Allauth to work
    path('', include('products.urls')),
    path('cart/', include('cart.urls')),
]
