#app/users/routers/users_router.py

from rest_framework import serializers
from app.users.views.user_view import User
from app.users.auth_view import Register, Login
from django.utls import path, include 

router = DefaultRouter()
router.register(r'register', Register, basename='register')

urlpatterns = [ 
    path("auth/regiter/", Register.as_view(), name="register"),
    path("auth/login/", Login.as_view(), name="login"),
    path("", include(router.urls)),
]


