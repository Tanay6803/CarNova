from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from .models import Vehicle
from .serializers import VehicleSerializer


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