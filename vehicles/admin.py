from django.contrib import admin
from django.utils.html import format_html

from .models import Vehicle, Sale


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
        "inventory_value_display",
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

    ordering = (
        "-created_at",
    )

    readonly_fields = (
        "image_preview",
        "inventory_value_display",
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
                    "inventory_value_display",
                )
            },
        ),
        (
            "Image Preview",
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
                '<img src="{}" width="120" height="80" style="border-radius:10px;border:1px solid #ccc;" />',
                obj.image.url
            )

        return "No Image Available"

    image_preview.short_description = "Preview"

    def stock_status(self, obj):

        if obj.quantity == 0:
            return "Out of Stock"

        if obj.quantity <= 5:
            return "Low Stock"

        return "In Stock"

    stock_status.short_description = "Stock Status"

    def inventory_value_display(self, obj):

        return f"₹ {obj.inventory_value:,.2f}"

    inventory_value_display.short_description = "Inventory Value"


@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "vehicle",
        "selling_price",
        "quantity",
        "total_amount_display",
        "sold_at",
    )

    search_fields = (
        "vehicle__make",
        "vehicle__model",
        "vehicle__category",
    )

    list_filter = (
        "sold_at",
        "vehicle__category",
    )

    ordering = (
        "-sold_at",
    )

    readonly_fields = (
        "vehicle",
        "selling_price",
        "quantity",
        "total_amount_display",
        "sold_at",
    )

    fieldsets = (
        (
            "Sale Details",
            {
                "fields": (
                    "vehicle",
                    "selling_price",
                    "quantity",
                    "total_amount_display",
                    "sold_at",
                )
            },
        ),
    )

    def total_amount_display(self, obj):

        return f"₹ {obj.total_amount:,.2f}"

    total_amount_display.short_description = "Total Amount"