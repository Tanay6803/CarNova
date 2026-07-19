from django.db.models import Q

from rest_framework import generics, status
from rest_framework.parsers import (
    JSONParser,
    MultiPartParser,
    FormParser,
)
from rest_framework.permissions import (
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
)
from rest_framework.response import Response

from .models import Vehicle
from .serializers import VehicleSerializer


class VehicleListCreateView(generics.ListCreateAPIView):

    queryset = Vehicle.objects.all().order_by("-created_at")
    serializer_class = VehicleSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    parser_classes = [
        JSONParser,
        MultiPartParser,
        FormParser,
    ]


class VehicleUpdateView(generics.UpdateAPIView):

    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    permission_classes = [IsAuthenticated]

    parser_classes = [
        JSONParser,
        MultiPartParser,
        FormParser,
    ]


class VehicleDeleteView(generics.DestroyAPIView):

    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    permission_classes = [IsAuthenticated]


class VehicleSearchView(generics.ListAPIView):

    serializer_class = VehicleSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):

        query = self.request.GET.get("q", "")

        return Vehicle.objects.filter(
            Q(make__icontains=query) |
            Q(model__icontains=query) |
            Q(category__icontains=query)
        ).order_by("-created_at")


class PurchaseVehicleView(generics.GenericAPIView):

    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):

        vehicle = self.get_object()

        if vehicle.quantity <= 0:

            return Response(
                {
                    "error": "Vehicle Out of Stock"
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        vehicle.quantity -= 1
        vehicle.save()

        return Response(
            {
                "message": "Vehicle Purchased Successfully"
            }
        )


class RestockVehicleView(generics.GenericAPIView):

    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):

        if not request.user.is_staff:

            return Response(
                {
                    "detail": "You do not have permission to perform this action."
                },
                status=status.HTTP_403_FORBIDDEN
            )

        vehicle = self.get_object()

        try:

            quantity = int(request.data.get("quantity", 1))

        except (TypeError, ValueError):

            return Response(
                {
                    "error": "Invalid quantity."
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        if quantity <= 0:

            return Response(
                {
                    "error": "Quantity must be greater than zero."
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        vehicle.quantity += quantity
        vehicle.save()

        return Response(
            {
                "message": "Vehicle Restocked Successfully"
            }
        )