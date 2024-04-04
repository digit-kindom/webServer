import json

from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse, HttpResponse
from device import models
from django.http import JsonResponse

def index(request):  # 网页直接访问，helloworld
    if request.method == 'GET':
        return JsonResponse('Hello world', safe=False)
    else:
     return JsonResponse('world is left')

def id_create(request):
    if request.method == 'POST':
        data=eval(request.body)
        Id = data['id']
        if Id is not None:
         data = {
             "status": True,
             "msg": "string",
             "id": Id,
            }
         return HttpResponse(json.dumps(data))
        else:
            error_data={
                "status": False,
                "msg": "string",
                "id":None,
            }
            return HttpResponse(json.dumps(error_data))
    elif request.method=='GET':
        return HttpResponse(json.dumps("请以POST方式提交"))

def id_list_time(request):  # 依据时间对设备进行数据查询
    if request.method == 'GET':
        time_set = request.GET.get('time_set')
        models.Device.objects.filter(device_time_gte=time_set, safe=False)
        return JsonResponse("时间查询成功")
    elif request.method == 'POST':
        Id = request.GET.get('id')
        models.Device.objects.create(id=Id)
        return JsonResponse({"status":"true"},{"msg":"string"},{"id":Id})


def id_history_state(request):  # 数据设备历史状态查询
    if request.method == 'GET':
        Id=request.GET.get('id')
        models.Device.objects.filter(device_status='0',id=Id)
        models.Device.objects.filter(device_status='1',id=Id)
    return JsonResponse('以获取开关状态', safe=False)


def information_add(request):  # 添加数据（多次与一次）
    if request.method == 'PUT':
        name = request.PUT.get('name')
        status = request.PUT.get('status')
        time = request.PUT.get('time')
        value = request.put.get('value')
        models.Device.objects.create(device_name=name, device_status=status, device_time=time, device_value=value)
    return JsonResponse('已添加', safe=False)


def id_delete(request):  # 数据的删除
    if request.method == 'GET':
        value = request.GET.get('value')
        models.Device.objects.filter(device_value=value).delete()
    return JsonResponse('成功删除', safe=False)
