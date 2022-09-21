from rest_framework import viewsets

from api_yamdb.api.serializers import GenresSerializers
from api_yamdb.reviews.models import Genres


class GenresViewSet(viewsets.ModelViewSet):
    queryset = Genres.objects.all()
    serializer_class = GenresSerializers
