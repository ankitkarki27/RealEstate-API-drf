from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import PropertyViewSet  # Import PropertyViewSet

# Initialize DefaultRouter
router = DefaultRouter()
router.register(r'properties', PropertyViewSet, basename='properties')

# Define URL patterns with 'api/v1/'
urlpatterns = [
    path('api/v1/', include(router.urls)),
]
