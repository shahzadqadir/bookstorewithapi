from django.urls import path

from .views import CustomUserRegistration

urlpatterns = [
    path("signup/", CustomUserRegistration.as_view(), name="signup"),
]