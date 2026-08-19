from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class  registration(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,default=None)
    full_name=models.CharField(max_length=30)
    email=models.EmailField(unique=True)
    user_name=models.CharField(max_length=20)

    def __str__(self):
        return self.email
