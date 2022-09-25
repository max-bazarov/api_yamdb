from rest_framework.routers import DefaultRouter

from api.views import CategoryViewSet


router = DefaultRouter()
router.register('categories', CategoryViewSet, basename='categorie')
