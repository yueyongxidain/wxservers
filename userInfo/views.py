# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Person
import urllib,urllib2
# Create your views here.
@csrf_exempt #屏蔽装饰器器
def login(request):
    if request.method == 'POST':
        AppID = 'wxd7761fa4fa16ae3f'
        AppSecret = 'a7fad3a73fd8b8a39458357542428e30'
        req = json.loads(request.body)
        code  = req['code']
        print code
        if code:
            url = "https://api.weixin.qq.com/sns/jscode2session?appid="+AppID+"&secret="+AppSecret+"&js_code="+code+"&grant_type=authorization_code"
            wxRequest = urllib2.Request(url=url)   
            res_data = urllib2.urlopen(wxRequest)
            res = res_data.read()
            return JsonResponse(json.loads(res))
        else:
            return JsonResponse({'code':0})
