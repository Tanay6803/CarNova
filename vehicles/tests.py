from django.contrib.auth.models import User
from django.urls import reverse

from rest_framework.test import APITestCase
from rest_framework import status

from rest_framework_simplejwt.tokens import RefreshToken

from .models import Vehicle


class VehicleAPITest(APITestCase):

    def setUp(self):

        self.user = User.objects.create_user(
            username="admin",
            password="password123"
        )

        refresh = RefreshToken.for_user(self.user)

        self.client.credentials(
            HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}"
        )

    def test_create_vehicle(self):

        url = reverse("vehicle-list")

        data = {

            "make": "Toyota",

            "model": "Fortuner",

            "category": "SUV",

            "price": 3500000,

            "quantity": 5

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
            Vehicle.objects.count(),
            1
        )

    def test_get_vehicle(self):

        Vehicle.objects.create(

            make="Toyota",

            model="Fortuner",

            category="SUV",

            price=3500000,

            quantity=5

        )

        response = self.client.get(
            reverse("vehicle-list")
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )