
zmc_patient_documents_hubs = {'table': 'zmc.patient_documents', 'hubs': [{'hub': 'hub_object', 'keys': ['patnr']}]}

zmc_patient_documents_satellites = {
    'satellites': [
        {
            'satellite': 'sat_object_patient_documents', 
            'columns': ['report_title', 'department', 'date', 'content'], 
            'hub': 'hub_object', 
            'hub_id': 0,
            'display_text': 'Patient Documents'
        }
    ]
}

zmc_patient_documents_links = {'links': []}
    