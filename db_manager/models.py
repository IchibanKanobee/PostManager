from django.contrib.postgres.fields import ArrayField
from django.db import models
import os

class Post(models.Model):
    account = models.ForeignKey(
        "Account",
        on_delete=models.CASCADE,
    )
    record = models.ForeignKey(
        "Record",
        on_delete=models.CASCADE,
    )
    annotation = models.TextField(blank=True)
    creation_date = models.DateTimeField(blank=True) 
    platform_specific_reference = models.CharField(blank=True)


class RecordType(models.Model):
    type = models.CharField(unique=True)


class Platform(models.Model):
    name = models.CharField(unique=True)


class Record(models.Model):
    tags = ArrayField(models.CharField(max_length=100), blank=True)
    file_name = models.CharField(blank=True)
    creation_date = models.DateTimeField(auto_now_add=True, blank=True) 
    type = models.ForeignKey(
        "RecordType",
        on_delete=models.CASCADE,
    )
    source_platform = models.ForeignKey(
         "Platform",
         on_delete=models.CASCADE,
         default = 2,
    )
    author = models.CharField(blank=True)
    url = models.URLField(blank=True)
    edited = models.BooleanField(default=False)
    

class Account(models.Model):
    platform = models.ForeignKey(
        "Platform",
        on_delete=models.CASCADE,
    )
    name = models.CharField()
    suffix = models.CharField(blank=True)
    creation_date = models.DateField() 
    email = models.CharField(blank=True)
