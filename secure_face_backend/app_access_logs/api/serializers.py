from rest_framework import serializers
from app_access_logs.models import AccessLog
from app_users.models import CustomUser

class AccessLogSerializer(serializers.ModelSerializer):
    user_email = serializers.EmailField(source='user.email', read_only=True)  # Ejemplo para mostrar el email del usuario
    
    class Meta:
        model = AccessLog
        fields = ['id', 'user', 'user_email', 'timestamp', 'ip_address', 'success', 'message']
        read_only_fields = ['id', 'user', 'timestamp', 'ip_address', 'success', 'message']