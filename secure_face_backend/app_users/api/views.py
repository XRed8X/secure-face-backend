from rest_framework import generics, permissions
from app_users.models import CustomUser
from app_users.api.serializers import CustomUserSerializer, CreateCustomUserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from .serializers import LoginSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny

class CustomUserListCreateView(generics.ListCreateAPIView):
    """ Handless listing all users and creating a new user """
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated]
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateCustomUserSerializer
        return CustomUserSerializer
    

class CustomUserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """ Handles retrieving, updating, and deleting a user by ID """
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated]
    
class LoginView(APIView):
    permission_classes = [AllowAny]  # Permite el acceso a cualquier usuario

    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)  # Crea o obtiene el token
            return Response({"token": token.key}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)