
from atlapi.attribute_dict import *

create_type_schema = AD({
})

create_type_sql = f'''insert into resource_type_schema (path, json_schema, media_path)
                                    values ( '{type_name}', '{json_schema}', '{s3_path}');'''

create_resource_type_sql = '''insert into resource_type (resource_path, type_schema_path, json_schema, semver)
                                    values ('{resource_path}', '{schema_type}', '{json_schema}', '{semver}');'''

create_resource_domain_sql = '''insert into resource_type (resource_path, type_schema_path, json_schema, semver)
                                    values ('{resource_path}', '{schema_type}', '{json_schema}', '{semver}');'''


add_resource_to_domain_resolver_sql = '''

'''

create_resource_sql = '''

'''
