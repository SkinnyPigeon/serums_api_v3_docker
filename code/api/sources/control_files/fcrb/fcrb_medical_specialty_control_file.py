
fcrb_medical_specialty_hubs = {'table': 'fcrb.medical_specialty', 'hubs': [{'hub': 'hub_object', 'keys': ['orgid']}],'key_lookup': [{'table': 'fcrb.order_entry', 'keys': ['patnr']}]}

fcrb_medical_specialty_satellites = {
    'satellites': [
        {
            'satellite': 'sat_object_organisation_details', 
            'columns': ['orgna'], 
            'hub': 'hub_object', 
            'hub_id': 0,
            'display_name': 'Organisation Details'
        }
    ]
}

fcrb_medical_specialty_links = {'links': []}
    