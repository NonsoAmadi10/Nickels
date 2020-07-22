from rest_framework.permissions import BasePermission


class IsOwnerOrReadOnly(BasePermission):
    message = 'You must be the owner of this object.'
    my_safe_method = ['GET', 'PUT', 'OPTIONS', 'HEAD', 'PATCH']

    def has_permission(self, request, view):
        if request.method in self.my_safe_method:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        #member = Membership.objects.get(user=request.user)
        # member.is_active
        if request.method in self.my_safe_method:
            return True
        return obj.user == request.user
