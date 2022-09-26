from .views import (CategoryViewSet, CommentViewSet, GenreViewSet,
                    ReviewViewSet, TitleViewSet, APIGetToken, APISignup)
from django.urls import include, path
from rest_framework.routers import DefaultRouter
# APIGetToken, APISignup,
app_name = 'api'

router = DefaultRouter()
router.register('genres', GenreViewSet, basename='genre')
router.register('title', TitleViewSet, basename='title')
router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet, basename='comment'
)
router.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet, basename='review'
)
router.register('categories', CategoryViewSet, basename='categorie')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/auth/token/', APIGetToken.as_view(), name='get_token'),
    path('v1/auth/signup/', APISignup.as_view(), name='signup'),
]
