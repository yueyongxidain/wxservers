# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Person(models.Model):
    username = models.CharField(max_length=30)
    age = models.IntegerField()
    def __str__(self):
        return self.name