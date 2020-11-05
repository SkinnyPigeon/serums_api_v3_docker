# Imports

from sqlalchemy import Column, Integer, String, Numeric, DateTime, Time, Text, ForeignKey

# Column Types

column_types = {
    'integer': Integer,
    'string': String,
    'varchar': String,
    'numeric': Numeric,
    'datetime': DateTime,
    'text': Text, 
    'time': Time
}

# Functions

def get_class_by_tablename(table_fullname, base):
  for class_name in base._decl_class_registry.values():
    if hasattr(class_name, '__table__') and class_name.__table__.fullname == table_fullname:
      return class_name


def create_fcrb_dv(schema, base, engine):
    
    # HUBS
        
    hub_time={'__tablename__': 'hub_time',
    '__table_args__':{'schema':  schema},
    'id': Column(column_types['integer'], primary_key=True)}

    keys = [{'einri': Column(String)},{'patnr': Column(Integer)},{'falnr': Column(String)},{'pernr': Column(String)},{'orgid': Column(String)},{'vppid': Column(String)}]
    for key in keys:
        hub_time.update(key)

    time = type('FCRB_Hub_Time',(base,),hub_time)
        
    hub_person={'__tablename__': 'hub_person',
    '__table_args__':{'schema':  schema},
    'id': Column(column_types['integer'], primary_key=True)}

    keys = [{'patnr': Column(Integer)},{'pernr': Column(String)},{'orgid': Column(String)}]
    for key in keys:
        hub_person.update(key)

    person = type('FCRB_Hub_Person',(base,),hub_person)
        
    hub_object={'__tablename__': 'hub_object',
    '__table_args__':{'schema':  schema},
    'id': Column(column_types['integer'], primary_key=True)}

    keys = [{'einri': Column(String)},{'patnr': Column(Integer)},{'falnr': Column(String)},{'pernr': Column(String)},{'orgid': Column(String)},{'vppid': Column(String)}]
    for key in keys:
        hub_object.update(key)

    object = type('FCRB_Hub_Object',(base,),hub_object)
        
    hub_location={'__tablename__': 'hub_location',
    '__table_args__':{'schema':  schema},
    'id': Column(column_types['integer'], primary_key=True)}

    keys = [{'patnr': Column(Integer)}]
    for key in keys:
        hub_location.update(key)

    location = type('FCRB_Hub_Location',(base,),hub_location)
        
    hub_event={'__tablename__': 'hub_event',
    '__table_args__':{'schema':  schema},
    'id': Column(column_types['integer'], primary_key=True)}

    keys = [{'einri': Column(String)},{'falnr': Column(String)},{'patnr': Column(Integer)},{'pernr': Column(String)}]
    for key in keys:
        hub_event.update(key)

    event = type('FCRB_Hub_Event',(base,),hub_event)

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
        
    new_satellite={'__tablename__':'sat_object_diagnostic_details',
    '__table_args__':{'schema':  schema},
    'id': Column(column_types['integer'], primary_key=True),
    'source_table': Column(column_types['string']),
    'hub_id': Column(column_types['integer'], ForeignKey(hub_object.id)),
    'display_text': Column(column_types['string'])}

    columns = [{'lfdnr': Column(column_types['integer'])},{'dkey1': Column(column_types['varchar'])}]
    for column in columns:
        new_satellite.update(column)

    object_diagnostic_details = type('FCRB_Sat_Object_Diagnostic_Details',(base,),new_satellite)

    #
        
    new_satellite={'__tablename__':'sat_object_treatment_category',
    '__table_args__':{'schema':  schema},
    'id': Column(column_types['integer'], primary_key=True),
    'source_table': Column(column_types['string']),
    'hub_id': Column(column_types['integer'], ForeignKey(hub_object.id)),
    'display_text': Column(column_types['string'])}

    columns = [{'bekat': Column(column_types['varchar'])}]
    for column in columns:
        new_satellite.update(column)

    object_treatment_category = type('FCRB_Sat_Object_Treatment_Category',(base,),new_satellite)

    #
        
    new_satellite={'__tablename__':'sat_event_episode_type',
    '__table_args__':{'schema':  schema},
    'id': Column(column_types['integer'], primary_key=True),
    'source_table': Column(column_types['string']),
    'hub_id': Column(column_types['integer'], ForeignKey(hub_event.id)),
    'display_text': Column(column_types['string'])}

    columns = [{'falar': Column(column_types['varchar'])},{'statu': Column(column_types['varchar'])},{'krzan': Column(column_types['varchar'])},{'storn': Column(column_types['varchar'])},{'casetx': Column(column_types['varchar'])},{'enddtx': Column(column_types['varchar'])}]
    for column in columns:
        new_satellite.update(column)

    event_episode_type = type('FCRB_Sat_Event_Episode_Type',(base,),new_satellite)

    #
        
    new_satellite={'__tablename__':'sat_object_medical_center',
    '__table_args__':{'schema':  schema},
    'id': Column(column_types['integer'], primary_key=True),
    'source_table': Column(column_types['string']),
    'hub_id': Column(column_types['integer'], ForeignKey(hub_object.id)),
    'display_text': Column(column_types['string'])}

    columns = [{'einzg': Column(column_types['varchar'])},{'fatnx': Column(column_types['varchar'])}]
    for column in columns:
        new_satellite.update(column)

    object_medical_center = type('FCRB_Sat_Object_Medical_Center',(base,),new_satellite)

    #
        
    new_satellite={'__tablename__':'sat_object_organisation_details',
    '__table_args__':{'schema':  schema},
    'id': Column(column_types['integer'], primary_key=True),
    'source_table': Column(column_types['string']),
    'hub_id': Column(column_types['integer'], ForeignKey(hub_object.id)),
    'display_text': Column(column_types['string'])}

    columns = [{'orgna': Column(column_types['varchar'])}]
    for column in columns:
        new_satellite.update(column)

    object_organisation_details = type('FCRB_Sat_Object_Organisation_Details',(base,),new_satellite)

    #
        
    new_satellite={'__tablename__':'sat_object_medication_details',
    '__table_args__':{'schema':  schema},
    'id': Column(column_types['integer'], primary_key=True),
    'source_table': Column(column_types['string']),
    'hub_id': Column(column_types['integer'], ForeignKey(hub_object.id)),
    'display_text': Column(column_types['string'])}

    columns = [{'motx': Column(column_types['varchar'])},{'mostx': Column(column_types['varchar'])},{'motypid': Column(column_types['varchar'])},{'mpresnr': Column(column_types['varchar'])},{'storn': Column(column_types['varchar'])},{'stusr': Column(column_types['varchar'])},{'stoid': Column(column_types['varchar'])}]
    for column in columns:
        new_satellite.update(column)

    object_medication_details = type('FCRB_Sat_Object_Medication_Details',(base,),new_satellite)

    #
        
    new_satellite={'__tablename__':'sat_time_medication_date',
    '__table_args__':{'schema':  schema},
    'id': Column(column_types['integer'], primary_key=True),
    'source_table': Column(column_types['string']),
    'hub_id': Column(column_types['integer'], ForeignKey(hub_time.id)),
    'display_text': Column(column_types['string'])}

    columns = [{'erdat': Column(column_types['datetime'])},{'stdat': Column(column_types['datetime'])}]
    for column in columns:
        new_satellite.update(column)

    time_medication_date = type('FCRB_Sat_Time_Medication_Date',(base,),new_satellite)

    #
        
    new_satellite={'__tablename__':'sat_object_monitoring_parameters',
    '__table_args__':{'schema':  schema},
    'id': Column(column_types['integer'], primary_key=True),
    'source_table': Column(column_types['string']),
    'hub_id': Column(column_types['integer'], ForeignKey(hub_object.id)),
    'display_text': Column(column_types['string'])}

    columns = [{'vbem': Column(column_types['varchar'])},{'datyp': Column(column_types['datetime'])},{'wertogr': Column(column_types['varchar'])},{'wertugr': Column(column_types['varchar'])},{'wertmax': Column(column_types['varchar'])},{'wertmin': Column(column_types['varchar'])}]
    for column in columns:
        new_satellite.update(column)

    object_monitoring_parameters = type('FCRB_Sat_Object_Monitoring_Parameters',(base,),new_satellite)

    #
        
    new_satellite={'__tablename__':'sat_object_order_entry',
    '__table_args__':{'schema':  schema},
    'id': Column(column_types['integer'], primary_key=True),
    'source_table': Column(column_types['string']),
    'hub_id': Column(column_types['integer'], ForeignKey(hub_object.id)),
    'display_text': Column(column_types['string'])}

    columns = [{'idodr': Column(column_types['string'])}]
    for column in columns:
        new_satellite.update(column)

    object_order_entry = type('FCRB_Sat_Object_Order_Entry',(base,),new_satellite)

    #
        
    new_satellite={'__tablename__':'sat_time_order_date',
    '__table_args__':{'schema':  schema},
    'id': Column(column_types['integer'], primary_key=True),
    'source_table': Column(column_types['string']),
    'hub_id': Column(column_types['integer'], ForeignKey(hub_time.id)),
    'display_text': Column(column_types['string'])}

    columns = [{'erdat': Column(column_types['datetime'])}]
    for column in columns:
        new_satellite.update(column)

    time_order_date = type('FCRB_Sat_Time_Order_Date',(base,),new_satellite)

    #
        
    new_satellite={'__tablename__':'sat_person_patient_details',
    '__table_args__':{'schema':  schema},
    'id': Column(column_types['integer'], primary_key=True),
    'source_table': Column(column_types['string']),
    'hub_id': Column(column_types['integer'], ForeignKey(hub_person.id)),
    'display_text': Column(column_types['string'])}

    columns = [{'gschl': Column(column_types['varchar'])},{'nname': Column(column_types['varchar'])},{'vname': Column(column_types['varchar'])},{'gbdat': Column(column_types['datetime'])},{'gbnam': Column(column_types['varchar'])},{'namzu': Column(column_types['varchar'])},{'glrand': Column(column_types['varchar'])},{'famst': Column(column_types['varchar'])},{'telf1': Column(column_types['varchar'])},{'rvnum': Column(column_types['varchar'])},{'decdat': Column(column_types['time'])}]
    for column in columns:
        new_satellite.update(column)

    person_patient_details = type('FCRB_Sat_Person_Patient_Details',(base,),new_satellite)

    #
        
    new_satellite={'__tablename__':'sat_location_patient_address',
    '__table_args__':{'schema':  schema},
    'id': Column(column_types['integer'], primary_key=True),
    'source_table': Column(column_types['string']),
    'hub_id': Column(column_types['integer'], ForeignKey(hub_location.id)),
    'display_text': Column(column_types['string'])}

    columns = [{'pstlz': Column(column_types['varchar'])},{'stras': Column(column_types['varchar'])},{'land': Column(column_types['varchar'])},{'ort': Column(column_types['varchar'])},{'floor': Column(column_types['varchar'])},{'adrnr': Column(column_types['varchar'])}]
    for column in columns:
        new_satellite.update(column)

    location_patient_address = type('FCRB_Sat_Location_Patient_Address',(base,),new_satellite)

    #
        
    new_satellite={'__tablename__':'sat_person_professional_details',
    '__table_args__':{'schema':  schema},
    'id': Column(column_types['integer'], primary_key=True),
    'source_table': Column(column_types['string']),
    'hub_id': Column(column_types['integer'], ForeignKey(hub_person.id)),
    'display_text': Column(column_types['string'])}

    columns = [{'erusr': Column(column_types['varchar'])},{'gbdat': Column(column_types['datetime'])},{'rank': Column(column_types['varchar'])}]
    for column in columns:
        new_satellite.update(column)

    person_professional_details = type('FCRB_Sat_Person_Professional_Details',(base,),new_satellite)

    #
        
    new_satellite={'__tablename__':'sat_time_professional_date',
    '__table_args__':{'schema':  schema},
    'id': Column(column_types['integer'], primary_key=True),
    'source_table': Column(column_types['string']),
    'hub_id': Column(column_types['integer'], ForeignKey(hub_time.id)),
    'display_text': Column(column_types['string'])}

    columns = [{'begdt': Column(column_types['datetime'])},{'enddt': Column(column_types['datetime'])},{'erdat': Column(column_types['datetime'])}]
    for column in columns:
        new_satellite.update(column)

    time_professional_date = type('FCRB_Sat_Time_Professional_Date',(base,),new_satellite)

    #
        
    new_satellite={'__tablename__':'sat_object_vital_signs',
    '__table_args__':{'schema':  schema},
    'id': Column(column_types['integer'], primary_key=True),
    'source_table': Column(column_types['string']),
    'hub_id': Column(column_types['integer'], ForeignKey(hub_object.id)),
    'display_text': Column(column_types['string'])}

    columns = [{'idvs': Column(column_types['varchar'])},{'dttyp': Column(column_types['varchar'])},{'typevs': Column(column_types['varchar'])},{'vwert': Column(column_types['varchar'])},{'vbem': Column(column_types['varchar'])}]
    for column in columns:
        new_satellite.update(column)

    object_vital_signs = type('FCRB_Sat_Object_Vital_Signs',(base,),new_satellite)

    #
        
    new_satellite={'__tablename__':'sat_time_vital_signs_date',
    '__table_args__':{'schema':  schema},
    'id': Column(column_types['integer'], primary_key=True),
    'source_table': Column(column_types['string']),
    'hub_id': Column(column_types['integer'], ForeignKey(hub_time.id)),
    'display_text': Column(column_types['string'])}

    columns = [{'erdat': Column(column_types['datetime'])},{'vptim': Column(column_types['time'])}]
    for column in columns:
        new_satellite.update(column)

    time_vital_signs_date = type('FCRB_Sat_Time_Vital_Signs_Date',(base,),new_satellite)

    #
        
    base.metadata.create_all(engine)
    print("FINISHED MAKING DATAVAULT")