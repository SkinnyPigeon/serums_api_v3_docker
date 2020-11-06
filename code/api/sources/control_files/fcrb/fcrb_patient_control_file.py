
fcrb_patient_hubs = {'table': 'fcrb.patient', 'hubs': [{'hub': 'hub_person', 'keys': ['patnr']}]}

fcrb_patient_satellites = {
    'satellites': [
        {
            'satellite': 'sat_person_patient_details', 
            'columns': ['gschl', 'nname', 'vname', 'gbdat', 'gbnam', 'namzu', 'glrand', 'famst', 'telf1', 'rvnum', 'decdat'], 
            'hub': 'hub_person', 'hub_id': 0,
            'display_text': 'Patient Details'
        }
    ]
}

fcrb_patient_links = {'links': []}
