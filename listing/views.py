from django.shortcuts import render
from .models import Listing
from .serializers import ListingSerializer
from rest_framework import viewsets, permissions
from .permissions import IsRealtorOrReadOnly

# Create your views here.

class ListingViewSet(viewsets.ModelViewSet):
   queryset=Listing.objects.all()
   
   serializer_class=ListingSerializer
#    permission_classes=[permissions.IsAuthenticated]
   permission_classes = [IsRealtorOrReadOnly]
   
   def get_queryset(self):
       queryset=Listing.objects.all()
       is_active=self.request.query_params.get('is_active', None)
       if is_active is not None:
           queryset=queryset.filter(is_active=is_active)
       return queryset
   
      