from django.db import models

from accounts.models import User


class Address(models.Model):
    """
    This model is for handling of addresses all over the platform
    """
    STATE_CHOICES = [
        ('uttarakhand', 'Uttarakhand'),
    ]
    COUNTRY_CHOICES = [
        ('india', 'India'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=True)
    address1 = models.CharField(max_length=255, null=True)
    address2 = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True)
    state = models.CharField(max_length=255, null=True, choices=STATE_CHOICES)
    country = models.CharField(max_length=255, null=True, choices=COUNTRY_CHOICES)
    pincode = models.CharField(max_length=6, null=True)
    mobile_number = models.CharField(max_length=20, null=True)
    alt_mobile = models.CharField(max_length=20, null=True, blank=True)
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Address'
        verbose_name_plural = 'Addresses'

    def __str__(self):
        return self.user.user_id

    def get_short_address(self):
        for_name = self.name
        return "{for_name} {line1}, {city}".format(
                for_name = for_name or "",
                line1 = self.address1,
                city = self.city
            ) 

    def get_address(self):
        return "{for_name}\n{line1}\n{line2}\n{city}\n{state}, {postal}\n{country}".format(
                for_name = self.name or "",
                line1 = self.address1,
                line2 = self.address2 or "",
                city = self.city,
                state = self.state,
                postal= self.pincode,
                country = self.country
            )