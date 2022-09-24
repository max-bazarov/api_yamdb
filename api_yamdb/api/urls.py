from rest_framework.routers import DefaultRouter

from api.views import CategorieViewSet


router = DefaultRouter()
router.register('categories', CategorieViewSet, basename='categorie')
