from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from api.views import (
    CategoryViewSet,
    GenreViewSet,
    CommentViewSet,
    TitlesViewSet,
    UserViewSet,
    ReviewsViewSet,
    RegisterViewSet,
    GetTokenViewSet
)

app_name = 'api'

router = DefaultRouter()

router.register('users', UserViewSet, basename='users')
router.register('categories', CategoryViewSet, basename='categories')
router.register('titles', TitlesViewSet, basename='titles')
router.register('genres', GenreViewSet, basename='genres')
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
    path('v1/auth/token', GetTokenViewSet.as_view),
    path('v1/auth/signup', RegisterViewSet.as_view),
]