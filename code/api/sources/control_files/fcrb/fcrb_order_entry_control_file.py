
fcrb_order_entry_hubs = {'table': 'fcrb.order_entry', 'hubs': [{'hub': 'hub_object', 'keys': ['einri', 'falnr', 'patnr', 'orgid', 'pernr']}, {'hub': 'hub_time', 'keys': ['einri', 'falnr', 'patnr', 'pernr', 'orgid']}]}

fcrb_order_entry_satellites = {'satellites': [{'satellite': 'sat_object_order_entry', 'columns': ['idodr'], 'hub': 'hub_object', 'hub_id': 0}, {'satellite': 'sat_time_order_date', 'columns': ['erdat'], 'hub': 'hub_time', 'hub_id': 0}]}

fcrb_order_entry_links = {'links': [{'link': 'object_time_link', 'values': {'object_id': 0, 'time_id': 0}}]}
    