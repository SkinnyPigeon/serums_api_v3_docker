
fcrb_professional_hubs = {'table': 'fcrb.professional', 'hubs': [{'hub': 'hub_person', 'keys': ['pernr', 'orgid']}, {'hub': 'hub_time', 'keys': ['pernr', 'orgid']}]}

fcrb_professional_satellites = {
    'satellites': [
        {
            'satellite': 'sat_person_professional_details', 
            'columns': ['erusr', 'gbdat', 'rank'], 
            'hub': 'hub_person', 
            'hub_id': 0,
            'display_text': 'Detalls Professional'
        }, 
        {
            'satellite': 'sat_time_professional_date', 
            'columns': ['begdt', 'enddt', 'erdat'], 
            'hub': 'hub_time', 
            'hub_id': 0,
            'display_text': 'Dates Professional'
        }
    ]
}

fcrb_professional_links = {'links': [{'link': 'person_time_link', 'values': {'person_id': 0, 'time_id': 0}}]}
    