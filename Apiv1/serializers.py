from djoser.serializers import UserCreateSerializer,UserSerializer
from rest_framework import serializers
from .models import*


class UserCreateSerializer(UserCreateSerializer):
    class meta(UserCreateSerializer.Meta):
        model =User
        fields='__all__'