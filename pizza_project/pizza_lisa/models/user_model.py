from django.db import models
from django.contrib.auth.models import AbstractUser

    

class User(AbstractUser):
    phone_number = models.BigIntegerField(null=False)
    first_name = models.CharField (null = False)
    discont = models.IntegerField (default = 0 )
    total_shopping = models.FloatField(default = 0)
    def __str__(self):
        return self.first_name
    