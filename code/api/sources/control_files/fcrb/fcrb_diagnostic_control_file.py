
fcrb_diagnostic_hubs = {'table': 'fcrb.diagnostic', 'hubs': [{'hub': 'hub_object', 'keys': ['einri', 'patnr', 'falnr', 'pernr']}]}

fcrb_diagnostic_satellites = {
    'satellites': [
        {
            'satellite': 'sat_object_diagnostic_details', 
            'columns': ['lfdnr', 'dkey1'], 
            'hub': 'hub_object', 'hub_id': 0,
            'display_text': 'Diagnostic Details'
        }
    ]
}

fcrb_diagnostic_links = {'links': []}
    