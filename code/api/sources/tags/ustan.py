ustan_wearable = {}

ustan_diagnostic = {
  'tag': 'diagnostic',
  'table': 'ustan.diagnosis',
  'fields': [
    'chi',
    'first_seen_date',
    '"primary"',
    'age',
    'site',
    'side',
    'histology',
    'stage',
    'tnm_t',
    'tnm_n',
    'tnm_m',
    'perf_stat',
    'metastasis1'
  ], 'key_lookup': {}
}

ustan_medication = {}

ustan_patient_details = {
  'tag': 'patient_details',
  'table': 'ustan.demographics',
  'fields': [
    'chi',
    'name',
    'gp_name',
    'postcode',
    'age',
    'dat_birth',
    'gender',
    'civil_status',
    'religion',
    'ref_hospital',
    'dat_death'
  ], 'key_lookup': {}
}

ustan_patient_address = {}

ustan_appointments = {
  'tag': 'appointments',
  'table': 'ustan.smr01',
  'fields': [
    'chi',
    'incidence_date',
    'admission_date',
    'length_of_stay',
    'other_condition1',
    'other_condition2',
    'other_condition3',
    'main_operation_b',
    'discharge_date',
    'waiting_list_type',
    'main_condition',
    'main_operation_a',
    'marital_status',
    'ethnic_group'
  ], 'key_lookup': {}
}

ustan_operations = {}

ustan_documents = {}

ustan_healthcare_providers = {}

ustan_drugs_and_alcohol = {}

ustan_allergies = {}

ustan_additional_information = {}

ustan_treatments = {
  'tag': 'treatments',
  'table': 'ustan.chemocare',
  'fields': [
    'chi',
    'intention',
    'regime',
    'appointment_date',
    'drug_dose',
    'drug_type',
    'stage_clinical_m',
    'drug_status',
    'outcome'
  ], 'key_lookup': {}
}

ustan_personal = {}

ustan_all_1 = {
  'tag': 'all',
  'table': 'ustan.smr01',
  'fields': [
    'chi',
    'incidence_date',
    'admission_date',
    'length_of_stay',
    'other_condition1',
    'other_condition2',
    'other_condition3',
    'main_operation_b',
    'discharge_date',
    'waiting_list_type',
    'main_condition',
    'main_operation_a',
    'marital_status',
    'ethnic_group'
  ], 'key_lookup': {}
}

ustan_all_2 = {
  'tag': 'all',
  'table': 'ustan.chemocare',
  'fields': [
    'chi',
    'intention',
    'regime',
    'appointment_date',
    'drug_dose',
    'drug_type',
    'stage_clinical_m',
    'drug_status',
    'outcome'
  ], 'key_lookup': {}
}

ustan_all_3 = {
  'tag': 'all',
  'table': 'ustan.diagnosis',
  'fields': [
    'chi',
    'first_seen_date',
    'primary',
    'age',
    'site',
    'side',
    'histology',
    'stage',
    'tnm_t',
    'tnm_n',
    'tnm_m',
    'perf_stat',
    'metastasis1'
  ], 'key_lookup': {}
}

ustan_all_4 = {
  'tag': 'all',
  'table': 'ustan.demographics',
  'fields': [
    'chi',
    'name',
    'gp_name',
    'postcode',
    'age',
    'dat_birth',
    'gender',
    'civil_status',
    'religion',
    'ref_hospital',
    'dat_death'
  ], 'key_lookup': {}
}

ustan_tags = [
    ustan_wearable,
    ustan_diagnostic,
    ustan_medication,
    ustan_patient_details,
    ustan_patient_address,
    ustan_appointments,
    ustan_operations,
    ustan_documents,
    ustan_healthcare_providers,
    ustan_drugs_and_alcohol,
    ustan_allergies,
    ustan_additional_information,
    ustan_treatments,
    ustan_personal,
    ustan_all_1,
    ustan_all_2,
    ustan_all_3,
    ustan_all_4
]