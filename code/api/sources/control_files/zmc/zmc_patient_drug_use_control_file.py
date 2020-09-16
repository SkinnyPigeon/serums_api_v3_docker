
zmc_patient_drug_use_hubs = {'table': 'zmc.patient_drug_use', 'hubs': [{'hub': 'hub_object', 'keys': ['patnr']}]}

zmc_patient_drug_use_satellites = {'satellites': [{'satellite': 'sat_object_patient_drug_use', 'columns': ['substance', 'quantity', 'description'], 'hub': 'hub_object', 'hub_id': 0}]}

zmc_patient_drug_use_links = {'links': []}
