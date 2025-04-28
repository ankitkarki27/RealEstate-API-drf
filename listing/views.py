from django.shortcuts import render
from .models import Listing
from .serializers import ListingSerializer
from rest_framework import viewsets, permissions
from .permissions import IsRealtorOrReadOnly
from rest_framework.filters import SearchFilter
from rest_framework.exceptions import PermissionDenied

# Create your views here.

class ListingViewSet(viewsets.ModelViewSet):
    queryset=Listing.objects.all()
    
    serializer_class=ListingSerializer
    filter_backends = (SearchFilter,)
    search_fields = ['property_type', 'sales_type', 'price']
    permission_classes = [IsRealtorOrReadOnly]
    
    def get_queryset(self):
        queryset=Listing.objects.all()
        is_active=self.request.query_params.get('is_active', None)
        if is_active is not None:
            queryset=queryset.filter(is_active=is_active)
        return queryset
    
    def perform_create(self, serializer):
            serializer.save(realtor=self.request.user)
            
    def perform_update(self, serializer):
            instance=self.get_object()
            if instance.realtor != self.request.user:
                raise PermissionDenied("You do not have permission to update this listing.")
            serializer.save()
            
    def perform_destroy(self, instance):
            if instance.realtor != self.request.user:
                raise PermissionDenied("You do not have permission to delete this listing.")
            instance.delete()
    
   
      