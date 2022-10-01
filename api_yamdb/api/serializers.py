from rest_framework import serializers
from reviews.models import Category, Comment, Genre, Review, Title
from users.models import User


class GetTokenSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        required=True)
    confirmation_code = serializers.CharField(
        required=True)

    class Meta:
        model = User
        fields = (
            'username',
            'confirmation_code'
        )


class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'username')

    def validate_username(self, value):
        if value == 'me':
            raise serializers.ValidationError(
                'Недопустимое имя пользователя')
        return value


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        exclude = ('id', )


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ('id', )


class TitleSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=False)
    genre = GenreSerializer(many=True)
    rating = serializers.SerializerMethodField()

    def get_rating(self, obj):
        reviews = Review.objects.filter(title=obj)
        if reviews.count() == 0:
            return None
        return round(
            sum([review.score for review in reviews]) / reviews.count(),
            1
        )

    class Meta:
        model = Title
        fields = '__all__'


class TitleCreateSerializer(serializers.ModelSerializer):
    genre = serializers.SlugRelatedField(
        slug_field='slug',
        many=True,
        queryset=Genre.objects.all()
    )
    category = serializers.SlugRelatedField(
        slug_field='slug',
        many=False,
        queryset=Category.objects.all(),
    )
    description = serializers.CharField(required=False)

    class Meta:
        model = Title
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True,
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Comment
        fields = ('id', 'text', 'author', 'pub_date')


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True,
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Review
        fields = ('id', 'text', 'author', 'score', 'pub_date')


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username',
                  'role',
                  'bio',
                  'email',
                  'first_name',
                  'last_name')

    def validate_username(self, value):
        if value == 'me':
            raise serializers.ValidationError(
                'Недопустимое имя пользователя')
        return value
