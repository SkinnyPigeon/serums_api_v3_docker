
fcrb_patient_address_hubs = {'table': 'fcrb.patient_address', 'hubs': [{'hub': 'hub_location', 'keys': ['patnr']}]}

fcrb_patient_address_satellites = {
    'satellites': [
        {
            'satellite': 'sat_location_patient_address', 
            'columns': ['pstlz', 'stras', 'land', 'ort', 'floor', 'adrnr'], 
            'hub': 'hub_location', 'hub_id': 0,
            'display_text': 'Patient Address'
        }
    ]
}

fcrb_patient_address_links = {'links': []}
    