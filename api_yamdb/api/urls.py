from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api_yamdb.api.views import GenresViewSet, CommentViewSet, CategoryViewSet

router = DefaultRouter()
router.register('genres', GenresViewSet, basename='genre')
router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet, basename='comment'
)
router.register('categories', CategoryViewSet, basename='categorie')


urlpatterns = [
    path('v1/', include(router.urls)),
]
