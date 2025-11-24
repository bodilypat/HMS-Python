#users/views/auth_view.py

from rest_framework import generics, status, permissions
from rest_framework.response import Response
from app.users.serializers.register_serializer import RegisterSerializer
from app.users.serializers.user_serializer import UserSerializer
from app.users.models import User
from django.contrib.auth import authenticate


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "message": "User registered successfully."
        }, status=status.HTTP_201_CREATED)
    
class LoginView(generics.GenericAPIView):

    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            return Response({
                "user": UserSerializer(user).data,
                "message": "Login successful."
            }, status=status.HTTP_200_OK)
        return Response({
            "error": "Invalid credentials."
        }, status=status.HTTP_401_UNAUTHORIZED)
    
    