from rest_framework import serializers
from reviews.models import Genres


class GenresSerializers(serializers.ModelSerializers):
    class Meta:
        model = Genres
        fields = "__all__"
