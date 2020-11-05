
zmc_patient_warnings_hubs = {'table': 'zmc.patient_warnings', 'hubs': [{'hub': 'hub_object', 'keys': ['patnr']}, {'hub': 'hub_time', 'keys': ['patnr']}]}

zmc_patient_warnings_satellites = {
    'satellites': [
        {
            'satellite': 'sat_object_patient_warnings', 
            'columns': ['alerts', 'type'], 
            'hub': 'hub_object', 
            'hub_id': 0,
            'display_name': 'Warnings'
        }, 
        {
            'satellite': 'sat_time_patient_warnings', 
            'columns': ['begin_date'], 
            'hub': 'hub_time', 
            'hub_id': 0,
            'display_name': 'Warning Dates'
        }
    ]
}

zmc_patient_warnings_links = {'links': [{'link': 'object_time_link', 'values': {'object_id': 0, 'time_id': 0}}]}
