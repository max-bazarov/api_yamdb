from django.core.mail import EmailMessage
from rest_framework import permissions, status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework.decorators import action
from django.contrib.auth.tokens import default_token_generator

from api.serializers import (CategorySerializer, GenreSerializer,
                             GetTokenSerializer, SignUpSerializer,
                             TitleSerializer)
from reviews.models import Category, Comment, Genre, Review, Title
from users.models import User

from .permissions import AuthorOrReadOnly
from .serializers import (CommentSerializer, GenreSerializer, ReviewSerializer,
                          UserSerializer)


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    lookup_field = 'username'

    def get_permissions(self):
        if self.action == 'get_user_me':
            return [permissions.IsAuthenticated()]
        return [permissions.IsAdminUser()]

    def get_queryset(self):
        queryset = User.objects.all()
        username = self.request.query_params.get('username')
        if username:
            queryset = queryset.filter(username=username)
        return queryset

    @action(detail=False, methods=['get', 'patch'], url_path='me')
    def get_user_me(self, request):
        user = User.objects.get(username=request.user)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [AuthorOrReadOnly]

    def perform_create(self, serializer):
        return serializer.save(author=self.request.user)


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [AuthorOrReadOnly]

    def perform_create(self, serializer):
        title = Title.objects.get(id=self.kwargs.get('title_id'))
        return serializer.save(author=self.request.user,
                               title=title)


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class APIGetToken(APIView):
    """
    Получение JWT-токена в обмен на username и confirmation code.
    Права доступа: Доступно без токена. Пример тела запроса:
    {
        "username": "string",
        "confirmation_code": "string"
    }
    """
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = GetTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        try:
            user = User.objects.get(username=data.get('username'))
        except User.DoesNotExist:
            return Response(
                {'username': 'Пользователь не найден!'},
                status=status.HTTP_404_NOT_FOUND)

        if data.get('confirmation_code') == user.confirmation_code:
            token = AccessToken.for_user(user)
            return Response({'token': str(token)},
                            status=status.HTTP_201_CREATED)
        return Response(
            {'confirmation_code': 'Неверный код подтверждения!'},
            status=status.HTTP_400_BAD_REQUEST)


class APISignup(APIView):
    """
    Получить код подтверждения на переданный email. Права доступа: Доступно без
    токена. Пример тела запроса:
    {
        "email": "string",
        "username": "string"
    }
    """
    permission_classes = [permissions.AllowAny]

    def send_email(self, data):
        email = EmailMessage(
            subject=data.get('email_subject'),
            body=data.get('email_body'),
            to=[data.get('to_email')]
        )
        email.send()

    def post(self, request):
        serializer = SignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        confirmation_code = default_token_generator.make_token(user)
        user.confirmation_code = confirmation_code
        user.save()
        email_body = (
            f'Здравствуйте, {user.username}.'
            f'\nКод подтверждения для доступа к API: {confirmation_code}'
        )
        data = {
            'email_body': email_body,
            'to_email': user.email,
            'email_subject': 'Код подтверждения для доступа к API!'
        }
        print(data)
        self.send_email(data)
        return Response(serializer.data, status=status.HTTP_200_OK)
