
zmc_patient_appointments_hubs = {'table': 'zmc.patient_appointments', 'hubs': [{'hub': 'hub_event', 'keys': ['patnr']}]}

zmc_patient_appointments_satellites = {'satellites': [{'satellite': 'sat_event_patient_appointments', 'columns': ['type', 'date', 'notes'], 'hub': 'hub_event', 'hub_id': 0}]}

zmc_patient_appointments_links = {'links': []}
    