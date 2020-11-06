
fcrb_monitoring_parameters_hubs = {'table': 'fcrb.monitoring_parameters', 'hubs': [{'hub': 'hub_object', 'keys': ['patnr', 'falnr', 'vppid', 'pernr']}]}

fcrb_monitoring_parameters_satellites = {
    'satellites': [
        {
            'satellite': 'sat_object_monitoring_parameters', 
            'columns': ['vbem', 'datyp', 'wertogr', 'wertugr', 'wertmax', 'wertmin'], 
            'hub': 'hub_object', 'hub_id': 0,
            'display_text': 'Monitoring Parameters'
        }
    ]
}

fcrb_monitoring_parameters_links = {'links': []}
    