
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    # path("api/v1/", include("api.urls")),
    
     # JWT Authentication URLs (under api/v/)
    path('api/v/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'), 
    path('api/v/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    
    # Listings App APIs
    path('api/v/', include('listing.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

