from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User 
from .models import UserProfile
from django.contrib.auth.hashers import make_password
 

class UserCreateSerializer(ModelSerializer):

    def create(self, validate_data):
        validate_data['password'] = make_password(validate_data['password'])

        user = User.objects.create(**validate_data)

        UserProfile.objects.create(user=user)

        return user
    

    class Meta:
        model = User
        fields = ('username', 'password', 'email',)


class UserViewSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username',)

class UserProfileViewSerializer(ModelSerializer):

    user = UserViewSerializer()

    class Meta:
        model = UserProfile
        #fields = ('bio', 'profile_pic_url', 'user')
        exclude = ('id', 'is_verified')
