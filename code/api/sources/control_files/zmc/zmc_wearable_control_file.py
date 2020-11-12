
# zmc_wearable_hubs = {'table': 'zmc.wearable', 'hubs': [{'hub': 'hub_event', 'keys': ['patnr']}, {'hub': 'hub_time', 'keys': ['patnr']}]}
zmc_wearable_hubs = {'table': 'zmc.wearable', 'hubs': [{'hub': 'hub_event', 'keys': ['patnr']}]}

zmc_wearable_satellites = {
    # 'satellites': [
    #     {
    #         'satellite': 'sat_event_exercise_measurements', 
    #         'columns': ['nr_sst', 'steps_total', 'cadence', 'cyc_rot', 'cyc_rpm'], 
    #         'hub': 'hub_event', 
    #         'hub_id': 0,
    #         'display_text': 'Exercise Values'
    #     }, 
    #     {
    #         'satellite': 'sat_time_exercise_measurements', 
    #         'columns': ['day_nr', 'time_total', 'time_passive', 'time_active', 'time_sit', 'time_stand', 'time_walk', 'time_cycle', 'time_hi'], 
    #         'hub': 'hub_time', 
    #         'hub_id': 0,
    #         'display_text': 'Exercise Lengths'
    #     }
    # ]

    'satellites': [
        {
            'satellite': 'sat_event_exercise_measurements',
            'columns': [
                'datum',
                'duur_meting',
                'tijd_gezeten',
                'tijd_gelopen',
                'aantal_keren_opgestaan_uit_een_stoel',
                'aantal_stappen_gezet', 
                'gemiddeld_aantal_stappen_per_minuut'
            ],
            'hub': 'hub_event',
            'hub_id': 0,
            'display_text': 'Inspannings'
        }
    ]
}

zmc_wearable_links = {'links': []}
# zmc_wearable_links = {'links': [{'link': 'time_event_link', 'values': {'time_id': 0, 'event_id': 0}}]}
    