from django.urls import path
from . import views

urlpatterns = [
    path("", views.login_reg, name="login"),
    path("reg/", views.registration, name="reg"),
    path("logout/", views.logout, name="logout")
]