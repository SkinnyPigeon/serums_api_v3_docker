ustan_wearable = {}

ustan_diagnostic_1 = {'tag': 'diagnostic', 'table': 'ustan.chemocare_toxicity', 'fields': ['chi', 'date1', 'nausea', 'vomiting', 'diarrhoea', 'constipation', 'oral_mucostis', 'oesophasitis', 'neurotoxicity', 'hand_foot', 'skin', 'hypersensitivity', 'fatigue', 'performance_status', 'issues_since_last_visit', 'last_visit_issue_description'], 'key_lookup': {}}
ustan_diagnostic_2 = {'tag': 'diagnostic', 'table': 'ustan.ndc_charlson', 'fields': ['chi', 'incidence_year', 'simd1', 'simd', 'conf_heart_fail_flag', 'dementia_flag', 'pulmonary_flag', 'con_tiss_disease_flag', 'diabetes_flag', 'para_hemiplegia_flag', 'renal_flag', 'liver_flag', 'aids_hiv_flag', 'charlson_quan_score'], 'key_lookup': {}}
ustan_diagnostic_3 = {'tag': 'diagnostic', 'table': 'ustan.ndc_smr06', 'fields': ['chi', 'incidence_date', 'tumour_site_icd10', 'oestrogen_receptor_er_status', 'her2_status_code', 'stage_clinical_t_code', 'stage_clinical_n_code', 'stage_clinical_m_code', 'pathological_tumour_size'], 'key_lookup': {}}
ustan_diagnostic_4 = {'tag': 'diagnostic', 'table': 'ustan.ndc_smr01', 'fields': ['chi', 'main_condition', 'other_condition_1', 'other_condition_2', 'other_condition_3', 'other_condition_4', 'age_at_diagnosis'], 'key_lookup': {}}

ustan_medication = {'tag': 'medication', 'table': 'ustan.chemocare_treatment', 'fields': ['chi', 'intention', 'regime_code', 'cycle', 'cycle_id', 'drug_type', 'drug_name', 'drug_dose', 'required_dose', 'drug_status'], 'key_lookup': {}}

ustan_patient_details_1 = {'tag': 'patient_details', 'table': 'ustan.ndc_smr01', 'fields': ['chi', 'sex', 'age_in_years', 'ethnic_group', 'marital_status', 'postcode', 'height', 'weight'], 'key_lookup': {}}
ustan_patient_details_2 = {'tag': 'patient_details', 'table': 'ustan.ndc_charlson', 'fields': ['chi', 'postcode'], 'key_lookup': {}}

ustan_patient_address = {'tag': 'patient_address', 'table': 'ustan.ndc_charlson', 'fields': ['chi', 'postcode'], 'key_lookup': {}}

ustan_patient_appointments_1 = {'tag': 'appointments', 'table': 'ustan.chemocare_treatment', 'fields': ['chi', 'appointment_date', 'last_toxicity_date', 'tumour_group', 'age_at_diagnosis', 'height', 'weight', 'surface_area', 'patient_type', 'consultant_code', 'intention', 'regime_code', 'cycle', 'cycle_id', 'drug_type', 'drug_name', 'required_dose', 'drug_status'], 'key_lookup': {}}
ustan_patient_appointments_2 = {'tag': 'appointments', 'table': 'ustan.ndc_smr01', 'fields': ['chi','admission_date', 'discharge_date', 'length_of_stay', 'sex', 'age_in_years', 'ethnic_group', 'marital_status', 'postcode', 'age_at_diagnosis', 'height', 'weight', 'main_condition', 'other_condition_1', 'other_condition_2', 'other_condition_3', 'other_condition_4', 'main_operation_a', 'main_operation_b'], 'key_lookup': {}}

ustan_operations = {'tag': 'patient_details', 'table': 'ustan.ndc_smr01', 'fields': ['chi', 'admission_date', 'discharge_date', 'length_of_stay', 'main_condition', 'other_condition_1', 'other_condition_2', 'other_condition_3', 'other_condition_4', 'main_operation_a', 'main_operation_b', 'age_at_diagnosis'], 'key_lookup': {}}

