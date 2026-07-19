from django.contrib import admin
from django.utils.html import format_html

from .models import Vehicle


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "image_preview",
        "make",
        "model",
        "category",
        "price",
        "quantity",
        "stock_status",
        "created_at",
    )

    search_fields = (
        "make",
        "model",
        "category",
    )

    list_filter = (
        "category",
        "created_at",
    )

    readonly_fields = (
        "image_preview",
        "created_at",
        "updated_at",
    )

    fieldsets = (
        (
            "Vehicle Information",
            {
                "fields": (
                    "make",
                    "model",
                    "category",
                    "image",
                )
            },
        ),
        (
            "Inventory",
            {
                "fields": (
                    "price",
                    "quantity",
                )
            },
        ),
        (
            "Preview",
            {
                "fields": (
                    "image_preview",
                )
            },
        ),
        (
            "Timestamps",
            {
                "fields": (
                    "created_at",
                    "updated_at",
                )
            },
        ),
    )

    def image_preview(self, obj):

        if obj.image:
            return format_html(
                '<img src="{}" width="80" height="60" style="border-radius:8px;" />',
                obj.image.url
            )

        return "No Image"

    image_preview.short_description = "Preview"

    def stock_status(self, obj):

        if obj.quantity == 0:
            return "Out of Stock"

        if obj.quantity <= 5:
            return "Low Stock"

        return "In Stock"

    stock_status.short_description = "Status"