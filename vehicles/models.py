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

    make = models.CharField(
        max_length=100
    )

    model = models.CharField(
        max_length=100
    )

    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES
    )

    image = models.ImageField(
        upload_to="vehicles/",
        blank=True,
        null=True
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

    class Meta:

        ordering = ["-created_at"]

    @property
    def inventory_value(self):

        return self.price * self.quantity

    @property
    def in_stock(self):

        return self.quantity > 0

    @property
    def low_stock(self):

        return 0 < self.quantity <= 5

    def __str__(self):

        return f"{self.make} {self.model}"


class Sale(models.Model):

    vehicle = models.ForeignKey(
        Vehicle,
        on_delete=models.CASCADE,
        related_name="sales"
    )

    selling_price = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    quantity = models.PositiveIntegerField(
        default=1
    )

    sold_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:

        ordering = ["-sold_at"]

    @property
    def total_amount(self):

        return self.selling_price * self.quantity

    def __str__(self):

        return (
            f"{self.vehicle.make} "
            f"{self.vehicle.model} "
            f"({self.quantity})"
        )