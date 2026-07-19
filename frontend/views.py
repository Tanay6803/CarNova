from django.shortcuts import render, get_object_or_404
from django.db.models import Q

from vehicles.models import Vehicle


def home(request):

    search = request.GET.get("search", "")
    category = request.GET.get("category", "")

    vehicles = Vehicle.objects.all().order_by("-created_at")

    if search:
        vehicles = vehicles.filter(
            Q(make__icontains=search) |
            Q(model__icontains=search)
        )

    if category:
        vehicles = vehicles.filter(category=category)

    return render(
        request,
        "home.html",
        {
            "vehicles": vehicles,
            "search": search,
            "selected_category": category,
            "categories": [
                "Sedan",
                "SUV",
                "Hatchback",
                "Truck",
                "Luxury",
                "Sports",
            ],
        },
    )


def vehicle_details(request, pk):

    vehicle = get_object_or_404(
        Vehicle,
        pk=pk
    )

    return render(
        request,
        "vehicle_details.html",
        {
            "vehicle": vehicle
        },
    )


def login_page(request):

    return render(
        request,
        "login.html"
    )


def register_page(request):

    return render(
        request,
        "register.html"
    )


def dashboard(request):

    vehicles = Vehicle.objects.all().order_by("-created_at")

    total_vehicles = vehicles.count()

    inventory_value = sum(
        vehicle.price * vehicle.quantity
        for vehicle in vehicles
    )

    total_categories = (
        vehicles.values("category")
        .distinct()
        .count()
    )

    out_of_stock = vehicles.filter(
        quantity=0
    ).count()

    return render(
        request,
        "dashboard.html",
        {
            "vehicles": vehicles,
            "total_vehicles": total_vehicles,
            "inventory_value": inventory_value,
            "total_categories": total_categories,
            "out_of_stock": out_of_stock,
        },
    )


def add_vehicle(request):

    return render(
        request,
        "add_vehicle.html"
    )


def edit_vehicle(request, pk):

    vehicle = get_object_or_404(
        Vehicle,
        pk=pk
    )

    return render(
        request,
        "edit_vehicle.html",
        {
            "vehicle": vehicle
        },
    )