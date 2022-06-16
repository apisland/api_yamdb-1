from django.shortcuts import get_object_or_404
from rest_framework import filters, permissions, viewsets
from reviews.models import Category, Comment, Genre, Reviews, Titles, User
from api.mixins import GetListViewSet
from rest_framework.mixins import CreateModelMixin
from api.serializers import (CategorySerializer, CommentSerializer,
                             GenreSerializer, ReviewsSerializer,
                             TitlesSerializer, UserSerializer, TokenSerializer)
from rest_framework.response import Response
from rest_framework import status

class RegisеterViewSet(CreateModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CategoryViewSet(GetListViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class TitlesViewSet(viewsets.ModelViewSet):
    queryset = Titles.objects.all()
    serializer_class = TitlesSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self):
        review = get_object_or_404(Comment, id=self.kwargs.get('reviews_id'))
        return review.comments.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class ReviewsViewSet(viewsets.ModelViewSet):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer
