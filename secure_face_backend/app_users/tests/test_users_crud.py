from rest_framework.test import APITestCase
from rest_framework import status
from app_users.models import CustomUser

class CustomUserCRUDTest(APITestCase):
    """Test suite for the CustomUser CRUD operations."""

    def setUp(self):
        """Set up initial data for testing."""
        self.user_data = {
            "email": "testuser@example.com",
            "username": "testuser",
            "password": "securepassword123"
        }
        self.user = CustomUser.objects.create_user(
            email=self.user_data["email"],
            username=self.user_data["username"],
            password=self.user_data["password"]
        )
        self.create_url = "/api/users/"
        self.detail_url = f"/api/users/{self.user.id}/"

    def test_create_user(self):
        """Test creating a user."""
        response = self.client.post(self.create_url, {
            "email": "newuser@example.com",
            "username": "newuser",
            "password": "anothersecurepassword"
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(CustomUser.objects.count(), 2)

    def test_list_users(self):
        """Test listing users."""
        response = self.client.get(self.create_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Only one user exists initially

    def test_retrieve_user(self):
        """Test retrieving a specific user."""
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["email"], self.user.email)

    def test_update_user(self):
        """Test updating a user's username."""
        response = self.client.patch(self.detail_url, {"username": "updateduser"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.user.refresh_from_db()
        self.assertEqual(self.user.username, "updateduser")

    def test_delete_user(self):
        """Test deleting a user."""
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(CustomUser.objects.count(), 0)
