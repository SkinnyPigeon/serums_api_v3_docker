
ustan_chemocare_hubs = {
    'table': 'ustan.chemocare', 
    'hubs': [
        {'hub': 'hub_time', 'keys': ['chi']}, 
        {'hub': 'hub_object', 'keys': ['chi']}, 
        {'hub': 'hub_event', 'keys': ['chi']}
    ]
}

ustan_chemocare_satellites = {
    'satellites': [
        {
            'satellite': 'sat_time_chemocare_dates', 
            'columns': ['appointment_date'], 'hub': 'hub_time', 'hub_id': 0
        }, 
        {
            'satellite': 'sat_event_chemocare_treatment', 
            'columns': ['intention', 'regime', 'outcome'], 'hub': 'hub_event', 'hub_id': 0
        }, 
        {
            'satellite': 'sat_object_drug_details', 
            'columns': ['drug_dose', 'drug_type', 'drug_type'], 'hub': 'hub_object', 'hub_id': 0
        }
    ]
}

ustan_chemocare_links = {'links': 
    [
        {
            'link': 'object_time_link', 'values': {'object_id': 0, 'time_id': 0}
        },
        {
            'link': 'object_event_link', 'values': {'object_id': 0, 'event_id': 0}
        },
        {
            'link': 'time_event_link', 'values': {'time_id': 0, 'event_id': 0}
        }
    ]
}
    