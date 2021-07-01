
#DB Connection switch based on app


class Database_Router(object):
    def db_for_read( self, model, **hints ):
        if model._meta.app_label == 'user_management':
            return 'user'
        elif model._meta.app_label == 'setup_configuration':
            return 'config_setup'
        elif model._meta.app_label == 'dataviewer':
            return 'dataviewer'
        else:
            return 'default'
    
    def db_for_write( self, model, **hints ):
        if model._meta.app_label == 'user_management':
            return 'user'
        elif model._meta.app_label == 'setup_configuration':
            return 'config_setup'
        elif model._meta.app_label == 'dataviewer':
            return 'dataviewer'
        else:
            return 'default'

    def allow_relation( self, obj1, obj2, **hints ):
        if obj1._meta.app_label == 'user_management' and obj2._meta.app_label == 'user_management':
            return True
        elif 'user_management' in [obj1._meta.app_label, obj2._meta.app_label]:
            return True
        elif obj1._meta.app_label == 'setup_configuration'  and obj2._meta.app_label == 'setup_configuration':
            return True
        elif 'setup_configuration' in [obj1._meta.app_label, obj2._meta.app_label]:
            return True
        elif 'dataviewer' in [obj1._meta.app_label, obj2._meta.app_label]:
            return True
        else:
            return False