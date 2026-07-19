from django.urls import path

from .views import (
    VehicleListCreateView,
    VehicleUpdateView,
    VehicleDeleteView,
    VehicleSearchView,
)

urlpatterns = [

    path(
        "",
        VehicleListCreateView.as_view(),
        name="vehicle-list"
    ),

    path(
        "search/",
        VehicleSearchView.as_view(),
        name="vehicle-search"
    ),

    path(
        "<int:pk>/",
        VehicleUpdateView.as_view(),
        name="vehicle-update"
    ),

    path(
        "<int:pk>/delete/",
        VehicleDeleteView.as_view(),
        name="vehicle-delete"
    ),

]