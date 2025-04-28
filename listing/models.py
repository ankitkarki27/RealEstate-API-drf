from django.db import models
from user.models import UserAccount
# Create your models here.

class Listing(models.Model):
    class SaleType(models.TextChoices):
     FOR_SALE= 'For Sale'
     FOR_RENT= 'For Rent'
     FOR_LEASE= 'For Lease'
     
    class PropertyType(models.TextChoices):
     APARTMENT= 'Apartment'
     HOUSE= 'House'
     LAND= 'Land'
     COMMERCIAL= 'Commercial'
     INDUSTRIAL= 'Industrial'
     RETAIL= 'Retail'
     OFFICE= 'Office'
     WAREHOUSE= 'Warehouse'
     HOTEL= 'Hotel'
     VILLA= 'Villa'
     
    realtor = models.ForeignKey(
        UserAccount,
        on_delete=models.CASCADE,
        limit_choices_to={'role': 'realtor'}
    )
    
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    address = models.CharField(max_length=255)
    bedrooms = models.IntegerField()
    bathrooms = models.DecimalField(max_digits=4,decimal_places=1)
    
    sales_type = models.CharField(
        max_length=20,
        choices=SaleType.choices,
        default=SaleType.FOR_SALE
    )
    
    property_type = models.CharField(
        max_length=20,
        choices=PropertyType.choices,
        default=PropertyType.APARTMENT
    )
    
    photo_main=models.ImageField(upload_to='listing_photos/%Y/%m/%d/')
    photo_1=models.ImageField(upload_to='listing_photos/%Y/%m/%d/', blank=True, null=True)
    photo_2=models.ImageField(upload_to='listing_photos/%Y/%m/%d/', blank=True, null=True)
    photo_3=models.ImageField(upload_to='listing_photos/%Y/%m/%d/', blank=True, null=True)
    
    is_published = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def delete(self, *args, **kwargs):
        # Delete the photo file from the filesystem
        if self.photo_main:
            self.photo_main.delete(save=False)
        if self.photo_1:
            self.photo_1.delete(save=False)
        if self.photo_2:
            self.photo_2.delete(save=False)
        if self.photo_3:
            self.photo_3.delete(save=False)
        super().delete(*args, **kwargs)
        
    def __str__(self):
        return self.title