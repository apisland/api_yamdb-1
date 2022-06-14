from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
<<<<<<< HEAD



router = DefaultRouter()
#router.register('auth/signup', AuthViewset, basename='auth')
#router.register('auth/token', TokenViewset, basename='tokenauth')
#router.register('categories', CategoriesVitewSet, basename='categories')
#router.register('genres', GenreViewSet, basename='genre')
#router.register(
#    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments/(?P<comment_id>\d+)',
#                TitleViewSet, basename='comments'
#)
#router.register('users', UserViewSet, basename='users')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
=======
>>>>>>> categories
