from rest_framework import serializers
from app_users.models import CustomUser
from django.contrib.auth import authenticate

class CustomUserSerializer(serializers.ModelSerializer):
    """ Serializer for thee CustomUser model """
    
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'username', 'is_active', 'date_joined', 'last_login',]
        read_only_fields = ['id', 'date_joined', 'last_login']
        
class CreateCustomUserSerializer(serializers.ModelSerializer):
    """ Serializer to create a user with hashed password """
    
    class Meta:
        model = CustomUser
        fields = ['email', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}
        
    def create(self, validated_data):
        """ Override to hash the password """
        return CustomUser.objects.create_user(**validated_data)
    
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(username=data['email'], password=data['password'])
        if user is None:
            raise serializers.ValidationError("Invalid credentials")
        return {'user': user}