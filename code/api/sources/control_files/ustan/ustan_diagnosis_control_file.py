
ustan_diagnosis_hubs = {
    'table': 'ustan.diagnosis', 
    'hubs': [
        {'hub': 'hub_time', 'keys': ['chi']},
        {'hub': 'hub_event', 'keys': ['chi']}
    ]
}

ustan_diagnosis_satellites = {
    'satellites': [
        {
            'satellite': 'sat_time_diagnosis_dates', 
            'columns': ['first_seen_date'], 'hub': 'hub_time', 'hub_id': 0
        },
        {
            'satellite': 'sat_event_diagnosis_details', 
            'columns': ['"primary"', 'age' ,'site', 'side', 'histology', 'stage', 'tnm_t', 'tnm_n', 'tnm_m', 'perf_stat', 'metastasis1'], 'hub': 'hub_event', 'hub_id': 0
        }
    ]
}

ustan_diagnosis_links = {
    'links': [
        {
            'link': 'time_event_link', 'values': {'time_id': 0, 'event_id': 0}
        }
    ]
}
    