#app/users/serializers/user_serializer.py

from rest_framework import serializers
from app.users.models.user import User
from app.common.serializers.base_serializer import BaseSerializer

class UserSerializer(BaseSerializer):
    full_name = serializers.ReadOnlyField()
    class Meta:
        model = User
        fields = [
            'id',
            'email',
            'full_name',
            'role',
            'is_active',
            'is_staff',
            'date_created',
            'date_updated',
        ]
        read_only_fields = [
            'id',
            'is_staff',
            'date_created',
            'date_updated',
            'full_name',
        ]

        
