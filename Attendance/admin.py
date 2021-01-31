from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.Mass)
admin.site.register(models.Member)
admin.site.register(models.Town)
admin.site.register(models.This_Sunday_Member)
admin.site.register(models.LogsFile)