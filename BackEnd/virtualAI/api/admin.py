from django.contrib import admin
from api import models

# Register your models here.

admin.site.register(models.CustomUser)
admin.site.register(models.BookMark)
admin.site.register(models.Url)
