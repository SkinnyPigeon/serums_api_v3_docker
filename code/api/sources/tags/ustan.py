ustan_personal = {'tag': 'personal', 'table': 'ustan.ndc_smr01', 'fields': ['sex', 'height', 'weight']}
ustan_patient_details_1 = {'tag': 'patient_details', 'table': 'ustan.ndc_smr01', 'fields': ['sex', 'age_in_years', 'ethnic_group', 'marital_status', 'postcode', 'height', 'weight']}
ustan_patient_details_2 = {'tag': 'patient_details', 'table': 'ustan.ndc_charlson', 'fields': ['postcode']}
ustan_treatments = {'tag': 'treatments', 'table': 'ustan.chemocare_treatment', 'fields': ['appointment_date', 'last_toxicity_date', 'tumour_group', 'age_at_diagnosis', 'height', 'weight', 'surface_area', 'patient_type', 'consultant_code', 'intention', 'regime_code', 'cycle', 'cycle_id', 'drug_type', 'drug_name', 'drug_dose', 'required_dose', 'drug_status']}

ustan_tags = [ustan_personal, ustan_patient_details_1, ustan_patient_details_2, ustan_treatments]