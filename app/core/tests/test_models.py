from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):

    def test_create_user_with_email_successfull(self):
        """Test Creating a user with an email is successfull"""

        email = 'wenky4all@gmail.com'
        password = 'Sunny369'
        user = get_user_model().objects.create_user(
            email = email,
            password = password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the new user with a email is normalized"""
        email = 'wenky4all@GMAIL.COM'
        user = get_user_model().objects.create_user(email, 'Sunny369')

        self.assertEqual(user.email, email.lower())

    def test_new_user_email_invalid(self):
        """Test creating with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'Sunny369')

    def test_create_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            'wenky4all@gmail.com',
            'Sunny369'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
