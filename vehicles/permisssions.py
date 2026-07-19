from rest_framework.permissions import BasePermission, SAFE_METHODS


class ReadOnlyOrAuthenticated(BasePermission):
    """
    Anyone can read.
    Authentication required for write operations.
    """

    def has_permission(self, request, view):

        if request.method in SAFE_METHODS:
            return True

        return request.user and request.user.is_authenticated


class IsAdminInventoryManager(BasePermission):
    """
    Only staff/admin users can manage inventory.
    """

    def has_permission(self, request, view):

        return (
            request.user
            and request.user.is_authenticated
            and request.user.is_staff
        )


class CanPurchaseVehicle(BasePermission):
    """
    Any authenticated user can purchase a vehicle.
    """

    def has_permission(self, request, view):

        return (
            request.user
            and request.user.is_authenticated
        )