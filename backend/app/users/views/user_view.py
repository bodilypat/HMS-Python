#users/views/user_view.py

from rest_framework import viewsets, permissions
from app.users.models import User
from app.users.serializers.user_serializer import UserSerializer
from app.users.permissions.roles import IsAdminSelf
from rest_framework.response import Response

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    Admins can view/edit all users.
    Regular users can view/edit only their own data.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdminSelf]

    def get_permissions(self):
        """
        Assign permissions based on action.
        Admins have full access.
        Regular users can only access their own data.
        """
        if self.request.user.is_staff:
            return [permission() for permission in self.permission_classes]
        else:
            return [permissions.IsAuthenticated()]
        
    def get_queryset(self):
        """
        Restrict queryset based on user role.
        Admins see all users.
        Regular users see only their own data.
        """
        user = self.request.user
        if user.is_staff:
            return User.objects.all()
        return User.objects.filter(id=user.id)
    