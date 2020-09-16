
ustan_ndc_charlson_hubs = {'table': 'ustan.ndc_charlson', 'hubs': [{'hub': 'hub_person', 'keys': ['chi']}, {'hub': 'hub_time', 'keys': ['chi']}, {'hub': 'hub_object', 'keys': ['chi']}]}

ustan_ndc_charlson_satellites = {'satellites': [{'satellite': 'sat_person_demographic_data', 'columns': ['postcode', 'simd', 'simd1'], 'hub': 'hub_person', 'hub_id': 0}, {'satellite': 'sat_time_incidence_year', 'columns': ['incidence_year'], 'hub': 'hub_time', 'hub_id': 0}, {'satellite': 'sat_object_condition_flags', 'columns': ['conf_heart_fail_flag', 'dementia_flag', 'pulmonary_flag', 'con_tiss_disease_flag', 'diabetes_flag', 'para_hemiplegia_flag', 'renal_flag', 'liver_flag', 'aids_hiv_flag'], 'hub': 'hub_object', 'hub_id': 0}, {'satellite': 'sat_object_quan_score', 'columns': ['charlson_quan_score'], 'hub': 'hub_object', 'hub_id': 0}]}

ustan_ndc_charlson_links = {'links': [{'link': 'person_time_link', 'values': {'person_id': 0, 'time_id': 0}}, {'link': 'person_object_link', 'values': {'person_id': 0, 'object_id': 0}}, {'link': 'object_time_link', 'values': {'object_id': 0, 'time_id': 0}}]}
    