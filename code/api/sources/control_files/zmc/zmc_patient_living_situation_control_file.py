
zmc_patient_living_situation_hubs = {'table': 'zmc.patient_living_situation', 'hubs': [{'hub': 'hub_object', 'keys': ['patnr']}]}

zmc_patient_living_situation_satellites = {
    'satellites': [
        {
            'satellite': 'sat_object_patient_living_situation', 
            'columns': ['house_type', 'description'], 
            'hub': 'hub_object', 
            'hub_id': 0,
            'display_text': 'Living Situation'
        }
    ]
}

zmc_patient_living_situation_links = {'links': []}
    