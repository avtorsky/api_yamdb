from django.urls import path, include
from rest_framework import routers

from .views import UserViewSet, regist, get_jwt_token
router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename='users')


urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/auth/signup/', regist, name='regist'),
    path('v1/auth/token/', get_jwt_token, name='token')
]
