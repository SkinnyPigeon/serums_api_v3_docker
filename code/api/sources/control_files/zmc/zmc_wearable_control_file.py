
zmc_wearable_hubs = {'table': 'zmc.wearable', 'hubs': [{'hub': 'hub_event', 'keys': ['patnr']}, {'hub': 'hub_time', 'keys': ['patnr']}]}

zmc_wearable_satellites = {'satellites': [{'satellite': 'sat_event_exercise_measurements', 'columns': ['nr_sst', 'steps_total', 'cadence', 'cyc_rot', 'cyc_rpm'], 'hub': 'hub_event', 'hub_id': 0}, {'satellite': 'sat_time_exercise_measurements', 'columns': ['day_nr', 'time_total', 'time_passive', 'time_active', 'time_sit', 'time_stand', 'time_walk', 'time_cycle', 'time_hi'], 'hub': 'hub_time', 'hub_id': 0}]}

zmc_wearable_links = {'links': [{'link': 'time_event_link', 'values': {'time_id': 0, 'event_id': 0}}]}
    