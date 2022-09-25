from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api_yamdb.api.views import GenreViewSet

router = DefaultRouter()
router.register('genres', GenreViewSet, basename='genre')

urlpatterns = [
    path('v1/', include(router.urls)),
]
