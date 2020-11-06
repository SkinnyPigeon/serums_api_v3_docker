
zmc_patient_tobacco_use_hubs = {'table': 'zmc.patient_tobacco_use', 'hubs': [{'hub': 'hub_object', 'keys': ['patnr']}]}

zmc_patient_tobacco_use_satellites = {
    'satellites': [
        {
            'satellite': 'sat_object_patient_tobacco_use', 
            'columns': ['substance', 'description'], 
            'hub': 'hub_object', 
            'hub_id': 0,
            'display_text': 'Tobacco Use'
        }
    ]
}

zmc_patient_tobacco_use_links = {'links': []}
