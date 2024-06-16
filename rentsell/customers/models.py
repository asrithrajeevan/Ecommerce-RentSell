from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    LIVE = 1
    DELETE = 0
    DELETE_CHOICES = ((LIVE, 'Live'), (DELETE ,'Delete'))
    delete_status = models.IntegerField(choices = DELETE_CHOICES, default=LIVE)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customer')
    name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True) # auto matically add created date of a product when a product adding
    updated_at = models.DateTimeField(auto_now=True) # when a change came in this product modal, at that time will store this updated_at field
    def __str__(self) -> str:
        return self.name