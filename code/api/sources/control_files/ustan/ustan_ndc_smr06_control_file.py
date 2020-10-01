
ustan_ndc_smr06_hubs = {'table': 'ustan.ndc_smr06', 'hubs': [{'hub': 'hub_time', 'keys': ['chi']}, {'hub': 'hub_location', 'keys': ['chi']}, {'hub': 'hub_object', 'keys': ['chi']}]}

ustan_ndc_smr06_satellites = {'satellites': [{'satellite': 'sat_time_incidence_date', 'columns': ['incidence_date'], 'hub': 'hub_time', 'hub_id': 0}, {'satellite': 'sat_location_tumour_site', 'columns': ['tumour_site_icd10'], 'hub': 'hub_location', 'hub_id': 0}, {'satellite': 'sat_object_status_codes', 'columns': ['oestrogen_receptor_er_status', 'her2_status_code', 'stage_clinical_t_code', 'stage_clinical_n_code', 'stage_clinical_m_code'], 'hub': 'hub_object', 'hub_id': 0}, {'satellite': 'sat_object_tumour_size', 'columns': ['pathological_tumour_size'], 'hub': 'hub_object', 'hub_id': 0}]}

ustan_ndc_smr06_links = {'links': [{'link': 'object_time_link', 'values': {'object_id': 0, 'time_id': 0}}, {'link': 'time_location_link', 'values': {'time_id': 0, 'location_id': 0}}, {'link': 'object_location_link', 'values': {'object_id': 0, 'location_id': 0}}]}
    