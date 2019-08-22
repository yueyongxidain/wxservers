
# -*- coding: utf-8 -*-

from rest_framework import serializers
from userInfo.models import Person
from django.core.serializers import serialize
class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields ='__all__'
