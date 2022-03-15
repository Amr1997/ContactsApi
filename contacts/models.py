from django.db import models
from django.conf import settings
# Create your models here.


class Contact(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL , on_delete=models.CASCADE)
    phone = models.IntegerField(max_length=15)
    country_code = models.IntegerField(max_length=8)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_fav = models.BooleanField(default=False)
