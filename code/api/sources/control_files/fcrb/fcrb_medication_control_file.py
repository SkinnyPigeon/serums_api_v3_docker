
fcrb_medication_hubs = {'table': 'fcrb.medication', 'hubs': [{'hub': 'hub_object', 'keys': ['einri', 'patnr', 'falnr', 'pernr']}, {'hub': 'hub_time', 'keys': ['einri', 'patnr', 'falnr', 'pernr']}]}

fcrb_medication_satellites = {
    'satellites': [
        {
            'satellite': 'sat_object_medication_details', 
            'columns': ['motx', 'mostx', 'motypid', 'mpresnr', 'storn', 'stusr', 'stoid'], 
            'hub': 'hub_object', 'hub_id': 0,
            'display_name': 'Medication Details'
        }, 
        {
            'satellite': 'sat_time_medication_date', 
            'columns': ['erdat', 'stdat'], 
            'hub': 'hub_time', 'hub_id': 0,
            'display_name': 'Medication Dates'
        }
    ]
}

fcrb_medication_links = {'links': [{'link': 'object_time_link', 'values': {'object_id': 0, 'time_id': 0}}]}
    