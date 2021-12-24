from django.urls import path
from . import views

urlpatterns = [
    path("", views.login_reg, name="login"),
    path("reg/", views.registration, name="reg"),
    path("logout/", views.logout, name="logout"),
    path("profile/", views.profile, name="profile"),
    path("result/", views.search_result, name="result")
]