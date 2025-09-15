from rest_framework.permissions import BasePermission

class RoleActionPermissionMixin(BasePermission):

    allow_admin = True

    def has_permission(self, request, view):
        role_name = getattr(request.user.role, "name", None)

        if self.allow_admin and role_name == "admin":
            return True

        allowed_actions = getattr(self, "ROLE_PERMISSIONS", {}).get(role_name, [])
        return view.action in allowed_actions
