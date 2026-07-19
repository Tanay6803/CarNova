from rest_framework import serializers

from .models import Vehicle, Sale


class VehicleSerializer(serializers.ModelSerializer):

    image = serializers.ImageField(
        required=False,
        allow_null=True
    )

    inventory_value = serializers.ReadOnlyField()

    in_stock = serializers.ReadOnlyField()

    low_stock = serializers.ReadOnlyField()

    class Meta:

        model = Vehicle

        fields = [
            "id",
            "make",
            "model",
            "category",
            "image",
            "price",
            "quantity",
            "inventory_value",
            "in_stock",
            "low_stock",
            "created_at",
            "updated_at",
        ]

        read_only_fields = [
            "id",
            "inventory_value",
            "in_stock",
            "low_stock",
            "created_at",
            "updated_at",
        ]

    def validate_price(self, value):

        if value <= 0:

            raise serializers.ValidationError(
                "Price must be greater than zero."
            )

        return value

    def validate_quantity(self, value):

        if value < 0:

            raise serializers.ValidationError(
                "Quantity cannot be negative."
            )

        return value


class SaleSerializer(serializers.ModelSerializer):

    vehicle_name = serializers.SerializerMethodField()

    total_amount = serializers.ReadOnlyField()

    class Meta:

        model = Sale

        fields = [
            "id",
            "vehicle",
            "vehicle_name",
            "selling_price",
            "quantity",
            "total_amount",
            "sold_at",
        ]

        read_only_fields = [
            "id",
            "vehicle_name",
            "total_amount",
            "sold_at",
        ]

    def get_vehicle_name(self, obj):

        return f"{obj.vehicle.make} {obj.vehicle.model}"