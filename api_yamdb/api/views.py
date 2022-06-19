from django.shortcuts import get_object_or_404
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from rest_framework import filters, permissions, status, viewsets
from rest_framework.response import Response
from reviews.models import Category, Comment, Genre, Reviews, Titles, User
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import api_view, action, permission_classes
from django.db.models import Avg

from api.mixins import CreateLisDestroytViewSet
from api.permissions import (IsAdmin, IsAdminModeratorAuthorOrReadOnly,
                             IsAuthorOrReadOnly, ReadOnly)
from api.serializers import (CategorySerializer, CommentSerializer,
                             GenreSerializer, ReviewsSerializer,
                             TitlesSerializer, TokenSerializer, UserSerializer, UserEditionSerializer,
                             RegisterSerializer)
from rest_framework_simplejwt.tokens import RefreshToken

from api.filters import TitleFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework_simplejwt.tokens import AccessToken


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdmin,)
    filter_backends = (filters.SearchFilter,)
    filter_fields = ('username',)
    search_fields = ('username',)
    lookup_field = 'username'
    
    @action(methods=['get', 'patch'],
            detail=False,
            serializer_class=UserEditionSerializer,
            permission_classes=[permissions.IsAuthenticated],
            url_path='me')
    def user_update_profile(self, request):
        user = request.user
        if request.method == 'GET':
            serializer = UserEditionSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        elif request.method == 'PATCH':
            serializer = UserEditionSerializer(partial=True, data=request.data)
            serializer.is_valid()
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = PageNumberPagination
    permission_classes = (ReadOnly,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ['name', ]
    lookup_field = 'slug'

    def retrieve(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def update(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    pagination_class = PageNumberPagination
    permission_classes = (ReadOnly,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ['name', ]
    lookup_field = 'slug'

    def retrieve(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def update(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


class TitlesViewSet(viewsets.ModelViewSet):
    queryset = Titles.objects.all()
    serializer_class = TitlesSerializer
    permission_classes = (ReadOnly,)
    pagination_class = PageNumberPagination
    filter_class = TitleFilter
    filter_backends = (DjangoFilterBackend,)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (IsAdminModeratorAuthorOrReadOnly,)
    pagination_class = PageNumberPagination

    def get_queryset(self):
        review = get_object_or_404(Comment, id=self.kwargs.get('reviews_id'))
        return review.comments.all()

    def perform_create(self, serializer):
        review = get_object_or_404(Reviews, pk=self.kwargs.get('reviews_id'))
        serializer.save(author=self.request.user, review=review)


class ReviewsViewSet(viewsets.ModelViewSet):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsAdminModeratorAuthorOrReadOnly,)
    
    def get_queryset(self):
        title = get_object_or_404(Titles, id=self.kwargs.get('title_id'))
        return title.reviews.all()

    def perform_create(self, serializer):
        title = get_object_or_404(Titles, id=self.kwargs.get('title_id'))
        serializer.save(author=self.request.user, title=title)

@api_view(["POST"])
@permission_classes([permissions.AllowAny])
def create_user(request):
    serializer = RegisterSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    user = get_object_or_404(
        User,
        username=serializer.validated_data["username"]
    )
    confirmation_code = default_token_generator.make_token(user)
    send_mail(
        subject="YaMDb registration",
        message=f"Your confirmation code: {confirmation_code}",
        from_email=None,
        recipient_list=[user.email],
    )
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(["POST"])
@permission_classes([permissions.AllowAny])
def get_jwt_token(request):
    serializer = TokenSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = get_object_or_404(
        User,
        username=serializer.validated_data["username"]
    )
    if default_token_generator.check_token(
        user, serializer.validated_data["confirmation_code"]
    ):
        token = AccessToken.for_user(user)
        return Response({"token": str(token)}, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