ustan_documents = {}

ustan_healthcare_providers = {'tag': 'healthcare_providers', 'table': 'ustan.chemocare_treatment', 'fields': ['chi', 'consultant_code'], 'key_lookup': {}}

ustan_drugs_and_alcohol = {}

ustan_allergies = {}

ustan_additional_information = {}

ustan_treatments = {'tag': 'treatments', 'table': 'ustan.chemocare_treatment', 'fields': ['chi', 'appointment_date', 'last_toxicity_date', 'tumour_group', 'age_at_diagnosis', 'height', 'weight', 'surface_area', 'patient_type', 'consultant_code', 'intention', 'regime_code', 'cycle', 'cycle_id', 'drug_type', 'drug_name', 'required_dose', 'drug_status'], 'key_lookup': {}}

ustan_personal = {'tag': 'personal', 'table': 'ustan.ndc_smr01', 'fields': ['chi', 'sex', 'height', 'weight'], 'key_lookup': {}}

ustan_all_1 = {'tag': 'all', 'table': 'ustan.chemocare_toxicity', 'fields': ['chi', 'date1', 'nausea', 'vomiting', 'diarrhoea', 'constipation', 'oral_mucostis', 'oesophasitis', 'neurotoxicity', 'hand_foot', 'skin', 'hypersensitivity', 'fatigue', 'performance_status', 'issues_since_last_visit', 'last_visit_issue_description'], 'key_lookup': {}}
ustan_all_2 = {'tag': 'all', 'table': 'ustan.chemocare_treatment', 'fields': ['chi', 'appointment_date', 'last_toxicity_date', 'tumour_group', 'age_at_diagnosis', 'height', 'weight', 'surface_area', 'patient_type', 'consultant_code', 'intention', 'regime_code', 'cycle', 'cycle_id', 'drug_type', 'drug_name', 'required_dose', 'drug_status'], 'key_lookup': {}}
ustan_all_3 = {'tag': 'all', 'table': 'ustan.ndc_charlson', 'fields': ['chi', 'postcode', 'simd', 'simd1', 'incidence_year', 'conf_heart_fail_flag', 'dementia_flag', 'pulmonary_flag', 'con_tiss_disease_flag', 'diabetes_flag', 'para_hemiplegia_flag', 'renal_flag', 'liver_flag', 'aids_hiv_flag', 'charlson_quan_score'], 'key_lookup': {}}
ustan_all_4 = {'tag': 'all', 'table': 'ustan.ndc_smr01', 'fields': ['chi','admission_date', 'discharge_date', 'length_of_stay', 'sex', 'age_in_years', 'ethnic_group', 'marital_status', 'postcode', 'age_at_diagnosis', 'height', 'weight', 'main_condition', 'other_condition_1', 'other_condition_2', 'other_condition_3', 'other_condition_4', 'main_operation_a', 'main_operation_b'], 'key_lookup': {}}
ustan_all_5 = {'tag': 'all', 'table': 'ustan.ndc_smr06', 'fields': ['chi', 'incidence_date', 'tumour_site_icd10', 'oestrogen_receptor_er_status', 'her2_status_code', 'stage_clinical_t_code', 'stage_clinical_n_code', 'stage_clinical_m_code', 'pathological_tumour_size'], 'key_lookup': {}}

ustan_tags = [ustan_wearable, ustan_diagnostic_1, ustan_diagnostic_2, ustan_diagnostic_3, ustan_diagnostic_4, ustan_medication, ustan_patient_details_1, ustan_patient_details_2, ustan_patient_address, ustan_patient_appointments_1, ustan_patient_appointments_2, ustan_operations, ustan_documents, ustan_healthcare_providers, ustan_drugs_and_alcohol, ustan_allergies, ustan_additional_information, ustan_treatments, ustan_personal, ustan_all_1, ustan_all_2, ustan_all_3, ustan_all_4, ustan_all_5]