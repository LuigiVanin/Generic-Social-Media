from django.urls import path
from . import views

urlpatterns = [
    path("", views.login_reg, name="login"),
    path("reg/", views.registration, name="reg"),
    path("logout/", views.logout, name="logout"),
    path("profile/<str:acc>/", views.profile, name="profile"),
    path("result/", views.search_result, name="result"),
    path("new_img/", views.new_img, name="new_img"),
    path("add_friend/<str:friend>", views.make_friend, name="make_friend"),
    path("remove_friend/<str:friend>", views.remove_friend, name="remove_friend"),
    path("all_friends/", views.show_all_friends, name="show_friends" )
]