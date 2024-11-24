from django.test import TestCase
from django.contrib.admin.sites import site
from app_users.admin import CustomUserAdmin
from app_users.models import CustomUser
from django.contrib.auth import get_user_model

class CustomUserAdminTest(TestCase):
    def test_admin_is_registered(self):
        """Test that CustomUser is registered with the admin."""
        self.assertIn(CustomUser, site._registry)

    def test_custom_user_admin_list_display(self):
        """Test the fields displayed in the user list in the admin panel."""
        user = CustomUser.objects.create_user(
            email="testuser@example.com", password="testpassword", username="testuser"
        )
        admin_obj = CustomUserAdmin(CustomUser, site)
        list_display = admin_obj.get_list_display(request=None)

        # Check if the list display contains the expected fields
        self.assertIn('email', list_display)
        self.assertIn('username', list_display)
