zmc_wearable = {'tag': 'wearable', 'table': 'zmc.wearable', 'fields': ['patnr', 'nr_sst', 'steps_total', 'cadence', 'cyc_rot', 'cyc_rpm', 'day_nr', 'time_total', 'time_passive', 'time_active', 'time_sit', 'time_stand', 'time_walk', 'time_cycle', 'time_hi'], 'key_lookup': {}}

zmc_diagnostic_1 = {'tag': 'diagnostic', 'table': 'zmc.patient_diagnostic', 'fields': ['patnr', 'type', 'name', 'anatomical_location', 'laterality', 'begin_date', 'end_date'], 'key_lookup': {}}
zmc_diagnostic_2 = {'tag': 'diagnostic', 'table': 'zmc.patient_documents', 'fields': ['patnr', 'report_title', 'department', 'date', 'content'], 'key_lookup': {}}

zmc_medication = {}

zmc_patient_details_1 = {'tag': 'patient_details', 'table': 'zmc.patient_details', 'fields': ['patnr', 'gschl', 'nname', 'nnams', 'vname', 'titel', 'namzu', 'gbdat', 'gbnam', 'gbnas', 'gland', 'natio', 'land', 'telf1', 'pstlz', 'ort', 'stras'], 'key_lookup': {}}
zmc_patient_details_2 = {'tag': 'patient_details', 'table': 'zmc.patient_measurements', 'fields': ['patnr', 'height', 'weight', 'date'], 'key_lookup': {}}

zmc_patient_address = {'tag': 'patient_address', 'table': 'zmc.patient_details', 'fields': ['land', 'pstlz', 'ort', 'stras', 'telf1'], 'key_lookup': {}}

zmc_patient_appointment = {'tag': 'appointments', 'table': 'zmc.patient_appointments', 'fields': ['patnr', 'type', 'date', 'notes'], 'key_lookup': {}}

zmc_operations = {'tag': 'operations', 'table': 'zmc.patient_operations', 'fields': ['patnr', 'anatomical_location', 'date', 'notes'], 'key_lookup': {}}

zmc_documents = {'tag': 'documents', 'table': 'zmc.patient_documents', 'fields': ['patnr', 'report_title', 'department', 'date', 'content'], 'key_lookup': {}}

zmc_healthcare_providers = {}

zmc_drugs_and_alcohol_1 = {'tag': 'drugs_and_alcohol', 'table': 'zmc.patient_drug_use', 'fields': ['patnr', 'substance', 'quantity', 'description'], 'key_lookup': {}}
zmc_drugs_and_alcohol_2 = {'tag': 'drugs_and_alcohol', 'table': 'zmc.patient_alcohol_use', 'fields': ['patnr', 'usage_status', 'quantity', 'description'], 'key_lookup': {}}
zmc_drugs_and_alcohol_3 = {'tag': 'drugs_and_alcohol', 'table': 'zmc.patient_tobacco_use', 'fields': ['patnr', 'substance', 'description'], 'key_lookup': {}}

zmc_allergies = {'tag': 'allergies', 'table': 'zmc.patient_allergies_intolerance', 'fields': ['patnr', 'caustic_substance', 'critical', 'description'], 'key_lookup': {}}

zmc_additional_information_1 = {'tag': 'additional_information', 'table': 'zmc.patient_warnings', 'fields': ['patnr', 'alerts', 'type', 'begin_date'], 'key_lookup': {}}
zmc_additional_information_2 = {'tag': 'additional_information', 'table': 'zmc.patient_functional_state', 'fields': ['patnr', 'name', 'value', 'date'], 'key_lookup': {}}
zmc_additional_information_3 = {'tag': 'additional_information', 'table': 'zmc.patient_living_situation', 'fields': ['patnr', 'house_type', 'description'], 'key_lookup': {}}

zmc_treatments_1 = {'tag': 'treatments', 'table': 'zmc.patient_operations', 'fields': ['patnr', 'anatomical_location', 'date', 'notes'], 'key_lookup': {}}
zmc_treatments_2 = {'tag': 'treatments', 'table': 'zmc.patient_documents', 'fields': ['patnr', 'report_title', 'department', 'date', 'content'], 'key_lookup': {}}

