
zmc_patient_alcohol_use_hubs = {'table': 'zmc.patient_alcohol_use', 'hubs': [{'hub': 'hub_object', 'keys': ['patnr']}]}

zmc_patient_alcohol_use_satellites = {
    'satellites': [
        {
            'satellite': 'sat_object_patient_alcohol_use', 
            'columns': ['usage_status', 'quantity', 'description'], 
            'hub': 'hub_object', 
            'hub_id': 0,
            'display_text': 'Alcoholgebruik'
        }
    ]
}

zmc_patient_alcohol_use_links = {'links': []}
