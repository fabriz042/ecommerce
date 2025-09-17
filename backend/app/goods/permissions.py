from utils.permissions_mixins import RoleActionPermissionMixin

class GoodsPermission(RoleActionPermissionMixin):
    ROLE_PERMISSIONS = {
        "anonymous": ["list", "retrieve"]
    }