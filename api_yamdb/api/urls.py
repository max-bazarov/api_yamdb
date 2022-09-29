from api.views import (APIGetToken, APISignup, CategoryViewSet, CommentViewSet,
                       GenreViewSet, ReviewViewSet, TitleViewSet)
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import (CategoryViewSet, CommentViewSet, GenreViewSet,
                       ReviewViewSet, TitleViewSet, APIGetToken, APISignup)

app_name = 'api'

router = DefaultRouter()
router.register('genres', GenreViewSet, basename='genre')
router.register('titles', TitleViewSet, basename='title')
router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet, basename='comment'
)
router.register('categories', CategoryViewSet, basename='category')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/auth/token/', APIGetToken.as_view(), name='get_token'),
    path('v1/auth/signup/', APISignup.as_view(), name='signup'),
]
