from django.shortcuts import render
from datetime import datetime, timedelta
from django.conf import settings
from django.apps import apps
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.core import serializers
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated

import os, sys
import json
import jwt
from collections import OrderedDict

from .models import *
from .serializers import *


# Create your views here.

@csrf_exempt
@api_view(['GET'])
@permission_classes([AllowAny])
def get_camera_list(request):
    try:
        #request_data = request.data
        cam_object = camera_list.objects.all().values()
        return JsonResponse({"ret_code" : True, "ret_data" : list(cam_object)})
    except Exception as e:
        return JsonResponse({"ret_code" : False, "ret_data" : str(e)})

@csrf_exempt
@api_view(['POST'])
@permission_classes([AllowAny])
def create_configuration(request):
    try:
        groups_data = request.data['groups']
        config_data = request.data['config']
        serialize_data = camera_group_serializers(data=groups_data, many=True)
        if serialize_data.is_valid():
            serialize_data.save()
            group_data_dict = list(json.loads(json.dumps(serialize_data.data)))
            groups = [each['group_id'] for each in group_data_dict]
            config_data["data"] = groups
            camera_config_serializer = camera_configs_serializers(data=config_data)
            if camera_config_serializer.is_valid():
                camera_config_serializer.save()
                return JsonResponse({"ret_code" : True, "ret_data" : camera_config_serializer.data})
            else:
                print("Configuration save error")
                return JsonResponse({"ret_code" : False, "ret_data" : camera_config_serializer.errors})
            
        else:
            print("Group submission error")
            return JsonResponse({"ret_code" : False, "ret_data" : serialize_data.errors})
    except Exception as e:
        print("main exception")
        return JsonResponse({"ret_code" : False, "ret_data" : str(e)})

@csrf_exempt
@api_view(['GET'])
@permission_classes([AllowAny])
def get_camera_by_company(request):
    try:
        cam_object = camera_list.objects.filter(company_name=request.data['company_name'])
        serialize_data = camera_list_serializers(cam_object, many=True)
        return JsonResponse({"ret_code" : True, "ret_data" : serialize_data.data})
    except Exception as e:
        return JsonResponse({"ret_code" : False, "ret_data" : serialize_data.errors})
        
        
@csrf_exempt
@api_view(['POST'])
@permission_classes([AllowAny])
def register_camera(request):
    try:
        request_data = request.data
        cam_object_serializer = camera_list_serializers(data=request_data, many=True)
        if cam_object_serializer.is_valid():
            cam_object_serializer.save()
            return JsonResponse({'ret_code' : True, 'return_data' : cam_object_serializer.data})
        else:
            return JsonResponse({'ret_code' : False, 'return_data' : cam_object_serializer.errors})
    except Exception as e:
        return JsonResponse({"ret_code" : False, "ret_data" : str(e)})