from django.db import models


class Vehicle(models.Model):

    CATEGORY_CHOICES = [
        ("Sedan", "Sedan"),
        ("SUV", "SUV"),
        ("Hatchback", "Hatchback"),
        ("Truck", "Truck"),
        ("Luxury", "Luxury"),
        ("Sports", "Sports"),
    ]

    make = models.CharField(max_length=100)

    model = models.CharField(max_length=100)

    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES
    )

    price = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    quantity = models.PositiveIntegerField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f"{self.make} {self.model}"