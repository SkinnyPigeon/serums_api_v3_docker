
fcrb_vital_signs_hubs = {'table': 'fcrb.vital_signs', 'hubs': [{'hub': 'hub_object', 'keys': ['patnr', 'falnr', 'vppid']}, {'hub': 'hub_time', 'keys': ['patnr', 'falnr', 'vppid']}]}

fcrb_vital_signs_satellites = {'satellites': [{'satellite': 'sat_object_vital_signs', 'columns': ['idvs', 'dttyp', 'typevs', 'vwert', 'vbem'], 'hub': 'hub_object', 'hub_id': 0}, {'satellite': 'sat_time_vital_signs_date', 'columns': ['erdat', 'vptim'], 'hub': 'hub_time', 'hub_id': 0}]}

fcrb_vital_signs_links = {'links': [{'link': 'object_time_link', 'values': {'object_id': 0, 'time_id': 0}}]}
    