from django.shortcuts import render
from rest_framework import viewsets
from reviews.models import Categories, Genres
from api.serializers import CategoriesSerializers

class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializers
