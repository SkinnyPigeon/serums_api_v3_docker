
ustan_smr01_hubs = {
    'table': 'ustan.smr01', 
    'hubs': [
        {'hub': 'hub_time', 'keys': ['chi']},
        {'hub': 'hub_person', 'keys': ['chi']},
        {'hub': 'hub_object', 'keys': ['chi']}
    ]
}

ustan_smr01_satellites = {
    'satellites': [
        {
            'satellite': 'sat_time_care_dates', 
            'columns': ['incidence_date',' admission_date', 'length_of_stay', 'discharge_date'], 
            'hub': 'hub_time', 'hub_id': 0
        },
        {
            'satellite': 'sat_object_condition_details', 
            'columns': ['main_condition', 'other_condition1', 'other_condition2', 'other_condition3'], 
            'hub': 'hub_object', 'hub_id': 0
        },
        {
            'satellite': 'sat_object_operation_details', 
            'columns': ['main_operation_a', 'main_operation_b'], 
            'hub': 'hub_object', 'hub_id': 0
        },
        {
            'satellite': 'sat_person_care_details', 
            'columns': ['waiting_list_type', 'marital_status', 'ethnic_group'], 
            'hub': 'hub_person', 'hub_id': 0
        }
    ]
}

ustan_smr01_links = {
    'links': [
        {
            'link': 'person_time_link', 'values': {'person_id': 0, 'time_id': 0}
        },
        {
            'link': 'person_object_link', 'values': {'person_id': 0, 'object_id': 0}
        },
        {
            'link': 'object_time_link', 'values': {'object_id': 0, 'time_id': 0}
        },
    ]
}
    