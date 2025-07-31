from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class UserLoginSerializer(serializers.Serializer):
        username = serializers.CharField()
        password = serializers.CharField(write_only=True)


