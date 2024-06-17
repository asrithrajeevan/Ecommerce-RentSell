from django.db import models

# Create your models here.
class Products(models.Model):
    LIVE = 1
    DELETE = 0
    DELETE_CHOICES = ((LIVE, 'Live'), (DELETE ,'Delete'))
    title  = models.CharField(max_length=200)
    price  = models.FloatField(max_length=200)
    image  = models.ImageField(upload_to='media/')
    description  = models.TextField(max_length=200)
    priority = models.IntegerField(default=0) # to display product based on priority
    delete_status = models.IntegerField(choices = DELETE_CHOICES, default=LIVE) # for trash functionality
    created_at = models.DateTimeField(auto_now_add=True) # auto matically add created date of a product when a product adding
    updated_at = models.DateTimeField(auto_now=True) # when a change came in this product modal, at that time will store this updated_at field
    category = models.CharField(max_length=200, null=True)

    def __str__(self) -> str:
        return self.title