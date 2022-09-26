from rest_framework import viewsets

from .serializers import (CommentSerializer, GenreSerializer,
                                       ReviewSerializer)
from api_yamdb.api.serializers import (
    CategorySerializer,
    GenreSerializer,
    TitleSerializer
)
from api_yamdb.reviews.models import Category, Genre, Title, Comment, Review


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
