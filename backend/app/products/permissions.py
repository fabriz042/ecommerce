from utils.permissions_mixins import RoleActionPermissionMixin

class ProductPermission(RoleActionPermissionMixin):
    ROLE_PERMISSIONS = {
        "tester": ["create"],
        "anonymous": ["list", "retrieve"]
    }