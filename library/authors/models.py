from django.db import models
from uuid import uuid4
# Create your models here.


class Author(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid4())
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    birthday_year = models.PositiveIntegerField()

    def __str__(self):
        return self.first_name
