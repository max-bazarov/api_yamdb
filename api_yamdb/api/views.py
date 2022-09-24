from rest_framework import viewsets
from reviews.models import Categorie

from api.serializers import CategorieSerializer


class CategorieViewSet(viewsets.ModelViewSet):
    queryset = Categorie.objects.all()
    serializer_class = CategorieSerializer
