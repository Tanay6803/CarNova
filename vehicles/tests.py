from django.contrib.auth.models import User
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from rest_framework_simplejwt.tokens import RefreshToken

from .models import Vehicle


class VehicleAPITest(APITestCase):

    def setUp(self):

        self.user = User.objects.create_user(
            username="user",
            password="password123"
        )

        self.admin = User.objects.create_superuser(
            username="admin",
            email="admin@example.com",
            password="admin123"
        )

        refresh = RefreshToken.for_user(self.user)

        self.client.credentials(
            HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}"
        )

    # ----------------------------------
    # CREATE VEHICLE
    # ----------------------------------

    def test_create_vehicle(self):

        response = self.client.post(

            reverse("vehicle-list"),

            {

                "make": "Toyota",

                "model": "Fortuner",

                "category": "SUV",

                "price": 3500000,

                "quantity": 10

            },

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

    # ----------------------------------
    # LIST VEHICLES
    # ----------------------------------

    def test_list_vehicle(self):

        Vehicle.objects.create(

            make="BMW",

            model="X5",

            category="SUV",

            price=8000000,

            quantity=5

        )

        response = self.client.get(
            reverse("vehicle-list")
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            len(response.data),
            1
        )

    # ----------------------------------
    # SEARCH VEHICLE
    # ----------------------------------

    def test_search_vehicle(self):

        Vehicle.objects.create(

            make="Toyota",

            model="Fortuner",

            category="SUV",

            price=3500000,

            quantity=5

        )

        response = self.client.get(

            reverse("vehicle-search"),

            {

                "make": "Toyota"

            }

        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            len(response.data),
            1
        )

    # ----------------------------------
    # PURCHASE
    # ----------------------------------

    def test_purchase_vehicle(self):

        vehicle = Vehicle.objects.create(

            make="BMW",

            model="X5",

            category="SUV",

            price=7000000,

            quantity=3

        )

        response = self.client.post(

            reverse(

                "vehicle-purchase",

                args=[vehicle.id]

            )

        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        vehicle.refresh_from_db()

        self.assertEqual(
            vehicle.quantity,
            2
        )

    # ----------------------------------
    # OUT OF STOCK
    # ----------------------------------

    def test_purchase_out_of_stock(self):

        vehicle = Vehicle.objects.create(

            make="Audi",

            model="Q7",

            category="SUV",

            price=9000000,

            quantity=0

        )

        response = self.client.post(

            reverse(

                "vehicle-purchase",

                args=[vehicle.id]

            )

        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

    # ----------------------------------
    # ADMIN RESTOCK
    # ----------------------------------

    def test_admin_can_restock(self):

        refresh = RefreshToken.for_user(self.admin)

        self.client.credentials(

            HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}"

        )

        vehicle = Vehicle.objects.create(

            make="Honda",

            model="City",

            category="Sedan",

            price=1500000,

            quantity=2

        )

        response = self.client.post(

            reverse(

                "vehicle-restock",

                args=[vehicle.id]

            ),

            {

                "quantity": 5

            },

            format="json"

        )

        self.assertEqual(

            response.status_code,

            status.HTTP_200_OK

        )

        vehicle.refresh_from_db()

        self.assertEqual(

            vehicle.quantity,

            7

        )

    # ----------------------------------
    # NON ADMIN RESTOCK
    # ----------------------------------

    def test_user_cannot_restock(self):

        vehicle = Vehicle.objects.create(

            make="Honda",

            model="City",

            category="Sedan",

            price=1500000,

            quantity=2

        )

        response = self.client.post(

            reverse(

                "vehicle-restock",

                args=[vehicle.id]

            ),

            {

                "quantity": 5

            },

            format="json"

        )

        self.assertEqual(

            response.status_code,

            status.HTTP_403_FORBIDDEN

        )