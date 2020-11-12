
zmc_patient_measurements_hubs = {'table': 'zmc.patient_measurements', 'hubs': [{'hub': 'hub_person', 'keys': ['patnr']}]}

zmc_patient_measurements_satellites = {
    'satellites': [
        {
            'satellite': 'sat_person_patient_measurements', 
            'columns': ['height', 'weight', 'date'], 
            'hub': 'hub_person', 
            'hub_id': 0,
            'display_text': 'Meetgegevens van de patiënt'
        }
    ]
}

zmc_patient_measurements_links = {'links': []}
    