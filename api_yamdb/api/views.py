from statistics import quantiles
from rest_framework import viewsets

from api_yamdb.api.serializers import CategorySerializer, GenreSerializer, TitleSerializer
from api_yamdb.reviews.models import Category, Genre, Title




class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class TitleViewSet(viewsets.ModelViewSet):
    queryset =Title.objects.all()
    serializer_class = TitleSerializer
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
