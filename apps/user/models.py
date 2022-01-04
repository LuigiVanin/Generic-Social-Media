from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    class GenderChoices(models.TextChoices):
        MALE='M'
        FEMALE='F'
        OTHER='O'
        
    bio = models.TextField(blank=True, max_length=500)
    gender = models.CharField(choices=GenderChoices.choices, max_length=3)
    profile_pic = models.ImageField(upload_to="photos/%d/%m/", blank=True)
    

class Friends(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=False, related_name='owner')
    friend = models.ForeignKey(User, on_delete=models.CASCADE, null=False, related_name='friend')