zmc_personal = {'tag': 'personal', 'table': 'zmc.patient_details', 'fields': ['patnr','gschl','nname','nnams','gbdat','natio'], 'key_lookup': {}}

zmc_all_1 = {'tag': 'all', 'table': 'zmc.patient_alcohol_use', 'fields': ['patnr', 'usage_status', 'quantity', 'description'], 'key_lookup': {}}
zmc_all_2 = {'tag': 'all', 'table': 'zmc.patient_allergies_intolerance', 'fields': ['patnr', 'caustic_substance', 'critical', 'description'], 'key_lookup': {}}
zmc_all_3 = {'tag': 'all', 'table': 'zmc.patient_appointments', 'fields': ['patnr', 'type', 'date', 'notes'], 'key_lookup': {}}
zmc_all_4 = {'tag': 'all', 'table': 'zmc.patient_details', 'fields': ['patnr', 'gschl', 'nname', 'nnams', 'vname', 'titel', 'namzu', 'gbdat', 'gbnam', 'gbnas', 'gland', 'natio', 'land', 'telf1', 'pstlz', 'ort', 'stras'], 'key_lookup': {}}
zmc_all_5 = {'tag': 'all', 'table': 'zmc.patient_diagnostic', 'fields': ['patnr', 'type', 'name', 'anatomical_location', 'laterality', 'begin_date', 'end_date'], 'key_lookup': {}}
zmc_all_6 = {'tag': 'all', 'table': 'zmc.patient_documents', 'fields': ['patnr', 'report_title', 'department', 'date', 'content'], 'key_lookup': {}}
zmc_all_7 = {'tag': 'all', 'table': 'zmc.patient_drug_use', 'fields': ['patnr', 'substance', 'quantity', 'description'], 'key_lookup': {}}
zmc_all_8 = {'tag': 'all', 'table': 'zmc.patient_functional_state', 'fields': ['patnr', 'name', 'value', 'date'], 'key_lookup': {}}
zmc_all_9 = {'tag': 'all', 'table': 'zmc.patient_living_situation', 'fields': ['patnr', 'house_type', 'description'], 'key_lookup': {}}
zmc_all_10 = {'tag': 'all', 'table': 'zmc.patient_measurements', 'fields': ['patnr', 'height', 'weight', 'date'], 'key_lookup': {}}
zmc_all_11 = {'tag': 'all', 'table': 'zmc.patient_operations', 'fields': ['patnr', 'anatomical_location', 'date', 'notes'], 'key_lookup': {}}
zmc_all_12 = {'tag': 'all', 'table': 'zmc.patient_tobacco_use', 'fields': ['patnr', 'substance', 'description'], 'key_lookup': {}}
zmc_all_13 = {'tag': 'all', 'table': 'zmc.patient_warnings', 'fields': ['patnr', 'alerts', 'type', 'begin_date'], 'key_lookup': {}}
zmc_all_14 = {'tag': 'all', 'table': 'zmc.wearable', 'fields': ['patnr', 'nr_sst', 'steps_total', 'cadence', 'cyc_rot', 'cyc_rpm', 'day_nr', 'time_total', 'time_passive', 'time_active', 'time_sit', 'time_stand', 'time_walk', 'time_cycle', 'time_hi'], 'key_lookup': {}}

zmc_tags = [zmc_wearable, zmc_diagnostic_1, zmc_diagnostic_2, zmc_medication, zmc_patient_details_1, zmc_patient_details_2, zmc_patient_address, zmc_patient_appointment, zmc_operations, zmc_documents, zmc_healthcare_providers, zmc_drugs_and_alcohol_1, zmc_drugs_and_alcohol_2, zmc_drugs_and_alcohol_3, zmc_allergies, zmc_additional_information_1, zmc_additional_information_2, zmc_additional_information_3, zmc_treatments_1, zmc_treatments_2, zmc_personal, zmc_all_1, zmc_all_2, zmc_all_3, zmc_all_4, zmc_all_5, zmc_all_6, zmc_all_7, zmc_all_8, zmc_all_9, zmc_all_10, zmc_all_11, zmc_all_12, zmc_all_13, zmc_all_14]