from rest_framework import serializers
from .models import Book
from django.contrib.auth.models import User


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields='__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','username','password']
        extra_kwargs={'password':{'write_only':True}}


# api/serializers.py
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        token['email'] = user.email
        # More custom fields can be added here

        return token

