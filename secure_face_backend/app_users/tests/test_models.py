from django.test import TestCase
from app_users.models import CustomUser

class CustomUserModelTest(TestCase):
    def test_create_user(self):
        """Test creating a user with email and password."""
        user = CustomUser.objects.create_user(
        email="testuser@example.com", password="testpassword"
        )

        self.assertEqual(user.email, "testuser@example.com")
        self.assertTrue(user.check_password("testpassword"))
        self.assertFalse(user.is_staff)  # Confirming that is_staff is False
        self.assertTrue(user.is_superuser)  # Confirming that is_superuser is True


    def test_create_superuser(self):
        """Test creating a superuser."""
        superuser = CustomUser.objects.create_superuser(
            email="admin@example.com", password="adminpassword", username="admin"
        )

        self.assertEqual(superuser.email, "admin@example.com")
        self.assertTrue(superuser.check_password("adminpassword"))
        self.assertTrue(superuser.is_staff)
        self.assertTrue(superuser.is_superuser)  # Confirming that is_superuser is True


    def test_user_str_method(self):
        """Test the __str__ method of the CustomUser model."""
        user = CustomUser.objects.create_user(
            email="testuser@example.com", password="testpassword", username="testuser"
        )
        self.assertEqual(str(user), "testuser")
