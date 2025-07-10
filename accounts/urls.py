from django.urls import path
from . import views
from .views import CustomLoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', CustomLoginView.as_view(), name='account_login'),  # ✅ use only this
    path('logout/', LogoutView.as_view(next_page='/accounts/login/'), name='account_logout'),
]
