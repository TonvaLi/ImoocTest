from django.shortcuts import render

# Create your views here.

import json
from django.http.response import HttpResponse
from django.shortcuts import render_to_response

def Login(request):
    #if request.method == 'POST':
    if request.method == 'POST':
        result = {}
        # username = request.POST.get('username')
        username = request.POST.get('username')
        mobile = request.POST.get('mobile')
        # data = request.POST.get('data')
        result['user'] = username
        result['mobile'] = mobile
        # result['data'] = data
        # result转换为json
        result = json.dumps(result)
        # return HttpResponse(username)
        return HttpResponse(result, content_type='application/json;charset=utf-8')
    else:
        return render_to_response('login.html')