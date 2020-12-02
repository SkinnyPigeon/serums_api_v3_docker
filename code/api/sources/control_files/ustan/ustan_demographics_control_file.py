
ustan_demographics_hubs = {'table': 'ustan.demographics', 'hubs': [{'hub': 'hub_person', 'keys': ['chi']}]}

ustan_demographics_satellites = {
    'satellites': [
        {
            'satellite': 'sat_person_patient_details', 
            'columns': [
                'first_name', 
                'last_name', 
                'initial', 
                'gp_name', 
                'postcode', 
                'age', 
                'dat_birth', 
                'gender', 
                'civil_status', 
                'religion', 
                'nationality', 
                'height', 
                'weight', 
                'ref_hospital', 
                'dat_death'
            ], 'hub': 'hub_person', 'hub_id': 0,
            'display_text': 'Patient Details'
        }
    ]
}

ustan_demographics_links = {'links': []}
    