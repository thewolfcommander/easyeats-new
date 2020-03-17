import uuid

from django.db import models
from django.utils.text import Truncator
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser, BaseUserManager
from django.conf import settings




UPLOAD_DIRECTORY_PROFILEPHOTO = 'images_profilephoto'

class CustomUserManager(BaseUserManager):
    """
    Custom user manager to handle all the operations for the Custom User model
    """
    def create_user(self, user_id, email, password=None, **extra_fields):
        user = self.model(user_id=user_id, email=email, *extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, user_id, email, password, **extra_fields):
        user = self.create_user(user_id, email, password, **extra_fields)
        user.is_admin=True
        user.is_superuser = True
        user.save(using=self._db)
        return user

    def get_by_natural_key(self, username):
        return self.get(user_id=username)


class ResidentialPinCode(models.Model):
    """
    This model gonna hold the area details and pincodes where the service is currently operating
    """
    pincode = models.CharField(max_length=6, help_text="User's Residential pincode", default=246174)
    area = models.CharField(max_length=255, null=True)
    city = models.CharField(max_length=255, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('area',)
        verbose_name = 'Residential PIN Code'
        verbose_name_plural = 'Residential PIN Codes'
    
    def __str__(self):
        return self.area



class User(AbstractBaseUser, PermissionsMixin):
    """
    User that is capable of using the Information System
    """
    GENDER = [
        ('MALE', "MALE"),
        ('FEMALE', "FEMALE"),
        ('TRANSGENDER', "TRANSGENDER"),
        ('PREFER_NOT_TO_SAY', "PREFER_NOT_TO_SAY")
    ]
    user_id = models.CharField(max_length=24, null=True, unique=True, help_text="User's unique user id, keep it irrelated with respect to your name or email.", verbose_name='username')
    full_name = models.CharField(max_length=255, null=True, help_text="User's full name")
    gender = models.CharField(max_length=255, choices=GENDER, null=True, help_text="User's Gender")
    email = models.EmailField(max_length=255, null=True, default='', help_text="User's Email")
    mobile_number = models.CharField(max_length=10, null=True, help_text="User's Mobile number")
    profile_photo = models.ImageField(max_length=255, blank=True, null=True, upload_to=UPLOAD_DIRECTORY_PROFILEPHOTO, help_text="User's Profile photo")
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    order_count = models.IntegerField(default=0)

    is_admin = models.BooleanField(default=False)
    is_client = models.BooleanField(default=False)
    is_vendor = models.BooleanField(default=False)
    is_delivery = models.BooleanField(default=False)
    is_newsletter = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'user_id'
    REQUIRED_FIELDS= ['email',]
    UNIQUE_TOGETHER = ['user_id', 'email']

    def __str__(self):
        return '%s - %s'%(self.id, self.full_name)

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin



class Vendor(models.Model):
    """
    This model gonna hold the information about the vendor who is on the platform to sell the food
    """
    STATE_CHOICES = [
        ('uttarakhand', 'Uttarakhand'),
    ]
    COUNTRY_CHOICES = [
        ('india', 'India'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    business_phone = models.CharField(max_length=20, null=True)
    business_email = models.CharField(max_length=255, null=True)
    address1 = models.CharField(max_length=255, null=True)
    address2 = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True)
    landmark = models.CharField(max_length=255, null=True, blank=True)
    state = models.CharField(max_length=255, null=True, choices=STATE_CHOICES, default='uttarakhand')
    country = models.CharField(max_length=255, null=True, choices=COUNTRY_CHOICES, default='india')
    pincode = models.CharField(max_length=6, null=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('added',)
        verbose_name = 'Vendor'
        verbose_name_plural = 'Vendors'

    def __str__(self):
        return self.user.user_id



class DeliveryBoy(models.Model):
    """
    This model gonna hold the information about the delivery boys who are on the platform to deliver the food
    """
    STATE_CHOICES = [
        ('uttarakhand', 'Uttarakhand'),
    ]
    COUNTRY_CHOICES = [
        ('india', 'India'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    business_phone = models.CharField(max_length=20, null=True)
    business_email = models.CharField(max_length=255, null=True)
    address1 = models.CharField(max_length=255, null=True)
    address2 = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True)
    landmark = models.CharField(max_length=255, null=True, blank=True)
    state = models.CharField(max_length=255, null=True, choices=STATE_CHOICES, default='uttarakhand')
    country = models.CharField(max_length=255, null=True, choices=COUNTRY_CHOICES, default='india')
    pincode = models.CharField(max_length=6, null=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('added',)
        verbose_name = 'Delivery Boy'
        verbose_name_plural = 'Delivery Boys'

    def __str__(self):
        return self.user.user_id
