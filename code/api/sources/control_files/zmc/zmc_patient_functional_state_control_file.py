
zmc_patient_functional_state_hubs = {'table': 'zmc.patient_functional_state', 'hubs': [{'hub': 'hub_object', 'keys': ['patnr']}, {'hub': 'hub_time', 'keys': ['patnr']}]}

zmc_patient_functional_state_satellites = {'satellites': [{'satellite': 'sat_object_patient_functional_state', 'columns': ['name', 'value'], 'hub': 'hub_object', 'hub_id': 0}, {'satellite': 'sat_time_patient_functional_state', 'columns': ['date'], 'hub': 'hub_time', 'hub_id': 0}]}

zmc_patient_functional_state_links = {'links': [{'link': 'object_time_link', 'values': {'object_id': 0, 'time_id': 0}}]}
