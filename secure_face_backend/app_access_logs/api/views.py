from rest_framework import generics
from app_access_logs.models import AccessLog
from app_access_logs.api.serializers import AccessLogSerializer

class AccessLogListView(generics.ListAPIView):
    """ Endpoint para ver los registros de accesos """
    queryset = AccessLog.objects.all()
    serializer_class = AccessLogSerializer
    
class AccessLogDetailView(generics.RetrieveAPIView):
    queryset = AccessLog.objects.all()
    serializer_class = AccessLogSerializer