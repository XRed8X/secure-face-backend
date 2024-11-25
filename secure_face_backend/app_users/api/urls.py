from django.urls import path
from app_users.api.views import CustomUserListCreateView, CustomUserRetrieveUpdateDestroyView, LoginView, RegisterUserView

urlpatterns = [
    path('users/', CustomUserListCreateView.as_view(), name='user-list-create'),
    path('users/update/<int:pk>/', CustomUserRetrieveUpdateDestroyView.as_view(), name='user-detail'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterUserView.as_view(), name='register-user'),  # Endpoint para registrar usuarios
]
