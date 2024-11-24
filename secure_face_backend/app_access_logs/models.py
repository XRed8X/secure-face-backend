from django.db import models
from app_users.models import CustomUser

# Create your models here.
class AccessLog(models.Model):
    """ Model to store logs of user access attemps """
    user = models.ForeignKey(
        CustomUser, 
        on_delete = models.SET_NULL,
        null = True, 
        blank = True,
        verbose_name = "User",
        help_text = "User attemp access (Null for unauthenticated attemps)."
    )
    timestamp = models.DateTimeField(auto_now_add = True, verbose_name = "Timestamp")
    ip_address = models.GenericIPAddressField(null = True, blank = True, verbose_name = "IP Address Address")
    success = models.BoleanField(default = False, verbose_name = "Success Attemp?")
    message = models.TextField(null = True, blank = True, verbose_name = "Message")
    
    def __str__(self):
        return f"{'Success' if self.success else 'Failed'} login for {self.user or 'Uknown User'} on {self.timestamp}"