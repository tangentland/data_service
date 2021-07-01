from rest_framework import serializers
from rest_framework import exceptions
from . models import *

from rest_framework import serializers


class serializer_facility(serializers.ModelSerializer):
    children = serializers.SerializerMethodField('_get_children_data')
    
    def _get_children_data(self, obj):
        #code
        return []


    class Meta:
        model = facility
        fields = ("object_type","organization", "object_id","display_name" , "children")
        
        
class serializer_contact(serializers.ModelSerializer):
    children = serializers.SerializerMethodField('_get_children_data')
    
    def _get_children_data(self, obj):
        #code
        return []
    
    class Meta:
        model = contact
        fields = ("object_type", "contact_type", "object_id", "email", "phone", "address", "city", "state", "country", "zip", "display_name" , "children")
        
class serializer_insight(serializers.ModelSerializer):
    children = serializers.SerializerMethodField('_get_children_data')
    
    def _get_children_data(self, obj):
        #code
        return []


    class Meta:
        model = insight
        fields = ("object_type","organization", "object_id","display_name", "observations", "determinations", "metrics", "children")
        
class serializer_resource(serializers.ModelSerializer):
    
    children = serializers.SerializerMethodField('_get_children_data')
    
    
    def _get_children_data(self, obj):
        resource_id = self.context.get("object_id")
        return_pkt =[]
        customer_qs = customer.objects.filter(resource=resource_id).values("object_type" , "display_name" , "object_id")
        device_qs = device.objects.filter(resource=resource_id).values("object_type" , "display_name" , "object_id")
        location_qs = location.objects.filter(resource=resource_id).values("object_type" , "display_name" , "object_id")
        
        return_pkt.extend(list(customer_qs))
        return_pkt.extend(list(device_qs))
        return_pkt.extend(list(location_qs))

        return list(return_pkt)
    
    class Meta:
        model = resource
        fields = ("object_type", "object_id" , "resource_name", "display_name", "children")
        
class serializer_devices (serializers.ModelSerializer):
    children = serializers.SerializerMethodField('_get_children_data')
    
    def _get_children_data(self, obj):
        #code
        return []

    class Meta:
        model = device
        fields = ('object_type' , 'customer_name' 'object_id' , 'customer_name', 'display_name', 'children')
        
class serializer_station_caregory_profile(serializers.ModelSerializer):
    class Meta:
        model = station_caregory_profile
        fields = ('__all__')
        
class serializer_location(serializers.ModelSerializer):
    children = serializers.SerializerMethodField('_get_children_data')
    
    def _get_children_data(self, obj):
        #code
        return []
        
    class Meta:
        model = location
        fields = ("object_id", "object_type","location_name", "address","facility_nickname", "timezone", "hours_of_operation", "shifts", "use_case"	, "contacts", "cgr","subnet","stations", "display_name", "children")
        
class serializer_role(serializers.ModelSerializer):
    children = serializers.SerializerMethodField('_get_children_data')
    
    def _get_children_data(self, obj):
        #code
        return []
        
    class Meta:
        model = role
        fields = ("object_id", "object_type", "role_name", "display_name", "children")
        
class serializer_group(serializers.ModelSerializer):
    children = serializers.SerializerMethodField('_get_children_data')
    
    def _get_children_data(self, obj):
        #code
        return []
        
    class Meta:
        model = group
        fields = ("object_id", "object_type", "group_name", "display_name", "children")
        
class serializer_device(serializers.ModelSerializer):
    class Meta:
        model = device
        fields = ('__all__')    

       
class serializer_customer(serializers.ModelSerializer):
    class Meta:
        model = customer
        fields = ('__all__')
        
class serializer_user(serializers.ModelSerializer):
    children = serializers.SerializerMethodField('_get_children_data')
    
    def _get_children_data(self, obj):
        #code
        return []
        
    class Meta:
        model = user
        fields = ("object_type","object_id", "username", "fname", "lname", "roles", "display_name", "children")
        
class serializer_organization(serializers.ModelSerializer):
    children = serializers.SerializerMethodField('_get_children_data')
    
    def _get_children_data(self, obj):
        org_id = self.context.get("object_id")
        return_pkt =[]
        org_qs = organization.objects.filter(org=org_id).values("object_type" , "display_name" , "object_id")
        user_qs = user.objects.filter(organization=org_id).values("object_type" , "display_name" , "object_id")
        role_qs = role.objects.filter(organization=org_id).values("object_type" , "display_name" , "object_id")
        group_qs = group.objects.filter(organization=org_id).values("object_type" , "display_name" , "object_id")
        facility_qs = facility.objects.filter(organization=org_id).values("object_type" , "display_name" , "object_id")
        contact_qs = contact.objects.filter(organization=org_id).values("object_type" , "display_name" , "object_id")
        insight_qs = insight.objects.filter(organization=org_id).values("object_type" , "display_name" , "object_id")
        resource_qs = resource.objects.filter(organization=org_id).values("object_type" , "display_name" , "object_id")
        
        
        
        return_pkt.extend(list(org_qs))
        return_pkt.extend(list(user_qs))
        return_pkt.extend(list(role_qs))
        return_pkt.extend(list(group_qs))
        return_pkt.extend(list(facility_qs))
        return_pkt.extend(list(contact_qs))
        return_pkt.extend(list(insight_qs))
        return_pkt.extend(list(resource_qs))

        return list(return_pkt)
        return []
    class Meta:
        model = organization
        fields = ("object_type","object_id","name", "display_name", "children")
