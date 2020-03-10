from django.db import models
from private_storage.fields import PrivateFileField


class PrivateFile(models.Model):
    title = models.CharField("Title", max_length=200)
    file = PrivateFileField("File")


class PrivateFile2(models.Model):
    title = models.CharField("Title", max_length=200)
    file = models.FileField("File")
