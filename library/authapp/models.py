from django.db import models
from django.contrib.auth.models import AbstractUser
from uuid import uuid4

# Create your models here.

class LibUser(AbstractUser):
    uid = models.UUIDField(primary_key=True, default=uuid4(), null=False)
    avatar = models.ImageField(upload_to='users_avatars', blank=True)
    date_add = models.DateTimeField(auto_now_add=True)
    last_modify = models.DateTimeField(auto_now=True)

