from rest_framework import viewsets

from api_yamdb.api.serializers import CategorySerializer, GenreSerializer
from api_yamdb.reviews.models import Category, Genre


class GenresViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
