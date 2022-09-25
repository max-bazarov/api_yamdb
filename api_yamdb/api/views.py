from rest_framework import viewsets

from api_yamdb.api.serializers import GenreSerializer, CommentSerializer
from api_yamdb.reviews.models import Genre, Comment


class GenresViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
