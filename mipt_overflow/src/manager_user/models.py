# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    photo = models.FileField(null=True, upload_to='photos')

class File(models.Model):
    name = models.CharField( max_length=32, default='unnamed_file' )
    mime = models.CharField( max_length=72 )
    key = models.CharField( max_length=72 )
    content = models.FileField( null=True, upload_to='files' )
    owners = models.ManyToManyField( User, related_name='files' )