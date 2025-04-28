from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ListingViewSet
# from .views import ListingListCreateAPIView, ListingDetailAPIView
# ListingViewSet

router = DefaultRouter()
router.register(r'listings', ListingViewSet, basename='listing')

urlpatterns = [
    path('', include(router.urls)),
    # path('', ListingListCreateAPIView.as_view(), name='listing-list-create'),
    # path('<int:pk>/', ListingDetailAPIView.as_view(), name='listing-detail'),
]
