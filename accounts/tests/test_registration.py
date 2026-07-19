from django.contrib.auth.models import User

from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase


class RegistrationTest(APITestCase):

    def test_user_can_register(self):

        url = reverse("register")

        data = {

            "username": "spidey",

            "email": "spidey@gmail.com",

            "password": "StrongPassword123"

        }

        response = self.client.post(
            url,
            data,
            format="json"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            User.objects.count(),
            1
        )

        user = User.objects.first()

        self.assertEqual(
            user.username,
            "spidey"
        )

        self.assertEqual(
            user.email,
            "spidey@gmail.com"
        )

        self.assertTrue(
            user.check_password(
                "StrongPassword123"
            )
        )

    def test_duplicate_username(self):

        User.objects.create_user(
            username="spidey",
            email="abc@gmail.com",
            password="password123"
        )

        response = self.client.post(

            reverse("register"),

            {

                "username": "spidey",

                "email": "xyz@gmail.com",

                "password": "password123"

            },

            format="json"

        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

    def test_duplicate_email(self):

        User.objects.create_user(

            username="abc",

            email="spidey@gmail.com",

            password="password123"

        )

        response = self.client.post(

            reverse("register"),

            {

                "username": "xyz",

                "email": "spidey@gmail.com",

                "password": "password123"

            },

            format="json"

        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )