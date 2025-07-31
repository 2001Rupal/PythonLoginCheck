from django.shortcuts import render

# Create your views here.
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework import status
from django.views import View

from .serializers import UserLoginSerializer
from rest_framework.response import Response

class LoginView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            uname='rupal'
            upass='2222'
            user = authenticate(username=username, password=password)
            
            
            if user:
                
                return Response({"message": "Login successful"}, status=status.HTTP_200_OK)
            return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    




    
