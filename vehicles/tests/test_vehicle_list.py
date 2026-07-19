from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from vehicles.models import Vehicle


class VehicleListTest(APITestCase):

    def setUp(self):

        Vehicle.objects.create(
            make="Toyota",
            model="Corolla",
            year=2022,
            price=25000,
            mileage=15000,
            fuel_type="Petrol",
            transmission="Automatic",
            description="Excellent Condition"
        )

    def test_vehicle_list_returns_data(self):

        url = reverse("vehicle-list")

        response = self.client.get(url)

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            len(response.data),
            1
        )

        self.assertEqual(
            response.data[0]["make"],
            "Toyota"
        )