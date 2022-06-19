from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import create_user, get_jwt_token

from api.views import (
    CategoryViewSet,
    GenreViewSet,
    CommentViewSet,
    TitlesViewSet,
    UserViewSet,
    ReviewsViewSet,
)

app_name = 'api'

router = DefaultRouter()

router.register(r'users', UserViewSet, basename='users')
router.register(r'categories', CategoryViewSet, basename='categories')
router.register(r'titles', TitlesViewSet, basename='titles')
router.register(r'genres', GenreViewSet, basename='genres')
router.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewsViewSet,
    basename='reviews'
)
router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/auth/token/', get_jwt_token),
    path('v1/auth/signup/', create_user),
]