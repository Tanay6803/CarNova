from django.shortcuts import render, get_object_or_404
from django.db.models import Q, Sum
from django.utils import timezone

from vehicles.models import Vehicle, Sale


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
    sales = Sale.objects.select_related("vehicle").order_by("-sold_at")

    # Dashboard Statistics
    total_vehicles = vehicles.count()

    inventory = vehicles.aggregate(
        total=Sum("quantity")
    )["total"] or 0

    low_stock = vehicles.filter(
        quantity__gt=0,
        quantity__lte=5
    ).count()

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

    total_sales = sales.count()

    total_revenue = sum(
        sale.total_amount
        for sale in sales
    )

    today = timezone.now().date()

    todays_sales = sales.filter(
        sold_at__date=today
    ).count()

    best_selling_vehicle = (
        Sale.objects
        .values(
            "vehicle__make",
            "vehicle__model",
        )
        .annotate(
            total_sold=Sum("quantity")
        )
        .order_by("-total_sold")
        .first()
    )

    recent_sales = sales[:10]

    return render(
        request,
        "dashboard.html",
        {
            "vehicles": vehicles,
            "recent_sales": recent_sales,

            "total_vehicles": total_vehicles,
            "inventory": inventory,
            "low_stock": low_stock,

            "inventory_value": inventory_value,
            "total_categories": total_categories,
            "out_of_stock": out_of_stock,

            "total_sales": total_sales,
            "total_revenue": total_revenue,
            "todays_sales": todays_sales,
            "best_selling_vehicle": best_selling_vehicle,
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