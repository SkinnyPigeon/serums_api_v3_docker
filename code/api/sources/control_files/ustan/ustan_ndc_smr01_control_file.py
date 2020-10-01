
ustan_ndc_smr01_hubs = {'table': 'ustan.ndc_smr01', 'hubs': [{'hub': 'hub_time', 'keys': ['chi']}, {'hub': 'hub_person', 'keys': ['chi']}, {'hub': 'hub_object', 'keys': ['chi']}]}

ustan_ndc_smr01_satellites = {'satellites': [{'satellite': 'sat_time_admissions_date', 'columns': ['admission_date', 'discharge_date', 'length_of_stay'], 'hub': 'hub_time', 'hub_id': 0}, {'satellite': 'sat_person_patient_details', 'columns': ['sex', 'age_in_years', 'ethnic_group', 'marital_status', 'postcode', 'age_at_diagnosis', 'height', 'weight'], 'hub': 'hub_person', 'hub_id': 0}, {'satellite': 'sat_object_conditions_details', 'columns': ['main_condition', 'other_condition_1', 'other_condition_2', 'other_condition_3', 'other_condition_4'], 'hub': 'hub_object', 'hub_id': 0}, {'satellite': 'sat_object_operations_details', 'columns': ['main_operation_a', 'main_operation_b'], 'hub': 'hub_object', 'hub_id': 0}]}

ustan_ndc_smr01_links = {'links': [{'link': 'person_time_link', 'values': {'person_id': 0, 'time_id': 0}}, {'link': 'object_time_link', 'values': {'object_id': 0, 'time_id': 0}}, {'link': 'person_object_link', 'values': {'person_id': 0, 'object_id': 0}}]}
    