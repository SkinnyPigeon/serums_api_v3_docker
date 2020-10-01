
zmc_patient_diagnostic_hubs = {'table': 'zmc.patient_diagnostic', 'hubs': [{'hub': 'hub_object', 'keys': ['patnr']}, {'hub': 'hub_time', 'keys': ['patnr']}]}

zmc_patient_diagnostic_satellites = {'satellites': [{'satellite': 'sat_object_patient_diagnostic', 'columns': ['type', 'name', 'anatomical_location', 'laterality'], 'hub': 'hub_object', 'hub_id': 0}, {'satellite': 'sat_time_patient_diagnostic', 'columns': ['begin_date', 'end_date'], 'hub': 'hub_time', 'hub_id': 0}]}

zmc_patient_diagnostic_links = {'links': [{'link': 'object_time_link', 'values': {'object_id': 0, 'time_id': 0}}]}
