# -*- coding: utf-8 -*-   CBV编写接口
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Person
import urllib3,urllib
import json
import wXData
from userInfo.serializers import userSerializer
from userInfo.models import Person
# Create your views here.
@csrf_exempt #防止攻击注入
def login(request):
    if request.method == 'POST':
        AppID = 'wxd7761fa4fa16ae3f'
        AppSecret = 'a7fad3a73fd8b8a39458357542428e30'
        req = json.loads(request.body)
        code  = req['code']
        userInfo = req['userInfo']

        if code:
            url = "https://api.weixin.qq.com/sns/jscode2session?appid="+AppID+"&secret="+AppSecret+"&js_code="+code+"&grant_type=authorization_code"
            try:
                http = urllib3.PoolManager()
                wxRequest = http.request('GET',url=url)
                if wxRequest.status==200 and wxRequest.data:
                    wxDatas = json.loads(wxRequest.data.decode())

                    # if Person.objects.filter(OpenID=wxDatas['openid']):
                    #     return JsonResponse({'code': 0})
                    # else:
                    if Person.objects.filter(OpenID=wxDatas['openid']):
                        return JsonResponse({'code': 0, 'OpenID': wxDatas['openid']})
                    userInfo['OpenID'] = wxDatas['openid']
                    print(userInfo)
                    user = userSerializer(data=userInfo)
                    if user.is_valid():
                        user.save()
                    else:
                        print(user.errors)
                        return JsonResponse({'code': 1,'msg':'数据保存时出错'})
                    return JsonResponse({'code': 0,'OpenID':wxDatas['openid']})

                            # pc = wXData.WXDataCrypt(AppID, wxDatas['session_key'])
                    # print(pc.decrypt(encryptedData, iv))
                    # return JsonResponse({'code': 0,'data':json.loads(wxRequest.data)})

            except BaseException:
                return JsonResponse({'code': 1})
                # return JsonResponse(json.loads(res))
        else:
            return JsonResponse({'code':1})
