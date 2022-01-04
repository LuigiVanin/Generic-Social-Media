from django.contrib import admin
from .models import User, Friends
from django.contrib.auth import admin as auth_admin
from .forms import UserCreationForm, UserChangeForms


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    form = UserChangeForms
    add_form = UserCreationForm
    model = User
    fieldsets = auth_admin.UserAdmin.fieldsets + (
        (
            "Campos Personalizados", 
            {"fields": (
                "bio", 
                "gender", 
                "profile_pic"
            )}
        ),
    )
    
class AdminFriends(admin.ModelAdmin):
    list_display = (
        "owner",
        "friend"
    )
    
admin.site.register(Friends, AdminFriends)

