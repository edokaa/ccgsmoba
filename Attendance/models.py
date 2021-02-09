from django.db import models
from gdstorage.storage import GoogleDriveStorage

# Create your models here.

gd_storage = GoogleDriveStorage()


class Town(models.Model):
    town_name = models.CharField(max_length=50)

    def __str__(self):
        return self.town_name


class Mass(models.Model):
    mass_name = models.CharField(max_length=50)
    mass_time = models.TimeField()

    def __str__(self):
        return self.mass_name


class Member(models.Model):
    member_name = models.CharField(max_length=50)
    member_phone_no = models.CharField(max_length=12, blank=True, default='-')
    member_address = models.ForeignKey(Town, on_delete=models.CASCADE)

    def __str__(self):
        return self.member_name


class This_Sunday_Member(models.Model):
    member_name = models.OneToOneField(Member, on_delete=models.CASCADE)
    member_phone_no = models.CharField(max_length=12)
    member_address = models.ForeignKey(Town, on_delete=models.CASCADE)
    mass_attended = models.ForeignKey(Mass, on_delete=models.CASCADE)

    def __str__(self):
        return self.member_name.member_name


class LogsFile(models.Model):
    adminupload = models.FileField(upload_to='media/log/', storage=gd_storage)
    title = models.CharField(max_length=50)
    total_members = models.IntegerField(default=0)

    def __str__(self):
        return self.title