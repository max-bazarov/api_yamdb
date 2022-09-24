from rest_framework import serializers
from reviews.models import Genre


class GenreSerializer(serializers.ModelSerializers):
    class Meta:
        model = Genre
        fields = '__all__'
