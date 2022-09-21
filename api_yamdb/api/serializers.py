from dataclasses import field
from rest_framework import serializers

from reviews.models import Categories

class CategoriesSerializers(serializers.ModelSerializer):

    class Meta:
        model = Categories
        field = '__all__'