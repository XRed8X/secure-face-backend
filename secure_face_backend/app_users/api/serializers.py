from rest_framework import serializers
from app_users.models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    """ Serializer for thee CustomUser model """
    
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'username', 'is_active', 'date_joined', 'last_login',]
        read_only_fields = ['date_joined', 'last_login']
        
class CreateCustomUserSerializer(serializers.ModelSerializer):
    """ Serializer to create a user with hashed password """
    
    class Meta:
        model = CustomUser
        fields = ['email', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}
        
    def create(self, validated_data):
        """ Override to hash the password """
        return CustomUser.objects.create_user(**validated_data)