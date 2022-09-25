from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api_yamdb.api.views import GenresViewSet

router = DefaultRouter()
router.register('genres', GenresViewSet, basename='genre')

urlpatterns = [
    path('v1/', include(router.urls)),
]
