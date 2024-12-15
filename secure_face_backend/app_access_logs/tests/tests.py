from django.test import TestCase

# Create your tests here.

from django.test import TestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from app_access_logs.models import AccessLog
from rest_framework.test import APIClient

class AccessLogTests(TestCase):
    
    def setUp(self):
        # Create a user
        self.user = get_user_model().objects.create_user(
            email='testuser@example.com',
            username='testuser',
            password='password123'
        )
        self.client = APIClient()
        
        # Create an access log for the user
        self.access_log = AccessLog.objects.create(
            user=self.user,
            timestamp='2024-11-24T12:00:00Z',
            ip_address='192.168.0.1',
            success=True,
            message='Login success'
        )
        
    def test_access_log_list(self):
        # Log in the user
        self.client.login(username='testuser', password='password123')
        
        # Request the list of access logs
        response = self.client.get('/api/access-logs/logs/')

        # Assert that the request was successful
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)
        self.assertEqual(response.data[0]['id'], self.access_log.id)
        self.assertEqual(response.data[0]['user'], self.access_log.user.id)

    def test_access_log_retrieve(self):
        # Log in the user
        self.client.login(username='testuser', password='password123')

        # Request the detail of a specific access log
        response = self.client.get(f'/api/access-logs/logs/{self.access_log.id}/')

        # Assert that the request was successful
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], self.access_log.id)
        self.assertEqual(response.data['user'], self.access_log.user.id)
        self.assertEqual(response.data['success'], self.access_log.success)

    def test_access_log_create_not_allowed(self):
        # Log in the user
        self.client.login(username='testuser', password='password123')

        # Attempt to create an access log (should fail)
        response = self.client.post('/api/access-logs/logs/', data={
            'user': self.user.id,
            'timestamp': '2024-11-24T12:00:00Z',
            'ip_address': '192.168.0.1',
            'success': True,
            'message': 'Login success'
        })
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)  # Method not allowed

    def test_access_log_update_not_allowed(self):
        # Log in the user
        self.client.login(username='testuser', password='password123')

        # Attempt to update an access log (should fail)
        response = self.client.put(f'/api/access-logs/logs/{self.access_log.id}/', data={
            'user': self.user.id,
            'timestamp': '2024-11-24T12:00:00Z',
            'ip_address': '192.168.0.1',
            'success': False,  # Change success status (should not be allowed)
            'message': 'Login failed'
        })
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)  # Method not allowed

    def test_access_log_delete_not_allowed(self):
        # Log in the user
        self.client.login(username='testuser', password='password123')

        # Attempt to delete an access log (should fail)
        response = self.client.delete(f'/api/access-logs/logs/{self.access_log.id}/')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)  # Method not allowed
