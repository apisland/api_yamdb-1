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
                             TitlesSerializer, TokenSerializer, UserSerializer)

from api.filters import TitleFilter
from django_filters.rest_framework import DjangoFilterBackend

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = PageNumberPagination
    permission_classes = (IsAdminModeratorAuthorOrReadOnly,)
    filter_backends = (filters.SearchFilter,)
    filterset_fields = ('username')
    search_fields = ('username',)
    lookup_field = 'username'
    
    #  @action(
    #      methods=['get', 'patch'],
    #      detail=False
    #  )


class CategoryViewSet(CreateLisDestroytViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class GenreViewSet(CreateLisDestroytViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class TitlesViewSet(viewsets.ModelViewSet):
    queryset = Titles.objects.annotate(rating=Avg('reviews_score'))
    serializer_class = TitlesSerializer
    permission_classes = (IsAdmin, ReadOnly)
    pagination_class =PageNumberPagination
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
        new_queryset = title.reviews.all()
        return new_queryset

    def perform_create(self, serializer):
        title = get_object_or_404(Titles, id=self.kwargs.get('title_id'))
        serializer.save(author=self.request.user, title=title)