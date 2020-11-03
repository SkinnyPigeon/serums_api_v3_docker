# Imports
from sqlalchemy import Column, Integer, BigInteger, String, Numeric, DateTime, Text, ForeignKey

# Column Types

column_types = {
    'integer': Integer,
    'string': String,
    'varchar': String,
    'numeric': Numeric,
    'datetime': DateTime,
    'text': Text
}

# Functions

def get_class_by_tablename(table_fullname, base):
  for class_name in base._decl_class_registry.values():
    if hasattr(class_name, '__table__') and class_name.__table__.fullname == table_fullname:
      return class_name

def create_ustan_dv(schema, base, engine):

    # HUBS
        
    hub_time={'__tablename__': 'hub_time',
    '__table_args__':{'schema': schema},
    'id': Column(column_types['integer'], primary_key=True)}

    keys = [{'chi': Column(BigInteger)}]
    for key in keys:
        hub_time.update(key)

    time = type('USTAN_Hub_Time',(base,),hub_time)
        
    hub_person={'__tablename__': 'hub_person',
    '__table_args__':{'schema': schema},
    'id': Column(column_types['integer'], primary_key=True)}

    keys = [{'chi': Column(BigInteger)}]
    for key in keys:
        hub_person.update(key)

    person = type('USTAN_Hub_Person',(base,),hub_person)
        
    hub_object={'__tablename__': 'hub_object',
    '__table_args__':{'schema': schema},
    'id': Column(column_types['integer'], primary_key=True)}

    keys = [{'chi': Column(BigInteger)}]
    for key in keys:
        hub_object.update(key)

    object = type('USTAN_Hub_Object',(base,),hub_object)
        
    hub_location={'__tablename__': 'hub_location',
    '__table_args__':{'schema': schema},
    'id': Column(column_types['integer'], primary_key=True)}

    keys = [{'chi': Column(BigInteger)}]
    for key in keys:
        hub_location.update(key)

    location = type('USTAN_Hub_Location',(base,),hub_location)
        
    hub_event={'__tablename__': 'hub_event',
    '__table_args__':{'schema': schema},
    'id': Column(column_types['integer'], primary_key=True)}

    keys = [{'chi': Column(BigInteger)}]
    for key in keys:
        hub_event.update(key)

    event = type('USTAN_Hub_Event',(base,),hub_event)
        

    hub_time = get_class_by_tablename("{schema}.hub_time".format(schema=schema), base)
    hub_person = get_class_by_tablename("{schema}.hub_person".format(schema=schema), base)
    hub_object = get_class_by_tablename("{schema}.hub_object".format(schema=schema), base)
    hub_location = get_class_by_tablename("{schema}.hub_location".format(schema=schema), base)
    hub_event = get_class_by_tablename("{schema}.hub_event".format(schema=schema), base)
    
    # Links

    person_time_link={'__tablename__': 'person_time_link',
    '__table_args__':{'schema':  schema},
    'id': Column(column_types['integer'], primary_key=True),
    'person_id': Column(column_types['integer'], ForeignKey(hub_person.id)),
    'time_id': Column(column_types['integer'], ForeignKey(hub_time.id))}

    person_time = type('FCRB_Person_Time_Link',(base,),person_time_link)

    #

    person_object_link={'__tablename__': 'person_object_link',
    '__table_args__':{'schema':  schema},
    'id': Column(column_types['integer'], primary_key=True),
    'person_id': Column(column_types['integer'], ForeignKey(hub_person.id)),
    'object_id': Column(column_types['integer'], ForeignKey(hub_object.id))}

    person_object = type('FCRB_Person_Object_Link',(base,),person_object_link)

    #

    person_location_link={'__tablename__': 'person_location_link',
    '__table_args__':{'schema':  schema},
    'id': Column(column_types['integer'], primary_key=True),
    'person_id': Column(column_types['integer'], ForeignKey(hub_person.id)),
    'location_id': Column(column_types['integer'], ForeignKey(hub_location.id))}

    person_location = type('FCRB_Person_Location_Link',(base,),person_location_link)

    #

    person_event_link={'__tablename__': 'person_event_link',
    '__table_args__':{'schema':  schema},
    'id': Column(column_types['integer'], primary_key=True),
    'person_id': Column(column_types['integer'], ForeignKey(hub_person.id)),
    'event_id': Column(column_types['integer'], ForeignKey(hub_event.id))}

    person_event = type('FCRB_Person_Event_Link',(base,),person_event_link)

    ###

    object_time_link={'__tablename__': 'object_time_link',
    '__table_args__':{'schema':  schema},
    'id': Column(column_types['integer'], primary_key=True),
    'object_id': Column(column_types['integer'], ForeignKey(hub_object.id)),
    'time_id': Column(column_types['integer'], ForeignKey(hub_time.id))}

    object_time = type('FCRB_Object_Time_Link',(base,),object_time_link)

    #

    object_location_link={'__tablename__': 'object_location_link',
    '__table_args__':{'schema':  schema},
    'id': Column(column_types['integer'], primary_key=True),
    'object_id': Column(column_types['integer'], ForeignKey(hub_object.id)),
    'location_id': Column(column_types['integer'], ForeignKey(hub_location.id))}

    object_location = type('FCRB_Object_Location_Link',(base,),object_location_link)

    #

    object_event_link={'__tablename__': 'object_event_link',
    '__table_args__':{'schema':  schema},
    'id': Column(column_types['integer'], primary_key=True),
    'object_id': Column(column_types['integer'], ForeignKey(hub_object.id)),
    'event_id': Column(column_types['integer'], ForeignKey(hub_event.id))}

    object_event = type('FCRB_Object_Event_Link',(base,),object_event_link)

    ###

    time_location_link={'__tablename__': 'time_location_link',
    '__table_args__':{'schema':  schema},
    'id': Column(column_types['integer'], primary_key=True),
    'time_id': Column(column_types['integer'], ForeignKey(hub_time.id)),
    'location_id': Column(column_types['integer'], ForeignKey(hub_location.id))}

    time_location = type('FCRB_Time_Location_Link',(base,),time_location_link)

    #

    time_event_link={'__tablename__': 'time_event_link',
    '__table_args__':{'schema':  schema},
    'id': Column(column_types['integer'], primary_key=True),
    'time_id': Column(column_types['integer'], ForeignKey(hub_time.id)),
    'event_id': Column(column_types['integer'], ForeignKey(hub_event.id))}

    time_event = type('FCRB_Time_Event_Link',(base,),time_event_link)

    ###
    
    location_event_link={'__tablename__': 'location_event_link',
    '__table_args__':{'schema':  schema},
    'id': Column(column_types['integer'], primary_key=True),
    'location_id': Column(column_types['integer'], ForeignKey(hub_location.id)),
    'event_id': Column(column_types['integer'], ForeignKey(hub_event.id))}

    location_event = type('FCRB_Location_Event_Link',(base,),location_event_link)

    ###

    # Satellites
        
    new_satellite={'__tablename__':'sat_event_chemocare_treatment',
    '__table_args__':{'schema': schema},
    'id': Column(column_types['integer'], primary_key=True),
    'source_table': Column(column_types['string']),
    'hub_id': Column(column_types['integer'], ForeignKey(hub_event.id))}

    columns = [
        {'intension': Column(column_types['string'])},
        {'regime': Column(column_types['string'])},
        {'outcome': Column(column_types['string'])}
    ]
    for column in columns:
        new_satellite.update(column)

    event_chemocare_treatment = type('USTAN_Sat_Event_Chemocare_Treatment',(base,),new_satellite)

    #
        
    new_satellite={'__tablename__':'sat_time_chemocare_dates',
    '__table_args__':{'schema': schema},
    'id': Column(column_types['integer'], primary_key=True),
    'source_table': Column(column_types['string']),
    'hub_id': Column(column_types['integer'], ForeignKey(hub_time.id))}

    columns = [
        {'appointment_date': Column(column_types['datetime'])}
    ]
    for column in columns:
        new_satellite.update(column)

    time_chemocare_dates = type('USTAN_Sat_Time_Chemocare_Dates',(base,),new_satellite)

    #

    new_satellite={'__tablename__':'sat_object_drug_details',
    '__table_args__':{'schema': schema},
    'id': Column(column_types['integer'], primary_key=True),
    'source_table': Column(column_types['string']),
    'hub_id': Column(column_types['integer'], ForeignKey(hub_object.id))}

    columns = [
        {'drug_dose': Column(column_types['integer'])},
        {'drug_type': Column(column_types['string'])},
        {'drug_status': Column(column_types['string'])}
    
    ]
    for column in columns:
        new_satellite.update(column)

    object_drug_details = type('USTAN_Sat_Object_Drug_Details',(base,),new_satellite)

    #

    new_satellite={'__tablename__':'sat_person_patient_details',
    '__table_args__':{'schema': schema},
    'id': Column(column_types['integer'], primary_key=True),
    'source_table': Column(column_types['string']),
    'hub_id': Column(column_types['integer'], ForeignKey(hub_person.id))}

    columns = [
        {'name': Column(column_types['integer'])},
        {'initial': Column(column_types['string'])},
        {'gp_name': Column(column_types['string'])},
        {'postcode': Column(column_types['string'])},
        {'age': Column(column_types['integer'])},
        {'dat_birth': Column(column_types['datetime'])},
        {'gender': Column(column_types['string'])},
        {'civil_status': Column(column_types['integer'])},
        {'religion': Column(column_types['integer'])},
        {'ref_hospital': Column(column_types['integer'])},
        {'dat_death': Column(column_types['datetime'])}
    ]

    for column in columns:
        new_satellite.update(column)

    person_patient_details = type('USTAN_Sat_Person_Patient_Details',(base,),new_satellite)

    #

    new_satellite={'__tablename__':'sat_time_diagnosis_date',
    '__table_args__':{'schema': schema},
    'id': Column(column_types['integer'], primary_key=True),
    'source_table': Column(column_types['string']),
    'hub_id': Column(column_types['integer'], ForeignKey(hub_time.id))}

    columns = [
        {'first_seen_date': Column(column_types['datetime'])}
    ]
    for column in columns:
        new_satellite.update(column)

    time_diagnosis_date = type('USTAN_Sat_Time_Diagnosis_Date',(base,),new_satellite)

    #

    new_satellite={'__tablename__':'sat_event_diagnosis_details',
    '__table_args__':{'schema': schema},
    'id': Column(column_types['integer'], primary_key=True),
    'source_table': Column(column_types['string']),
    'hub_id': Column(column_types['integer'], ForeignKey(hub_event.id))}

    columns = [
        {'"primary"': Column(column_types['integer'])},
        {'age': Column(column_types['integer'])},
        {'site': Column(column_types['string'])},
        {'side': Column(column_types['integer'])},
        {'histology': Column(column_types['integer'])},
        {'stage': Column(column_types['string'])},
        {'tnm_t': Column(column_types['string'])},
        {'tnm_n': Column(column_types['string'])},
        {'tnm_m': Column(column_types['string'])},
        {'perf_stat': Column(column_types['string'])},
        {'metastasis1': Column(column_types['string'])},
    ]
    for column in columns:
        new_satellite.update(column)

    event_diagnosis_details = type('USTAN_Sat_Event_Diagnosis_Details',(base,),new_satellite)

    #

    new_satellite={'__tablename__':'sat_time_care_dates',
    '__table_args__':{'schema': schema},
    'id': Column(column_types['integer'], primary_key=True),
    'source_table': Column(column_types['string']),
    'hub_id': Column(column_types['integer'], ForeignKey(hub_time.id))}

    columns = [
        {'incidence_date': Column(column_types['datetime'])},
        {'admission_date': Column(column_types['datetime'])},
        {'length_of_stay': Column(column_types['integer'])},
        {'discharge_date': Column(column_types['datetime'])}
    ]
    for column in columns:
        new_satellite.update(column)

    time_care_dates = type('USTAN_Sat_Time_Care_Dates',(base,),new_satellite)

    #

    new_satellite={'__tablename__':'sat_object_condition_details',
    '__table_args__':{'schema': schema},
    'id': Column(column_types['integer'], primary_key=True),
    'source_table': Column(column_types['string']),
    'hub_id': Column(column_types['integer'], ForeignKey(hub_object.id))}

    columns = [
        {'main_condition': Column(column_types['string'])},
        {'other_condition1': Column(column_types['string'])},
        {'other_condition2': Column(column_types['string'])},
        {'other_condition3': Column(column_types['string'])}
    ]
    for column in columns:
        new_satellite.update(column)

    object_condition_details = type('USTAN_Sat_Object_Condition_Details',(base,),new_satellite)

    #

    new_satellite={'__tablename__':'sat_object_operation_details',
    '__table_args__':{'schema': schema},
    'id': Column(column_types['integer'], primary_key=True),
    'source_table': Column(column_types['string']),
    'hub_id': Column(column_types['integer'], ForeignKey(hub_object.id))}

    columns = [
        {'main_operation_a': Column(column_types['string'])},
        {'main_operation_b': Column(column_types['string'])}
    ]
    for column in columns:
        new_satellite.update(column)

    object_operation_details = type('USTAN_Sat_Object_Operation_Details',(base,),new_satellite)

    #

    new_satellite={'__tablename__':'sat_person_care_details',
    '__table_args__':{'schema': schema},
    'id': Column(column_types['integer'], primary_key=True),
    'source_table': Column(column_types['string']),
    'hub_id': Column(column_types['integer'], ForeignKey(hub_person.id))}

    columns = [
        {'waiting_list_type': Column(column_types['integer'])},
        {'marital_status': Column(column_types['string'])},
        {'ethnic_group': Column(column_types['string'])}
    ]
    for column in columns:
        new_satellite.update(column)
	
    person_care_details = type('USTAN_Sat_Person_Care_Details',(base,),new_satellite)

    #
        
    base.metadata.create_all(engine)
    