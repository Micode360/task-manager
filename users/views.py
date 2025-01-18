from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
from rest_framework import permissions
# Create your views here.

from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import AccessToken

class UserRegisterationView(APIView):
    permission_classes = [permissions.AllowAny]
    
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ "message": "User registered successfully" }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UserLoginView(APIView):
    permission_classes = [permissions.AllowAny]
    
    def post(self, request):
        data = request.data
        email = data.get('email', None)
        password = data.get('password', None)
        
        if email is None or password is None:
            return Response({ "error": "Please provide both email and password" }, status=status.HTTP_400_BAD_REQUEST)
        
        user = authenticate(email=email, password=password)
        
        if not user:
            return Response({ "error": "Invalid credentials" }, status=status.HTTP_404_NOT_FOUND)
        
        access = AccessToken.for_user(user)
        return Response({ "token": str(access) }, status=status.HTTP_200_OK)