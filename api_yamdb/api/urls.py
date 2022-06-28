from django.urls import path, include
from rest_framework import routers

from .views import CommentViewSet, ReviewViewSet, UserViewSet, regist, get_jwt_token

router_v1 = routers.DefaultRouter()
router_v1.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet,
    basename='reviews',
)
router_v1.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet,
    basename='comments',
)
router_v1.register(r'users', UserViewSet, basename='users')

urlpatterns = [
    path('v1/auth/signup/', regist, name='regist'),
    path('v1/auth/token/', get_jwt_token, name='token'),
    path('v1/', include(router_v1.urls)),
]
