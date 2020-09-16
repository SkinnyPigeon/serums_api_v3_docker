
zmc_patient_operations_hubs = {'table': 'zmc.patient_opperations', 'hubs': [{'hub': 'hub_event', 'keys': ['patnr']}]}

zmc_patient_operations_satellites = {'satellites': [{'satellite': 'sat_event_patient_operations', 'columns': ['anatomical_location', 'date', 'notes'], 'hub': 'hub_event', 'hub_id': 0}]}

zmc_patient_operations_links = {'links': []}
    