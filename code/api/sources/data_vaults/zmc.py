# Imports

from sqlalchemy import Column, Integer, String, Numeric, DateTime, Text, ForeignKey

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

def create_zmc_dv(schema, base, engine):
    
    # HUBS
        
    hub_time={'__tablename__': 'hub_time',
    '__table_args__':{'schema': schema},
    'id': Column(column_types['integer'], primary_key=True)}

    keys = [{'patnr': Column(Integer)}]
    for key in keys:
        hub_time.update(key)

    time = type('ZMC_Hub_Time',(base,),hub_time)
        
    hub_person={'__tablename__': 'hub_person',
    '__table_args__':{'schema': schema},
    'id': Column(column_types['integer'], primary_key=True)}

    keys = [{'patnr': Column(Integer)}]
    for key in keys:
        hub_person.update(key)

    person = type('ZMC_Hub_Person',(base,),hub_person)
        
    hub_object={'__tablename__': 'hub_object',
    '__table_args__':{'schema': schema},
    'id': Column(column_types['integer'], primary_key=True)}

    keys = [{'patnr': Column(Integer)}]
    for key in keys:
        hub_object.update(key)

    object = type('ZMC_Hub_Object',(base,),hub_object)
        
    hub_location={'__tablename__': 'hub_location',
    '__table_args__':{'schema': schema},
    'id': Column(column_types['integer'], primary_key=True)}

    keys = [{'patnr': Column(Integer)}]
    for key in keys:
        hub_location.update(key)

    location = type('ZMC_Hub_Location',(base,),hub_location)
        
    hub_event={'__tablename__': 'hub_event',
    '__table_args__':{'schema': schema},
    'id': Column(column_types['integer'], primary_key=True)}

    keys = [{'patnr': Column(Integer)}]
    for key in keys:
        hub_event.update(key)

    event = type('ZMC_Hub_Event',(base,),hub_event)
        
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
        
    new_satellite={'__tablename__':'sat_event_exercise_measurements',
    '__table_args__':{'schema': schema},
    'id': Column(column_types['integer'], primary_key=True),
    'source_table': Column(column_types['string']),
    'hub_id': Column(column_types['integer'], ForeignKey(hub_event.id))}

    columns = [{'nr_sst': Column(column_types['integer'])},{'steps_total': Column(column_types['integer'])},{'cadence': Column(column_types['integer'])},{'cyc_rot': Column(column_types['integer'])},{'cyc_rpm': Column(column_types['integer'])}]
    for column in columns:
        new_satellite.update(column)

    event_exercise_measurements = type('ZMC_Sat_Event_Exercise_Measurements',(base,),new_satellite)

    #
    
    new_satellite={'__tablename__':'sat_time_exercise_measurements',
    '__table_args__':{'schema': schema},
    'id': Column(column_types['integer'], primary_key=True),
    'source_table': Column(column_types['string']),
    'hub_id': Column(column_types['integer'], ForeignKey(hub_time.id))}

    columns = [{'day_nr': Column(column_types['integer'])},{'time_total': Column(column_types['integer'])},{'time_passive': Column(column_types['integer'])},{'time_active': Column(column_types['integer'])},{'time_sit': Column(column_types['integer'])},{'time_stand': Column(column_types['integer'])},{'time_walk': Column(column_types['integer'])},{'time_cycle': Column(column_types['integer'])},{'time_hi': Column(column_types['integer'])}]
    for column in columns:
        new_satellite.update(column)

    time_exercise_measurements = type('ZMC_Sat_Time_Exercise_Measurements',(base,),new_satellite)

    #
        
    new_satellite={'__tablename__':'sat_person_patient_details',
    '__table_args__':{'schema': schema},
    'id': Column(column_types['integer'], primary_key=True),
    'source_table': Column(column_types['string']),
    'hub_id': Column(column_types['integer'], ForeignKey(hub_person.id))}

    columns = [{'gschl': Column(column_types['varchar'])},{'nname': Column(column_types['varchar'])},{'nnams': Column(column_types['varchar'])},{'vname': Column(column_types['varchar'])},{'titel': Column(column_types['varchar'])},{'namzu': Column(column_types['varchar'])},{'gbdat': Column(column_types['datetime'])},{'gbnam': Column(column_types['varchar'])},{'gbnas': Column(column_types['varchar'])},{'gland': Column(column_types['varchar'])},{'natio': Column(column_types['varchar'])},{'land': Column(column_types['varchar'])},{'telf1': Column(column_types['varchar'])}]
    for column in columns:
        new_satellite.update(column)

    person_patient_details = type('ZMC_Sat_Person_Patient_Details',(base,),new_satellite)

    #
        
    new_satellite={'__tablename__':'sat_location_patient_address',
    '__table_args__':{'schema': schema},
    'id': Column(column_types['integer'], primary_key=True),
    'source_table': Column(column_types['string']),
    'hub_id': Column(column_types['integer'], ForeignKey(hub_location.id))}

    columns = [{'pstlz': Column(column_types['varchar'])},{'ort': Column(column_types['varchar'])},{'stras': Column(column_types['varchar'])}]
    for column in columns:
        new_satellite.update(column)

    location_patient_address = type('ZMC_Sat_Location_Patient_Address',(base,),new_satellite)

    #
        
    new_satellite={'__tablename__':'sat_person_patient_measurements',
    '__table_args__':{'schema': schema},
    'id': Column(column_types['integer'], primary_key=True),
    'source_table': Column(column_types['string']),
    'hub_id': Column(column_types['integer'], ForeignKey(hub_person.id))}

    columns = [{'height': Column(column_types['integer'])},{'weight': Column(column_types['integer'])},{'date': Column(column_types['datetime'])}]
    for column in columns:
        new_satellite.update(column)

    person_patient_measurements = type('ZMC_Sat_Person_Patient_Measurements',(base,),new_satellite)

    #
        
    new_satellite={'__tablename__':'sat_object_patient_documents',
    '__table_args__':{'schema': schema},
    'id': Column(column_types['integer'], primary_key=True),
    'source_table': Column(column_types['string']),
    'hub_id': Column(column_types['integer'], ForeignKey(hub_object.id))}

    columns = [{'report_title': Column(column_types['varchar'])},{'department': Column(column_types['varchar'])},{'date': Column(column_types['datetime'])},{'content': Column(column_types['text'])}]
    for column in columns:
        new_satellite.update(column)

    object_patient_documents = type('ZMC_Sat_Object_Patient_Documents',(base,),new_satellite)

    #
        
    new_satellite={'__tablename__':'sat_event_patient_appointments',
    '__table_args__':{'schema': schema},
    'id': Column(column_types['integer'], primary_key=True),
    'source_table': Column(column_types['string']),
    'hub_id': Column(column_types['integer'], ForeignKey(hub_event.id))}

    columns = [{'type': Column(column_types['varchar'])},{'date': Column(column_types['datetime'])},{'notes': Column(column_types['text'])}]
    for column in columns:
        new_satellite.update(column)

    event_patient_appointments = type('ZMC_Sat_Event_Patient_Appointments',(base,),new_satellite)

    #
        
    new_satellite={'__tablename__':'sat_event_patient_operations',
    '__table_args__':{'schema': schema},
    'id': Column(column_types['integer'], primary_key=True),
    'source_table': Column(column_types['string']),
    'hub_id': Column(column_types['integer'], ForeignKey(hub_event.id))}

    columns = [{'anatomical_location': Column(column_types['varchar'])},{'date': Column(column_types['datetime'])},{'notes': Column(column_types['text'])}]
    for column in columns:
        new_satellite.update(column)

    event_patient_operations = type('ZMC_Sat_Event_Patient_Operations',(base,),new_satellite)

    #

    new_satellite={'__tablename__':'sat_object_patient_alcohol_use',
    '__table_args__':{'schema': schema},
    'id': Column(column_types['integer'], primary_key=True),
    'source_table': Column(column_types['string']),
    'hub_id': Column(column_types['integer'], ForeignKey(hub_object.id))}

    columns = [{'usage_status': Column(column_types['varchar'])},{'quantity': Column(column_types['varchar'])},{'description': Column(column_types['varchar'])}]
    for column in columns:
        new_satellite.update(column)

    patient_alcohol_use = type('ZMC_Sat_Object_Patient_Alcohol_Use',(base,),new_satellite)

    #

    new_satellite={'__tablename__':'sat_object_patient_allergies_intolerance',
    '__table_args__':{'schema': schema},
    'id': Column(column_types['integer'], primary_key=True),
    'source_table': Column(column_types['string']),
    'hub_id': Column(column_types['integer'], ForeignKey(hub_object.id))}

    columns = [{'caustic_substance': Column(column_types['varchar'])},{'critical': Column(column_types['varchar'])},{'description': Column(column_types['varchar'])}]
    for column in columns:
        new_satellite.update(column)

    patient_allergies_intolerance = type('ZMC_Sat_Object_Patient_Allergies_Intolerance',(base,),new_satellite)

    #

    new_satellite={'__tablename__':'sat_object_patient_diagnostic',
    '__table_args__':{'schema': schema},
    'id': Column(column_types['integer'], primary_key=True),
    'source_table': Column(column_types['string']),
    'hub_id': Column(column_types['integer'], ForeignKey(hub_object.id))}

    columns = [{'type': Column(column_types['varchar'])},{'name': Column(column_types['varchar'])},{'anatomical_location': Column(column_types['varchar'])},{'laterality': Column(column_types['varchar'])}]
    for column in columns:
        new_satellite.update(column)

    object_patient_diagnostic = type('ZMC_Sat_Object_Patient_Diagnostic',(base,),new_satellite)

    #

    new_satellite={'__tablename__':'sat_time_patient_diagnostic',
    '__table_args__':{'schema': schema},
    'id': Column(column_types['integer'], primary_key=True),
    'source_table': Column(column_types['string']),
    'hub_id': Column(column_types['integer'], ForeignKey(hub_time.id))}

    columns = [{'begin_date': Column(column_types['datetime'])},{'end_date': Column(column_types['datetime'])}]
    for column in columns:
        new_satellite.update(column)

    time_patient_diagnostic = type('ZMC_Sat_Time_Patient_Diagnostic',(base,),new_satellite)

    #

    new_satellite={'__tablename__':'sat_object_patient_drug_use',
    '__table_args__':{'schema': schema},
    'id': Column(column_types['integer'], primary_key=True),
    'source_table': Column(column_types['string']),
    'hub_id': Column(column_types['integer'], ForeignKey(hub_object.id))}

    columns = [{'substance': Column(column_types['varchar'])},{'quantity': Column(column_types['varchar'])},{'description': Column(column_types['varchar'])},{'laterality': Column(column_types['varchar'])}]
    for column in columns:
        new_satellite.update(column)

    object_patient_drug_use = type('ZMC_Sat_Object_Patient_Drug_Use',(base,),new_satellite)

    #

    new_satellite={'__tablename__':'sat_object_patient_functional_state',
    '__table_args__':{'schema': schema},
    'id': Column(column_types['integer'], primary_key=True),
    'source_table': Column(column_types['string']),
    'hub_id': Column(column_types['integer'], ForeignKey(hub_object.id))}

    columns = [{'name': Column(column_types['varchar'])},{'value': Column(column_types['varchar'])}]
    for column in columns:
        new_satellite.update(column)

    object_patient_functional_state = type('ZMC_Sat_Object_Patient_Functional_State',(base,),new_satellite)

    #

    new_satellite={'__tablename__':'sat_time_patient_functional_state',
    '__table_args__':{'schema': schema},
    'id': Column(column_types['integer'], primary_key=True),
    'source_table': Column(column_types['string']),
    'hub_id': Column(column_types['integer'], ForeignKey(hub_time.id))}

    columns = [{'date': Column(column_types['datetime'])}]
    for column in columns:
        new_satellite.update(column)

    time_patient_functional_state = type('ZMC_Sat_Time_Patient_Functional_State',(base,),new_satellite)

    #

    new_satellite={'__tablename__':'sat_object_patient_living_situation',
    '__table_args__':{'schema': schema},
    'id': Column(column_types['integer'], primary_key=True),
    'source_table': Column(column_types['string']),
    'hub_id': Column(column_types['integer'], ForeignKey(hub_object.id))}

    columns = [{'house_type': Column(column_types['varchar'])},{'description': Column(column_types['varchar'])}]
    for column in columns:
        new_satellite.update(column)

    object_patient_living_situation = type('ZMC_Sat_Object_Patient_Living_Situation',(base,),new_satellite)

    #

    new_satellite={'__tablename__':'sat_object_patient_tobacco_use',
    '__table_args__':{'schema': schema},
    'id': Column(column_types['integer'], primary_key=True),
    'source_table': Column(column_types['string']),
    'hub_id': Column(column_types['integer'], ForeignKey(hub_object.id))}

    columns = [{'substance': Column(column_types['varchar'])},{'description': Column(column_types['varchar'])}]
    for column in columns:
        new_satellite.update(column)

    object_patient_tobacco_use = type('ZMC_Sat_Object_Patient_Tobacco_Use',(base,),new_satellite)

    #

    new_satellite={'__tablename__':'sat_object_patient_warnings',
    '__table_args__':{'schema': schema},
    'id': Column(column_types['integer'], primary_key=True),
    'source_table': Column(column_types['string']),
    'hub_id': Column(column_types['integer'], ForeignKey(hub_object.id))}

    columns = [{'alerts': Column(column_types['varchar'])},{'type': Column(column_types['varchar'])}]
    for column in columns:
        new_satellite.update(column)

    object_patient_warnings = type('ZMC_Sat_Object_Patient_Warnings',(base,),new_satellite)

    #

    new_satellite={'__tablename__':'sat_time_patient_warnings',
    '__table_args__':{'schema': schema},
    'id': Column(column_types['integer'], primary_key=True),
    'source_table': Column(column_types['string']),
    'hub_id': Column(column_types['integer'], ForeignKey(hub_time.id))}

    columns = [{'begin_date': Column(column_types['datetime'])}]
    for column in columns:
        new_satellite.update(column)

    time_patient_warnings = type('ZMC_Sat_Time_Patient_Warnings',(base,),new_satellite)

    #
  
    base.metadata.create_all(engine)
