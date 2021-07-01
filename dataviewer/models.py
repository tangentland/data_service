from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import PermissionsMixin
import jwt
from datetime import datetime
from datetime import timedelta
from django.conf import settings
from django.db import models
from django.core import validators
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django import forms
from django.contrib.postgres.fields import ArrayField

OBJECT_TYPE = [
                    ("contact", "contact"),
                    ("organization", "organization"),
                    ("insight", "insight"),
                    ("location", "location"),
                    ("resource", "resource"),
                    ("facility", "facility"),
                    ("role", "role"),
                    ("group", "group"),
                    ("user", "user"),
                    ("device", "device"),
                ]

CONTACT_TYPE = [
                    ("business", "business"),
                    ("technical", "technical"),
                    ("administrative", "administrative"),
                ]


    
class organization(models.Model):
    object_type = models.CharField( max_length=100, choices=OBJECT_TYPE, default='organization')
    object_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    org = models.ForeignKey('self', on_delete=models.CASCADE, default='', null=True, blank=True)
    display_name = models.CharField( max_length=100 )
    
    class Meta:
        app_label = 'dataviewer'
        db_table = 'organization'
        
class facility(models.Model):
    object_type = models.CharField( max_length=100, choices=OBJECT_TYPE, default='facility')
    object_id = models.AutoField(primary_key=True)
    organization = models.ForeignKey(organization, on_delete=models.CASCADE )
    display_name = models.CharField( max_length=100 )
    
    class Meta:
        app_label = 'dataviewer'
        db_table = 'facility'

class contact(models.Model):
    object_type = models.CharField( max_length=100, choices=OBJECT_TYPE, default='contact')
    contact_type = models.CharField( max_length=100, choices=CONTACT_TYPE)
    organization = models.ForeignKey(organization, on_delete=models.CASCADE )
    object_id = models.AutoField(primary_key=True)
    email = models.CharField( max_length=100 )
    phone = models.CharField( max_length=100 )
    address = models.CharField( max_length=100 )
    city = models.CharField( max_length=100 )
    state = models.CharField( max_length=100 )
    country = models.CharField( max_length=100 )
    zip = models.CharField( max_length=100 )
    display_name = models.CharField( max_length=100 )
    
    class Meta:
        app_label = 'dataviewer'
        db_table = 'contact'
    
class insight(models.Model):
    object_type = models.CharField( max_length=100, choices=OBJECT_TYPE, default='insight')
    object_id = models.AutoField(primary_key=True)
    organization = models.ForeignKey(organization, on_delete=models.CASCADE )
    observations = models.CharField( max_length=100 )
    determinations = models.CharField( max_length=100 )
    metrics = models.CharField( max_length=100 )
    display_name = models.CharField( max_length=100 )
    
    class Meta:
        app_label = 'dataviewer'
        db_table = 'insight'

class resource(models.Model):
    object_type = models.CharField( max_length=100, choices=OBJECT_TYPE, default='resource')
    object_id = models.AutoField(primary_key=True)
    resource_type = models.CharField( max_length=100 )
    resource_name = models.CharField( max_length=100 )
    organization = models.ForeignKey(organization, on_delete=models.CASCADE )
    display_name = models.CharField( max_length=100 )
    
    class Meta:
        app_label = 'dataviewer'
        db_table = 'resource'
        
class customer(models.Model):
    object_type = models.CharField( max_length=100, choices=OBJECT_TYPE, default='customer')
    object_id = models.AutoField(primary_key=True)
    customer_name = models.CharField( max_length=100 )
    resource = models.ForeignKey(resource, on_delete=models.CASCADE )
    display_name = models.CharField( max_length=100 , default="" )

    class Meta:
        app_label = 'dataviewer'
        db_table = 'customer'

class device(models.Model):
    object_type = models.CharField( max_length=100, choices=OBJECT_TYPE, default='device')
    object_id = models.AutoField(primary_key=True)
    device_name = models.CharField( max_length=100 )
    resource = models.ForeignKey(resource, on_delete=models.CASCADE )
    display_name = models.CharField( max_length=100 )
    
    class Meta:
        app_label = 'dataviewer'
        db_table = 'devices'
    
class location(models.Model):
    object_id = models.AutoField(primary_key=True)
    object_type = models.CharField( max_length=100, choices=OBJECT_TYPE, default='location')
    location_name = models.CharField( max_length=100 )
    address = models.CharField( max_length=100 )
    facility_nickname = models.CharField( max_length=100 )
    timezone = models.CharField( max_length=100 )
    hours_of_operation = models.CharField( max_length=100 )
    shifts = models.CharField( max_length=100 )
    use_case = models.CharField( max_length=100 )
    cgr = models.CharField( max_length=100 )
    subnet = models.CharField( max_length=100 )
    display_name = models.CharField( max_length=100 )
    resource = models.ForeignKey(resource, on_delete=models.CASCADE )
    
    class Meta:
        app_label = 'dataviewer'
        db_table = 'location'
    
class station_caregory_profile(models.Model):
    object_id = models.AutoField(primary_key=True)
    station_type = models.CharField( max_length=100 )
    station_class = models.CharField( max_length=100 )
    station_model = models.CharField( max_length=100 )
    lanes = models.CharField( max_length=100 )
    display_name = models.CharField( max_length=100 )
    locations = models.ForeignKey(location, on_delete=models.CASCADE)
    
    class Meta:
        app_label = 'dataviewer'
        db_table = 'station_caregory_profile'
    

class role(models.Model):
    object_type = models.CharField( max_length=100, choices=OBJECT_TYPE, default='role' )
    object_id = models.AutoField(primary_key=True)
    role_name = models.CharField( max_length=100 )
    display_name = models.CharField( max_length=100 )
    organization = models.ForeignKey(organization, on_delete=models.CASCADE )
    
    class Meta:
        app_label = 'dataviewer'
        db_table = 'role'
    
class group(models.Model):
    object_type = models.CharField( max_length=100, choices=OBJECT_TYPE, default='group' )
    object_id = models.AutoField(primary_key=True)
    name = models.CharField( max_length=100 )
    display_name = models.CharField( max_length=100 )
    organization = models.ForeignKey(organization, on_delete=models.CASCADE )
    
    class Meta:
        app_label = 'dataviewer'
        db_table = 'group'
    
class user(models.Model):
    object_type = models.CharField( max_length=100, choices=OBJECT_TYPE, default='user' )
    object_id = models.AutoField(primary_key=True)
    username = models.CharField(db_index=True, max_length=255, unique=True)
    fname = models.CharField( max_length=100 )
    lname = models.CharField( max_length=100 )
    roles = models.ManyToManyField(role)
    display_name = models.CharField( max_length=100 )
    organization = models.ForeignKey(organization, on_delete=models.CASCADE )
    
    class Meta:
        app_label = 'dataviewer'
        db_table = 'user'
