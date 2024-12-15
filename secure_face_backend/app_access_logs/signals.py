# app_access_logs/signals.py

from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from django.utils.timezone import now
from app_access_logs.models import AccessLog

@receiver(user_logged_in)
def log_user_login(sender, request, user, **kwargs):
    """
    Signal triggered when a user logs in successfully.
    """
    # Obtén la dirección IP del usuario desde el request
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip_address = x_forwarded_for.split(',')[0]
    else:
        ip_address = request.META.get('REMOTE_ADDR')

    # Crea un nuevo registro en los AccessLogs
    AccessLog.objects.create(
        user=user,
        timestamp=now(),
        ip_address=ip_address,
        success=True,
        message="User logged in successfully."
    )
