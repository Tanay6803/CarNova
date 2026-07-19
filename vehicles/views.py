from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Vehicle
from .serializers import VehicleSerializer


# ==========================
# Vehicle CRUD
# ==========================

class VehicleListCreateView(generics.ListCreateAPIView):

    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    permission_classes = [IsAuthenticated]


class VehicleUpdateView(generics.RetrieveUpdateAPIView):

    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    permission_classes = [IsAuthenticated]


class VehicleDeleteView(generics.DestroyAPIView):

    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    permission_classes = [IsAdminUser]


# ==========================
# Vehicle Search
# ==========================

class VehicleSearchView(generics.ListAPIView):

    serializer_class = VehicleSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):

        queryset = Vehicle.objects.all()

        make = self.request.GET.get("make")
        model = self.request.GET.get("model")
        category = self.request.GET.get("category")

        min_price = self.request.GET.get("min_price")
        max_price = self.request.GET.get("max_price")

        if make:
            queryset = queryset.filter(make__icontains=make)

        if model:
            queryset = queryset.filter(model__icontains=model)

        if category:
            queryset = queryset.filter(category__icontains=category)

        if min_price:
            queryset = queryset.filter(price__gte=min_price)

        if max_price:
            queryset = queryset.filter(price__lte=max_price)

        return queryset


# ==========================
# Purchase Vehicle
# ==========================

class PurchaseVehicleView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request, pk):

        try:
            vehicle = Vehicle.objects.get(pk=pk)

        except Vehicle.DoesNotExist:

            return Response(
                {"error": "Vehicle not found."},
                status=status.HTTP_404_NOT_FOUND
            )

        if vehicle.quantity <= 0:

            return Response(
                {"error": "Vehicle is out of stock."},
                status=status.HTTP_400_BAD_REQUEST
            )

        vehicle.quantity -= 1
        vehicle.save()

        return Response(
            {
                "message": "Vehicle purchased successfully.",
                "remaining_quantity": vehicle.quantity
            },
            status=status.HTTP_200_OK
        )


# ==========================
# Restock Vehicle
# ==========================

class RestockVehicleView(APIView):

    permission_classes = [IsAdminUser]

    def post(self, request, pk):

        try:
            vehicle = Vehicle.objects.get(pk=pk)

        except Vehicle.DoesNotExist:

            return Response(
                {"error": "Vehicle not found."},
                status=status.HTTP_404_NOT_FOUND
            )

        quantity = int(request.data.get("quantity", 0))

        if quantity <= 0:

            return Response(
                {"error": "Quantity must be greater than zero."},
                status=status.HTTP_400_BAD_REQUEST
            )

        vehicle.quantity += quantity
        vehicle.save()

        return Response(
            {
                "message": "Vehicle restocked successfully.",
                "current_quantity": vehicle.quantity
            },
            status=status.HTTP_200_OK
        )