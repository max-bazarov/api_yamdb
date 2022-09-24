from rest_framework import viewsets

from api_yamdb.api.serializers import GenreSerializer
from api_yamdb.reviews.models import Genre


class GenresViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
