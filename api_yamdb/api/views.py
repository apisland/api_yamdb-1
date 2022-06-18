from django.shortcuts import get_object_or_404
from rest_framework import filters, permissions, status, viewsets
from rest_framework.response import Response
from reviews.models import Category, Comment, Genre, Reviews, Titles, User
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import api_view, action
from django.db.models import Avg

from api.mixins import CreateLisDestroytViewSet
from api.permissions import (IsAdmin, IsAdminModeratorAuthorOrReadOnly,
                             IsAuthorOrReadOnly, ReadOnly)
from api.serializers import (CategorySerializer, CommentSerializer,
                             GenreSerializer, ReviewsSerializer,
                             TitlesSerializer, TokenSerializer, UserSerializer, UserEditionSerializer)

from api.filters import TitleFilter
from django_filters.rest_framework import DjangoFilterBackend


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = PageNumberPagination
    permission_classes = (IsAdminModeratorAuthorOrReadOnly,)
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


class CategoryViewSet(CreateLisDestroytViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAdmin, ReadOnly,)


class GenreViewSet(CreateLisDestroytViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = (IsAdmin, ReadOnly,)


class TitlesViewSet(viewsets.ModelViewSet):
    queryset = Titles.objects.all().annotate(Avg('reviews__score'))
    serializer_class = TitlesSerializer
    permission_classes = (IsAdmin, ReadOnly)
    pagination_class = PageNumberPagination
    filter_class = TitleFilter
    filter_backends = (DjangoFilterBackend,)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (IsAdminModeratorAuthorOrReadOnly,)

    def get_queryset(self):
        review = get_object_or_404(Comment, id=self.kwargs.get('reviews_id'))
        return review.comments.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class ReviewsViewSet(viewsets.ModelViewSet):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer
    
    def get_queryset(self):
        title = get_object_or_404(Titles, id=self.kwargs.get('title_id'))
        return title.reviews.all()

    def perform_create(self, serializer):
        title = get_object_or_404(Titles, id=self.kwargs.get('title_id'))
        serializer.save(author=self.request.user, title=title)


class RegisterViewSet(viewsets.ModelViewSet):
    pass


class GetTokenViewSet(viewsets.ModelViewSet):
    pass
