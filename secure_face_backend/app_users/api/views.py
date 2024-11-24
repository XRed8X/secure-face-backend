from rest_framework import generics, permissions
from app_users.models import CustomUser
from app_users.api.serializers import CustomUserSerializer, CreateCustomUserSerializer

class CustomUserListCreateView(generics.ListCreateAPIView):
    """ Handless listing all users and creating a new user """
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateCustomUserSerializer
        return CustomUserSerializer

class CustomUserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """ Handles retrieving, updating, and deleting a user by ID """
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer