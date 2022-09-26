from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api_yamdb.api.views import (
    CommentViewSet,
    CategoryViewSet,
    GenreViewSet,
    TitleViewSet,
    ReviewViewSet
)


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
]
