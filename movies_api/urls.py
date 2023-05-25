from movies_api.views import MovieViewSet
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'movies', MovieViewSet, basename='movie')

urlpatterns = []
urlpatterns += router.urls
