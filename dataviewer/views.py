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
#from django.db.models import get_model
from django.apps import apps

@csrf_exempt
@api_view(['GET'])
@permission_classes([AllowAny])
def get_object_details(request):
    #request.data.object_type
    #request.data.id
    try:
        model_object = apps.get_model('dataviewer', request.data['object_type'])
        obj = model_object.objects.get(object_id=request.data['object_id'])
        serializer_str = "serializer_" + str(request.data['object_type'])
        serializer_class = eval(serializer_str)
        serializer = serializer_class(obj, context={'object_id': request.data['object_id']})
        return JsonResponse({"ret_code" : True, "data" : serializer.data})
        
    except Exception as e:
        return JsonResponse({"ret_code" : False, "data" : str(e)})

@csrf_exempt
@api_view(['POST'])
@permission_classes([AllowAny])
def create_object(request):
    #request.data.object_type
    #request.data.data
    try:
        serializer_str = "serializer_" + str(request.data['object_type'])
        serializer_class = eval(serializer_str)
        serializer = serializer_class(data=request.data['data'])
        
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"ret_code" : True, "data" : serializer.data})
        else:
            return JsonResponse({"ret_code" : False, "data" : serializer.errors})
            
    except Exception as e:
        return JsonResponse({"ret_code" : False, "data" : str(e)})
        
      