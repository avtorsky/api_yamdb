from django.urls import path, include
from rest_framework import routers

from .views import regist, get_jwt_token
router = routers.DefaultRouter()


urlpatterns = [
    path('v1/auth/signup/', regist, name='regist'),
    path('v1/auth/token/', get_jwt_token, name='token')

]
