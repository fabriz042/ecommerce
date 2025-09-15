from utils.permissions_mixins import RoleActionPermissionMixin

class ProductPermission(RoleActionPermissionMixin):
    ROLE_PERMISSIONS = {
        "tester": ["create"], #Example
    }

    def has_permission(self, request, view):
        # Public read
        if view.action in ["list", "retrieve"]:
            return True

        return super().has_permission(request, view)
