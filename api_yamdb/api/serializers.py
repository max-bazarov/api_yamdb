from rest_framework import serializers
from reviews.models import Genre, Title


class GenreSerializer(serializers.ModelSerializers):
    class Meta:
        model = Genre
        fields = '__all__'

class TitleSerializer(serializers.ModelSerializer):
    categorie = serializers.SlugRelatedField(
        slug_field='slug',
        many = False,
    )
    genre = serializers.SlugRelatedField(
        slug_field='slug',
        many = True,
        required = False,
        
    )
    class Meta:
        model = Title
        fields = '__all__'