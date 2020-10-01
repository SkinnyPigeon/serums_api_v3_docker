
fcrb_episode_hubs = {'table': 'fcrb.episode', 'hubs': [{'hub': 'hub_event', 'keys': ['einri', 'falnr', 'patnr', 'pernr']}, {'hub': 'hub_object', 'keys': ['einri', 'falnr', 'patnr', 'pernr']}]}

fcrb_episode_satellites = {'satellites': [{'satellite': 'sat_object_treatment_category', 'columns': ['bekat'], 'hub': 'hub_object', 'hub_id': 0}, {'satellite': 'sat_event_episode_type', 'columns': ['falar', 'statu', 'krzan', 'storn', 'casetx', 'enddtx'], 'hub': 'hub_event', 'hub_id': 0}, {'satellite': 'sat_object_medical_center', 'columns': ['einzg', 'fatnx'], 'hub': 'hub_object', 'hub_id': 0}]}

fcrb_episode_links = {'links': [{'link': 'object_event_link', 'values': {'object_id': 0, 'event_id': 0}}]}
    