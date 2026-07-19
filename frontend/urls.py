from django.urls import path

from .views import (
    home,
    vehicle_details,
    login_page,
    register_page,
    dashboard,
    add_vehicle,
    edit_vehicle,
)

urlpatterns = [

    path("", home, name="home"),

    path(
        "vehicle/<int:pk>/",
        vehicle_details,
        name="vehicle-details",
    ),

    path(
        "login/",
        login_page,
        name="login",
    ),

    path(
        "register/",
        register_page,
        name="register",
    ),

    path(
        "dashboard/",
        dashboard,
        name="dashboard",
    ),

    path(
        "add-vehicle/",
        add_vehicle,
        name="add-vehicle",
    ),

    path(
        "edit-vehicle/<int:pk>/",
        edit_vehicle,
        name="edit-vehicle",
    ),

]