from django.urls import path
from django.conf.urls import url, include

from .views import *


urlpatterns = [

        path('get_object_details/', get_object_details),
        path('create_object/', create_object),

]