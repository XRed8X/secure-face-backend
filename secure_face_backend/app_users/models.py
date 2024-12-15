from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Custom manager for user creation
class CustomUserManager(BaseUserManager):
    """
    Class that handles the creation of users in the custom model
    """
    def create_user(self, email, password=None, **extra_fields):
        """
        Create and return a regular user with an email and password
        """
        if not email:
            raise ValueError("The Email must be provided")
        if not password:
            raise ValueError("The Password must be provided")
        
        # Normalize the email to avoid duplicates due to uppercase/lowercase letters
        email = self.normalize_email(email)
        
        # Create an instance of the user with the provided data
        user = self.model(email=email, **extra_fields)
        
        # Hash and save the password
        user.set_password(password)
        
        # Save the user to the database
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, username=None, password=None, **extra_fields):
        """
        Create and return a superuser with the given email, username, and password
        """
        # Ensure the superuser has the right flags
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_active", True)

        # Call create_user to create the superuser
        return self.create_user(email, password=password, username=username, **extra_fields)


# Custom model for users
class CustomUser(AbstractBaseUser, PermissionsMixin):
    """ Custom model for users """
    
    # Fields for users
    email = models.EmailField(unique=True, max_length=255, verbose_name="Email")
    username = models.CharField(unique=True, max_length=50, verbose_name="Username")
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name="Registration date")
    last_login = models.DateTimeField(auto_now=True)
    
    # Field for facial recognition data
    facial_data = models.TextField(null=True, blank=True, verbose_name="Facial data")
    
    # Basic boolean flags
    is_active = models.BooleanField(default=True, verbose_name="Is active?")
    is_staff = models.BooleanField(default=False, verbose_name="Is staff?")
    is_superuser = models.BooleanField(default=True, verbose_name="Is superuser?")
    
    # Manager to handle actions for this model
    objects = CustomUserManager()

    # The field used for login purposes
    USERNAME_FIELD = 'email'
    
    # Additional required fields when creating a user (username is required)
    REQUIRED_FIELDS = ['username']
    
    def __str__(self):
        return self.username
