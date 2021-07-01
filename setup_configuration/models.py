from django.db import models
import jsonfield
from django.contrib.postgres.fields import JSONField
from datetime import datetime
from django.contrib.postgres.fields import ArrayField
from datetime import datetime


CAMERA_STATUS = [
                    ("Active", "Active"), 
                    ("Inactive", "Inactive"),
                ]

CONFIGURATION_STATUS = [
                    ("Active", "Active"), 
                    ("Inactive", "Inactive"),
                ]
                
INCIDENT_TYPE = [
                    ("Air Dusting", "Air Dusting"),
                    ("Cage Operation", "Cage Operation"),
                    ("PPE", "PPE"),
                    ("Track Allignment", "Track Allignment")
                ]


class camera_list(models.Model):
    camera_id = models.AutoField(max_length=25, primary_key=True)
    camera_name = models.CharField( max_length=100, default='', null=True, blank=True )
    camera_status = models.CharField( max_length=100, choices=CAMERA_STATUS, default='', null=True, blank=True )
    company_name = models.CharField( max_length=200, default='', null=True, blank=True )
    
    class Meta:
        db_table = "camera_list"
        app_label = "setup_configuration"
        
class camera_configs(models.Model):
    config_id = models.AutoField(max_length=25, primary_key=True)
    config_name = models.CharField( max_length=100, unique=True )
    config_status = models.CharField( max_length=100, choices=CONFIGURATION_STATUS, default='', null=True, blank=True )
    data = ArrayField(models.CharField(max_length=100))
    last_modified_date = models.DateTimeField(default=datetime.now)
    
    
    class Meta:
        db_table = "camera_configs"
        app_label = "setup_configuration"
        
class camera_group(models.Model):
    group_id = models.AutoField(max_length=25, primary_key=True)
    cameras = JSONField(default=[], null=True, blank=True)
    
    class Meta:
        db_table = "camera_group"
        app_label = "setup_configuration"
        

class incident_severity_mapping(models.Model):
    camera_config = models.OneToOneField(camera_configs, on_delete=models.CASCADE, primary_key=True)
    severity =  models.CharField( max_length=100 )
    incident_type = models.CharField( max_length=100 )
    
    class Meta:
        db_table = "incident_severity_mapping"
        app_label = "setup_configuration"

class truck_details(models.Model):
    truck_id = models.AutoField(max_length=25, primary_key=True)
    license_number = models.CharField( max_length=100 )
    driver_id = models.CharField( max_length=100 )
    driver_name = models.CharField( max_length=100 )
    truck_customer = models.CharField( max_length=100 )
    
    class Meta:
        db_table = "truck_details"
        app_label = "setup_configuration"
        
class incident_details(models.Model):
    time = models.DateTimeField(default=datetime.now())
    truck_id = models.ForeignKey(truck_details, on_delete=models.CASCADE)
    camera_id = models.ForeignKey(camera_list, on_delete=models.CASCADE)
    incident_type = models.CharField( max_length=100, choices=INCIDENT_TYPE, default='', null=True, blank=True )
    severity =  models.CharField( max_length=100 )
    video = models.FileField()
    images = ArrayField(models.FileField())
    
    class Meta:
        db_table = "incident_details"
        app_label = "setup_configuration"
    
    

    
    