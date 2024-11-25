from django.urls import path
from app_users.api.views import CustomUserListCreateView, CustomUserRetrieveUpdateDestroyView, LoginView

urlpatterns = [
    path('users/', CustomUserListCreateView.as_view(), name='user-list-create'),
    path('users/update/<int:pk>/', CustomUserRetrieveUpdateDestroyView.as_view(), name='user-detail'),
    path('login/', LoginView.as_view(), name='login'),
]