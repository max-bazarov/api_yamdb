from rest_framework import viewsets

from api_yamdb.api.serializers import (CommentSerializer, GenreSerializer,
                                       ReviewSerializer)
from api_yamdb.reviews.models import Comment, Genre, Review


class GenresViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
