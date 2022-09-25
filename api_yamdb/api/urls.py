from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api_yamdb.api.views import GenreViewSet, TitleViewSet

router = DefaultRouter()
router.register('genres', GenreViewSet, basename='genre')
router.register('title', TitleViewSet, basename='title')

urlpatterns = [
    path('v1/', include(router.urls)),
]
