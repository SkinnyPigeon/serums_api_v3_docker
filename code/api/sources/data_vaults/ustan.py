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

def create_ustan_dv(schema, base, engine):

    # HUBS
        
    hub_time={'__tablename__': 'hub_time',
    '__table_args__':{'schema': schema},
    'id': Column(column_types['integer'], primary_key=True)}

    keys = [{'chi': Column(Integer)}]
    for key in keys:
        hub_time.update(key)

    time = type('USTAN_Hub_Time',(base,),hub_time)
        
    hub_person={'__tablename__': 'hub_person',
    '__table_args__':{'schema': schema},
    'id': Column(column_types['integer'], primary_key=True)}

    keys = [{'chi': Column(Integer)}]
    for key in keys:
        hub_person.update(key)

    person = type('USTAN_Hub_Person',(base,),hub_person)
        
    hub_object={'__tablename__': 'hub_object',
    '__table_args__':{'schema': schema},
    'id': Column(column_types['integer'], primary_key=True)}

    keys = [{'chi': Column(Integer)}]
    for key in keys:
        hub_object.update(key)

    object = type('USTAN_Hub_Object',(base,),hub_object)
        
    hub_location={'__tablename__': 'hub_location',
    '__table_args__':{'schema': schema},
    'id': Column(column_types['integer'], primary_key=True)}

    keys = [{'chi': Column(Integer)}]
    for key in keys:
        hub_location.update(key)

    location = type('USTAN_Hub_Location',(base,),hub_location)
        
    hub_event={'__tablename__': 'hub_event',
    '__table_args__':{'schema': schema},
    'id': Column(column_types['integer'], primary_key=True)}

    keys = [{'chi': Column(Integer)}]
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
        
    new_satellite={'__tablename__':'sat_time_issue_date',
    '__table_args__':{'schema': schema},
    'id': Column(column_types['integer'], primary_key=True),
    'source_table': Column(column_types['string']),
    'hub_id': Column(column_types['integer'], ForeignKey(hub_time.id))}

    columns = [{'date1': Column(column_types['datetime'])}]
    for column in columns:
        new_satellite.update(column)

    time_issue_date = type('USTAN_Sat_Time_Issue_Date',(base,),new_satellite)

    #
        
    new_satellite={'__tablename__':'sat_object_treatment_side_effects',
    '__table_args__':{'schema': schema},
    'id': Column(column_types['integer'], primary_key=True),
    'source_table': Column(column_types['string']),
    'hub_id': Column(column_types['integer'], ForeignKey(hub_object.id))}

    columns = [{'nausea': Column(column_types['numeric'])},{'vomiting': Column(column_types['numeric'])},{'diarrhoea': Column(column_types['numeric'])},{'constipation': Column(column_types['numeric'])},{'oral_mucostis': Column(column_types['numeric'])},{'oesophasitis': Column(column_types['numeric'])},{'neurotoxicity': Column(column_types['numeric'])},{'hand_foot': Column(column_types['numeric'])},{'skin': Column(column_types['numeric'])},{'hypersensitivity': Column(column_types['numeric'])},{'fatigue': Column(column_types['numeric'])}]
    for column in columns:
        new_satellite.update(column)

    object_treatment_side_effects = type('USTAN_Sat_Object_Treatment_Side_Effects',(base,),new_satellite)

    #
        
    new_satellite={'__tablename__':'sat_event_performance_status',
    '__table_args__':{'schema': schema},
    'id': Column(column_types['integer'], primary_key=True),
    'source_table': Column(column_types['string']),
    'hub_id': Column(column_types['integer'], ForeignKey(hub_event.id))}

    columns = [{'performance_status': Column(column_types['numeric'])}]
    for column in columns:
        new_satellite.update(column)

    event_performance_status = type('USTAN_Sat_Event_Performance_Status',(base,),new_satellite)

    #
        
    new_satellite={'__tablename__':'sat_object_last_visit',
    '__table_args__':{'schema': schema},
    'id': Column(column_types['integer'], primary_key=True),
    'source_table': Column(column_types['string']),
    'hub_id': Column(column_types['integer'], ForeignKey(hub_object.id))}

    columns = [{'issues_since_last_visit': Column(column_types['numeric'])},{'last_visit_issue_description': Column(column_types['varchar'])}]
    for column in columns:
        new_satellite.update(column)

    object_last_visit = type('USTAN_Sat_Object_Last_Visit',(base,),new_satellite)

    #
        
    new_satellite={'__tablename__':'sat_time_appointment_date',
    '__table_args__':{'schema': schema},
    'id': Column(column_types['integer'], primary_key=True),
    'source_table': Column(column_types['string']),
    'hub_id': Column(column_types['integer'], ForeignKey(hub_time.id))}

    columns = [{'appointment_date': Column(column_types['datetime'])}]
    for column in columns:
        new_satellite.update(column)

    time_appointment_date = type('USTAN_Sat_Time_Appointment_Date',(base,),new_satellite)

    #
        
    new_satellite={'__tablename__':'sat_time_last_toxicity_date',
    '__table_args__':{'schema': schema},
    'id': Column(column_types['integer'], primary_key=True),
    'source_table': Column(column_types['string']),
    'hub_id': Column(column_types['integer'], ForeignKey(hub_time.id))}

    columns = [{'last_toxicity_date': Column(column_types['datetime'])}]
    for column in columns:
        new_satellite.update(column)

    time_last_toxicity_date = type('USTAN_Sat_Time_Last_Toxicity_Date',(base,),new_satellite)

    #
        
    new_satellite={'__tablename__':'sat_object_tumour_group',
    '__table_args__':{'schema': schema},
    'id': Column(column_types['integer'], primary_key=True),
    'source_table': Column(column_types['string']),
    'hub_id': Column(column_types['integer'], ForeignKey(hub_object.id))}

    columns = [{'tumour_group': Column(column_types['varchar'])}]
    for column in columns:
        new_satellite.update(column)

    object_tumour_group = type('USTAN_Sat_Object_Tumour_Group',(base,),new_satellite)

    #
        
    new_satellite={'__tablename__':'sat_person_patient_measurements',
    '__table_args__':{'schema': schema},
    'id': Column(column_types['integer'], primary_key=True),
    'source_table': Column(column_types['string']),
    'hub_id': Column(column_types['integer'], ForeignKey(hub_person.id))}

    columns = [{'age_at_diagnosis': Column(column_types['numeric'])},{'height': Column(column_types['numeric'])},{'weight': Column(column_types['numeric'])},{'surface_area': Column(column_types['numeric'])}]
    for column in columns:
        new_satellite.update(column)

    person_patient_measurements = type('USTAN_Sat_Person_Patient_Measurements',(base,),new_satellite)

    #
        
    new_satellite={'__tablename__':'sat_person_patient_type',
    '__table_args__':{'schema': schema},
    'id': Column(column_types['integer'], primary_key=True),
    'source_table': Column(column_types['string']),
    'hub_id': Column(column_types['integer'], ForeignKey(hub_person.id))}

    columns = [{'patient_type': Column(column_types['varchar'])}]
    for column in columns:
        new_satellite.update(column)

    person_patient_type = type('USTAN_Sat_Person_Patient_Type',(base,),new_satellite)

    #
        
    new_satellite={'__tablename__':'sat_person_consultant_code',
    '__table_args__':{'schema': schema},
    'id': Column(column_types['integer'], primary_key=True),
    'source_table': Column(column_types['string']),
    'hub_id': Column(column_types['integer'], ForeignKey(hub_person.id))}

    columns = [{'consultant_code': Column(column_types['varchar'])}]
    for column in columns:
        new_satellite.update(column)

    person_consultant_code = type('USTAN_Sat_Person_Consultant_Code',(base,),new_satellite)

    #
        
    new_satellite={'__tablename__':'sat_object_treatment_details',
    '__table_args__':{'schema': schema},
    'id': Column(column_types['integer'], primary_key=True),
    'source_table': Column(column_types['string']),
    'hub_id': Column(column_types['integer'], ForeignKey(hub_object.id))}

    columns = [{'intention': Column(column_types['varchar'])},{'regime_code': Column(column_types['varchar'])},{'cycle': Column(column_types['integer'])},{'cycle_id': Column(column_types['integer'])}]
    for column in columns:
        new_satellite.update(column)

    object_treatment_details = type('USTAN_Sat_Object_Treatment_Details',(base,),new_satellite)

    #
        
    new_satellite={'__tablename__':'sat_object_drug_details',
    '__table_args__':{'schema': schema},
    'id': Column(column_types['integer'], primary_key=True),
    'source_table': Column(column_types['string']),
    'hub_id': Column(column_types['integer'], ForeignKey(hub_object.id))}

    columns = [{'drug_type': Column(column_types['varchar'])},{'drug_name': Column(column_types['varchar'])},{'required_dose': Column(column_types['numeric'])},{'drug_status': Column(column_types['varchar'])}]
    for column in columns:
        new_satellite.update(column)

    object_drug_details = type('USTAN_Sat_Object_Drug_Details',(base,),new_satellite)

    #
        
    new_satellite={'__tablename__':'sat_person_demographic_data',
    '__table_args__':{'schema': schema},
    'id': Column(column_types['integer'], primary_key=True),
    'source_table': Column(column_types['string']),
    'hub_id': Column(column_types['integer'], ForeignKey(hub_person.id))}

    columns = [{'postcode': Column(column_types['varchar'])},{'simd': Column(column_types['integer'])},{'simd1': Column(column_types['integer'])}]
    for column in columns:
        new_satellite.update(column)

    person_demographic_data = type('USTAN_Sat_Person_Demographic_Data',(base,),new_satellite)

    #
        
    new_satellite={'__tablename__':'sat_time_incidence_year',
    '__table_args__':{'schema': schema},
    'id': Column(column_types['integer'], primary_key=True),
    'source_table': Column(column_types['string']),
    'hub_id': Column(column_types['integer'], ForeignKey(hub_time.id))}

    columns = [{'incidence_year': Column(column_types['integer'])}]
    for column in columns:
        new_satellite.update(column)

    time_incidence_year = type('USTAN_Sat_Time_Incidence_Year',(base,),new_satellite)

    #
        
    new_satellite={'__tablename__':'sat_object_condition_flags',
    '__table_args__':{'schema': schema},
    'id': Column(column_types['integer'], primary_key=True),
    'source_table': Column(column_types['string']),
    'hub_id': Column(column_types['integer'], ForeignKey(hub_object.id))}

    columns = [{'conf_heart_fail_flag': Column(column_types['integer'])},{'dementia_flag': Column(column_types['integer'])},{'pulmonary_flag': Column(column_types['integer'])},{'con_tiss_disease_flag': Column(column_types['integer'])},{'diabetes_flag': Column(column_types['integer'])},{'para_hemiplegia_flag': Column(column_types['integer'])},{'renal_flag': Column(column_types['integer'])},{'liver_flag': Column(column_types['integer'])},{'aids_hiv_flag': Column(column_types['integer'])}]
    for column in columns:
        new_satellite.update(column)

    object_condition_flags = type('USTAN_Sat_Object_Condition_Flags',(base,),new_satellite)

    #
        
    new_satellite={'__tablename__':'sat_object_quan_score',
    '__table_args__':{'schema': schema},
    'id': Column(column_types['integer'], primary_key=True),
    'source_table': Column(column_types['string']),
    'hub_id': Column(column_types['integer'], ForeignKey(hub_object.id))}

    columns = [{'charlson_quan_score': Column(column_types['integer'])}]
    for column in columns:
        new_satellite.update(column)

    object_quan_score = type('USTAN_Sat_Object_Quan_Score',(base,),new_satellite)

    #
        
    new_satellite={'__tablename__':'sat_time_admissions_date',
    '__table_args__':{'schema': schema},
    'id': Column(column_types['integer'], primary_key=True),
    'source_table': Column(column_types['string']),
    'hub_id': Column(column_types['integer'], ForeignKey(hub_time.id))}

    columns = [{'admission_date': Column(column_types['datetime'])},{'discharge_date': Column(column_types['integer'])},{'length_of_stay': Column(column_types['integer'])}]
    for column in columns:
        new_satellite.update(column)

    time_admissions_date = type('USTAN_Sat_Time_Admissions_Date',(base,),new_satellite)

    #
        
    new_satellite={'__tablename__':'sat_person_patient_details',
    '__table_args__':{'schema': schema},
    'id': Column(column_types['integer'], primary_key=True),
    'source_table': Column(column_types['string']),
    'hub_id': Column(column_types['integer'], ForeignKey(hub_person.id))}

    columns = [{'sex': Column(column_types['integer'])},{'age_in_years': Column(column_types['integer'])},{'ethnic_group': Column(column_types['varchar'])},{'marital_status': Column(column_types['varchar'])},{'postcode': Column(column_types['varchar'])},{'age_at_diagnosis': Column(column_types['numeric'])},{'height': Column(column_types['numeric'])},{'weight': Column(column_types['numeric'])}]
    for column in columns:
        new_satellite.update(column)

    person_patient_details = type('USTAN_Sat_Person_Patient_Details',(base,),new_satellite)

    #
        
    new_satellite={'__tablename__':'sat_object_conditions_details',
    '__table_args__':{'schema': schema},
    'id': Column(column_types['integer'], primary_key=True),
    'source_table': Column(column_types['string']),
    'hub_id': Column(column_types['integer'], ForeignKey(hub_object.id))}

    columns = [{'main_condition': Column(column_types['varchar'])},{'other_condition_1': Column(column_types['varchar'])},{'other_condition_2': Column(column_types['varchar'])},{'other_condition_3': Column(column_types['varchar'])},{'other_condition_4': Column(column_types['varchar'])}]
    for column in columns:
        new_satellite.update(column)

    object_conditions_details = type('USTAN_Sat_Object_Conditions_Details',(base,),new_satellite)

    #
        
    new_satellite={'__tablename__':'sat_object_operations_details',
    '__table_args__':{'schema': schema},
    'id': Column(column_types['integer'], primary_key=True),
    'source_table': Column(column_types['string']),
    'hub_id': Column(column_types['integer'], ForeignKey(hub_object.id))}

    columns = [{'main_operation_a': Column(column_types['varchar'])},{'main_operation_b': Column(column_types['varchar'])}]
    for column in columns:
        new_satellite.update(column)

    object_operations_details = type('USTAN_Sat_Object_Operations_Details',(base,),new_satellite)

    #
        
    new_satellite={'__tablename__':'sat_time_incidence_date',
    '__table_args__':{'schema': schema},
    'id': Column(column_types['integer'], primary_key=True),
    'source_table': Column(column_types['string']),
    'hub_id': Column(column_types['integer'], ForeignKey(hub_time.id))}

    columns = [{'incidence_date': Column(column_types['datetime'])}]
    for column in columns:
        new_satellite.update(column)

    time_incidence_date = type('USTAN_Sat_Time_Incidence_Date',(base,),new_satellite)

    #
        
    new_satellite={'__tablename__':'sat_location_tumour_site',
    '__table_args__':{'schema': schema},
    'id': Column(column_types['integer'], primary_key=True),
    'source_table': Column(column_types['string']),
    'hub_id': Column(column_types['integer'], ForeignKey(hub_location.id))}

    columns = [{'tumour_site_icd10': Column(column_types['varchar'])}]
    for column in columns:
        new_satellite.update(column)

    location_tumour_site = type('USTAN_Sat_Location_Tumour_Site',(base,),new_satellite)

    #
        
    new_satellite={'__tablename__':'sat_object_status_codes',
    '__table_args__':{'schema': schema},
    'id': Column(column_types['integer'], primary_key=True),
    'source_table': Column(column_types['string']),
    'hub_id': Column(column_types['integer'], ForeignKey(hub_object.id))}

    columns = [{'oestrogen_receptor_er_status': Column(column_types['integer'])},{'her2_status_code': Column(column_types['integer'])},{'stage_clinical_t_code': Column(column_types['varchar'])},{'stage_clinical_n_code': Column(column_types['varchar'])},{'stage_clinical_m_code': Column(column_types['varchar'])}]
    for column in columns:
        new_satellite.update(column)

    object_status_codes = type('USTAN_Sat_Object_Status_Codes',(base,),new_satellite)

    #
        
    new_satellite={'__tablename__':'sat_object_tumour_size',
    '__table_args__':{'schema': schema},
    'id': Column(column_types['integer'], primary_key=True),
    'source_table': Column(column_types['string']),
    'hub_id': Column(column_types['integer'], ForeignKey(hub_object.id))}

    columns = [{'pathological_tumour_size': Column(column_types['integer'])}]
    for column in columns:
        new_satellite.update(column)

    object_tumour_size = type('USTAN_Sat_Object_Tumour_Size',(base,),new_satellite)

    #
        
    base.metadata.create_all(engine)
    