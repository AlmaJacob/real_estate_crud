from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class estate(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    price = models.IntegerField(null=True, blank=True)
    description = models.TextField(default=None, blank=True, null=True)
    phone_no = models.CharField(max_length=15, unique=True, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    estate = models.ForeignKey(estate, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['user', 'estate']