from django.urls import path, include
from rest_framework import routers

from .views import (
    CategoryViewSet,
    CommentViewSet,
    GenreViewSet,
    get_jwt_token,
    regist,
    ReviewViewSet,
    TitleViewSet,
    UserViewSet
)

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
router_v1.register(r'genres', GenreViewSet)
router_v1.register(r'categories', CategoryViewSet)
router_v1.register(r'titles', TitleViewSet)


urlpatterns = [
    path('v1/auth/signup/', regist, name='regist'),
    path('v1/auth/token/', get_jwt_token, name='token'),
    path('v1/', include(router_v1.urls)),
]
