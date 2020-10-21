from rest_framework import routers
from .views import *


users_router = routers.DefaultRouter()
#device_router.register(r'login', LoginViewSet, basename="login")
users_router.register(r'v1/users', UserViewSet)
users_router.register(r'v1/subject', SubjectViewSet)