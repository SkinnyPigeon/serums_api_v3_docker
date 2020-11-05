
zmc_patient_details_hubs = {'table': 'zmc.patient_details', 'hubs': [{'hub': 'hub_person', 'keys': ['patnr']}, {'hub': 'hub_location', 'keys': ['patnr']}]}

zmc_patient_details_satellites = {
    'satellites': [
        {
            'satellite': 'sat_person_patient_details', 
            'columns': ['gschl', 'nname', 'nnams', 'vname', 'titel', 'namzu', 'gbdat', 'gbnam', 'gbnas', 'gland', 'natio', 'land', 'telf1'], 
            'hub': 'hub_person', 
            'hub_id': 0,
            'display_name': 'Patient Details'
        }, 
        {
            'satellite': 'sat_location_patient_address', 
            'columns': ['pstlz', 'ort', 'stras'], 
            'hub': 'hub_location', 
            'hub_id': 0,
            'display_name': 'Patient Address'
        }
    ]
}

zmc_patient_details_links = {'links': [{'link': 'person_location_link', 'values': {'person_id': 0, 'location_id': 0}}]}
    