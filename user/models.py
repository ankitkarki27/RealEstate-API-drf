from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin

# Manager for UserAccount model
class UserAccountManager(BaseUserManager):
    def create_user(self, email, full_name, password=None,role='user'):
        if not email:
            raise ValueError("Users must have an email address")
        
        email = self.normalize_email(email)  # normalize email to lowercase
        email = email.lower()

        user = self.model(
            email=email,
            full_name=full_name,
            role=role
        )
        
        user.set_password(password)  # This will hash the password
        user.save(using=self._db)  # Save the user to the database
        return user

    def create_realtor(self, email, full_name, password=None):
        user = self.create_user(email, full_name, password)
        user.role = 'realtor'  # Assign role 'realtor'
        user.save(using=self._db)
        return user

    def create_superuser(self, email, full_name, password=None):
        user = self.create_user(email, full_name, password)
        user.is_staff = True
        user.is_superuser = True
        user.role = 'admin'  # Assign role 'admin'
        user.save(using=self._db)  # Save the user to the database
        return user


# UserAccount Model
class UserAccount(AbstractUser, PermissionsMixin):
    # Role choices for user type
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('realtor', 'Realtor'),
        ('user', 'User'),
    ]
    
    email = models.EmailField(unique=True, max_length=255)
    full_name = models.CharField(max_length=255, default="Anonymous")
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=True) 
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # New role field
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')  # Role field added
    
    # Custom manager for handling user creation
    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name']  # Change from name to full_name
    username = None  # Disable username field
    
    def __str__(self):
        return self.email
