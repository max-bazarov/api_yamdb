from api.views import (APIGetToken, APISignup, CategoryViewSet, CommentViewSet,
                       GenreViewSet, ReviewViewSet, TitleViewSet, UserViewSet)
from django.urls import include, path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('genres', GenreViewSet, basename='genre')
router.register('titles', TitleViewSet, basename='title')
router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet, basename='comment'
)
router.register('categories', CategoryViewSet, basename='category')
router.register('users', UserViewSet, basename='user')
router.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet,
    basename='reviews'
)

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/auth/token/', APIGetToken.as_view(), name='get_token'),
    path('v1/auth/signup/', APISignup.as_view(), name='signup'),
]
