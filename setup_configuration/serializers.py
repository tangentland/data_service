from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework import exceptions
from . models import *

from rest_framework import serializers
#from rest_framework_mongoengine.serializers import DocumentSerializer, EmbeddedDocumentSerializer


class camera_list_serializers( serializers.ModelSerializer ):
    class Meta:
        model = camera_list
        fields = ('__all__')
            
class camera_configs_serializers( serializers.ModelSerializer ):
    class Meta:
        model = camera_configs
        fields = ('__all__')
            
class camera_group_serializers( serializers.ModelSerializer ):
    class Meta:
        model = camera_group
        fields = ('group_id', 'cameras',)