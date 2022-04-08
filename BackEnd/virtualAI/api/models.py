from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    '''Custom User Model'''
    id=models.UUIDField(primary_key=True, default=uuid.uuid4)
    # prfile_image = models.ImageField()
    date_of_birth = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=200, blank=True)
    
    def __str__(self):
        return self.username


class Url(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    link = models.CharField(max_length=300)
    private = models.BooleanField(default=False)

    def __str__(self):
        return self.link


class BookMark(models.Model):
    '''URL Links'''
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.ForeignKey(CustomUser, on_delete=models.RESTRICT)
    url = models.ForeignKey(Url, on_delete=models.RESTRICT)

    def __str__(self):
        return f'{self.user}-{self.url}'