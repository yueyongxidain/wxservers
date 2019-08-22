# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Person(models.Model):
    OpenID = models.CharField(primary_key=True,default='',max_length=30)
    nickName = models.CharField(default='',max_length=30,null=True)
    phonenumber = models.CharField(default='',max_length=30,null=True)
    gender = models.IntegerField(default=1,null=True)
    language = models.CharField(default='',max_length=100,null=True)
    country = models.CharField(default='',max_length=30,null=True)
    city = models.CharField(default='',max_length=30,null=True)
    avatarUrl = models.CharField(default='',max_length=200,null=True)
    def __str__(self):
        return self.name