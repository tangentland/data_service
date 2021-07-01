from django.urls import path
from django.conf.urls import url, include


urlpatterns = [

        path('config/', include('setup_configuration.urls')),
        path('dataviewer/', include('dataviewer.urls')),

]