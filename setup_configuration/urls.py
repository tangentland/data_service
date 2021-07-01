from django.urls import path
from django.conf.urls import url, include

from .views import *


urlpatterns = [

        path('get_camera_list/', get_camera_list),
        path('register_camera/', register_camera),
        path('get_camera_by_company/', get_camera_by_company),
        path('create_configuration/', create_configuration),


]