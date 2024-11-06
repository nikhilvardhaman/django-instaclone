from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#CharField - varchar
#Boolean field
#Decimal field

class TimeStamp(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class UserProfile(TimeStamp):

    default_profile_pic_url = "https://mywebsite.com/image.png"

    profile_pic_url = models.ImageField(max_length=255, default=default_profile_pic_url)
    bio = models.CharField(max_length=255, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False) 
    is_verified = models.BooleanField(default=True)