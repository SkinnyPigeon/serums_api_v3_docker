
ustan_chemocare_toxicity_hubs = {'table': 'ustan.chemocare_toxicity', 'hubs': [{'hub': 'hub_time', 'keys': ['chi']}, {'hub': 'hub_event', 'keys': ['chi']}, {'hub': 'hub_object', 'keys': ['chi']}]}

ustan_chemocare_toxicity_satellites = {'satellites': [{'satellite': 'sat_time_issue_date', 'columns': ['date1'], 'hub': 'hub_time', 'hub_id': 0}, {'satellite': 'sat_object_treatment_side_effects', 'columns': ['nausea', 'vomiting', 'diarrhoea', 'constipation', 'oral_mucostis', 'oesophasitis', 'neurotoxicity', 'hand_foot', 'skin', 'hypersensitivity', 'fatigue'], 'hub': 'hub_object', 'hub_id': 0}, {'satellite': 'sat_event_performance_status', 'columns': ['performance_status'], 'hub': 'hub_event', 'hub_id': 0}, {'satellite': 'sat_object_last_visit', 'columns': ['issues_since_last_visit', 'last_visit_issue_description'], 'hub': 'hub_object', 'hub_id': 0}]}

ustan_chemocare_toxicity_links = {'links': [{'link': 'object_time_link', 'values': {'object_id': 0, 'time_id': 0}}, {'link': 'time_event_link', 'values': {'time_id': 0, 'event_id': 0}}, {'link': 'object_event_link', 'values': {'object_id': 0, 'event_id': 0}}]}
    