from django.urls import path
from app_access_logs.api.views import AccessLogDetailView, AccessLogListView

urlpatterns = [
    path('logs/', AccessLogListView.as_view(), name='access-logs-list-create'),
    path('logs/<int:pk>/', AccessLogDetailView.as_view(), name='access_log_detail'),
]
