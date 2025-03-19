from django.db import models
from django.contrib.auth.models import User

# property models but havent migrated
# class Property(models.Model):
#     PROPERTY_TYPE_CHOICES = [
#         ("house", "House"),
#         ("apartment", "Apartment"),
#         ("land", "Land"),
#         ("commercial", "Commercial"),
#     ]

#     PROPERTY_STATUS_CHOICES = [
#         ("available", "Available"),
#         ("sold", "Sold"),
#         ("rented", "Rented"),
#     ]

#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="properties")
#     title = models.CharField(max_length=255)
#     description = models.TextField()  # Kept as per your request
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     property_type = models.CharField(max_length=10, choices=PROPERTY_TYPE_CHOICES, default="house")
#     status = models.CharField(max_length=10, choices=PROPERTY_STATUS_CHOICES, default="available")
#     address = models.CharField(max_length=255)
#     city = models.CharField(max_length=100)
#     state = models.CharField(max_length=100)
#     zipcode = models.CharField(max_length=10)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.title

#     class Meta:
#         db_table = "property"
#         verbose_name_plural = "Properties"