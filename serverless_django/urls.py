from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from users.views import TokenObtainPairPatchedView
from rest_framework_simplejwt import views as jwt_views
from users.views import *
from users.routers import users_router


urlpatterns = [
    path('admin/', admin.site.urls),

    path(r'api/', include(users_router.urls)),

    # JWT authentication
    path('api/token/', TokenObtainPairPatchedView.as_view()),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

]
