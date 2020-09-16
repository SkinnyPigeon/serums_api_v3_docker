fcrb_wearable_1 = {'tag': 'wearable', 'table': 'fcrb.vital_signs', 'fields': ['patnr', 'falnr', 'vppid', 'idvs', 'dttyp', 'typevs', 'vwert', 'vbem', 'erdat', 'vptim'], 'key_lookup': {}}
fcrb_wearable_2 = {'tag': 'wearable', 'table': 'fcrb.monitoring_parameters', 'fields': ['patnr', 'falnr', 'vppid', 'pernr', 'vbem', 'datyp', 'wertogr', 'wertugr', 'wertmax', 'wertmin'], 'key_lookup': {}}
fcrb_diagnostic_1 = {'tag': 'diagnostic', 'table': 'fcrb.diagnostic', 'fields': ['einri', 'patnr', 'falnr', 'pernr', 'lfdnr', 'dkey1'], 'key_lookup': {}}
fcrb_diagnostic_2 = {'tag': 'diagnostic', 'table': 'fcrb.episode', 'fields': ['einri', 'falnr', 'patnr', 'pernr', 'bekat', 'falar', 'statu', 'krzan', 'storn', 'casetx', 'enddtx', 'einzg', 'fatnx'], 'key_lookup': {}}
fcrb_medication = {'tag': 'medication', 'table': 'fcrb.medication', 'fields': ['einri', 'patnr', 'falnr', 'pernr', 'motx', 'mostx', 'motypid', 'mpresnr', 'storn', 'stusr', 'stoid', 'erdat', 'stdat'], 'key_lookup': {}}
fcrb_patient_details_1 = {'tag': 'patient_details', 'table': 'fcrb.patient', 'fields': ['patnr', 'gschl', 'nname', 'vname', 'gbdat', 'gbnam', 'namzu', 'glrand', 'famst', 'telf1', 'rvnum', 'decdat'], 'key_lookup': {}}
fcrb_patient_details_2 = {'tag': 'patient_details', 'table': 'fcrb.patient_address', 'fields': ['patnr', 'pstlz', 'stras', 'land', 'ort', 'floor', 'adrnr'], 'key_lookup': {}}
fcrb_patient_address = {'tag': 'patient_address', 'table': 'fcrb.patient_address', 'fields': ['patnr', 'pstlz', 'stras', 'land', 'ort', 'floor', 'adrnr'], 'key_lookup': {}}
fcrb_patient_appointments_1 = {'tag': 'appointments', 'table': 'fcrb.episode', 'fields': ['einri', 'falnr', 'patnr', 'pernr', 'bekat', 'falar', 'statu', 'krzan', 'storn', 'casetx', 'enddtx', 'einzg', 'fatnx']}
fcrb_patient_address = {'tag': 'appointments', 'table': 'fcrb.order_entry', 'fields': ['einri', 'falnr', 'patnr', 'orgid', 'pernr', 'idodr', 'erdat'], 'key_lookup': {}}
fcrb_operations = {}
fcrb_documents = {}
fcrb_healthcare_providers_1 = {'tag': 'healthcare_providers', 'table': 'fcrb.professional', 'fields': ['pernr', 'orgid', 'erusr', 'gbdat', 'rank', 'begdt', 'enddt', 'erdat'], 'key_lookup': {'table': 'fcrb.order_entry', 'keys': ['patnr'], 'field': 'orgid'}}
fcrb_healthcare_providers_2 = {'tag': 'healthcare_providers', 'table': 'fcrb.medical_specialty', 'fields': ['orgid', 'orgna'], 'key_lookup': {'table': 'fcrb.order_entry', 'keys': ['patnr'], 'field': 'orgid'}}
fcrb_drugs_and_alcohol = {}
fcrb_allergies = {}
fcrb_additional_information = {}
fcrb_treatments_1 = {'tag': 'treatments', 'table': 'fcrb.medication', 'fields': ['einri', 'patnr', 'falnr', 'pernr', 'motx', 'mostx', 'motypid', 'mpresnr', 'storn', 'stusr', 'stoid', 'erdat', 'stdat'], 'key_lookup': {}}
fcrb_treatments_2 = {'tag': 'treatments', 'table': 'fcrb.medical_specialty', 'fields': ['orgid', 'orgna'], 'key_lookup': {}}
fcrb_personal = {'tag': 'personal', 'table': 'fcrb.patient', 'fields': ['patnr', 'gschl', 'vname', 'gbdat', 'gbnam', 'glrand'], 'key_lookup': {}}
fcrb_all_1 = {'tag': 'all', 'table': 'fcrb.diagnostic', 'fields': ['einri', 'patnr', 'falnr', 'pernr', 'lfdnr', 'dkey1'], 'key_lookup': {}}
fcrb_all_2 = {'tag': 'all', 'table': 'fcrb.episode', 'fields': ['einri', 'falnr', 'patnr', 'pernr', 'bekat', 'falar', 'statu', 'krzan', 'storn', 'casetx', 'enddtx', 'einzg', 'fatnx'], 'key_lookup': {}}
fcrb_all_3 = {'tag': 'all', 'table': 'fcrb.medical_specialty', 'fields': ['orgid', 'orgna'], 'key_lookup': {'table': 'fcrb.order_entry', 'keys': ['patnr'], 'field': 'orgid'}}
fcrb_all_4 = {'tag': 'all', 'table': 'fcrb.medication', 'fields': ['einri', 'patnr', 'falnr', 'pernr', 'motx', 'mostx', 'motypid', 'mpresnr', 'storn', 'stusr', 'stoid', 'erdat', 'stdat'], 'key_lookup': {}}
fcrb_all_5 = {'tag': 'all', 'table': 'fcrb.monitoring_parameters', 'fields': ['patnr', 'falnr', 'vppid', 'pernr', 'vbem', 'datyp', 'wertogr', 'wertugr', 'wertmax', 'wertmin'], 'key_lookup': {}}
fcrb_all_6 = {'tag': 'all', 'table': 'fcrb.order_entry', 'fields': ['einri', 'falnr', 'patnr', 'orgid', 'pernr', 'idodr', 'erdat'], 'key_lookup': {}}
fcrb_all_7 = {'tag': 'all', 'table': 'fcrb.patient', 'fields': ['patnr', 'gschl', 'nname', 'vname', 'gbdat', 'gbnam', 'namzu', 'glrand', 'famst', 'telf1', 'rvnum', 'decdat'], 'key_lookup': {}}
fcrb_all_8 = {'tag': 'all', 'table': 'fcrb.patient_address', 'fields': ['patnr', 'pstlz', 'stras', 'land', 'ort', 'floor', 'adrnr'], 'key_lookup': {}}
fcrb_all_9 = {'tag': 'all', 'table': 'fcrb.professional', 'fields': ['pernr', 'orgid', 'erusr', 'gbdat', 'rank', 'begdt', 'enddt', 'erdat'], 'key_lookup': {'table': 'fcrb.order_entry', 'keys': ['patnr'], 'field': 'orgid'}}
fcrb_all_10 = {'tag': 'all', 'table': 'fcrb.vital_signs', 'fields': ['patnr', 'falnr', 'vppid', 'idvs', 'dttyp', 'typevs', 'vwert', 'vbem', 'erdat', 'vptim'], 'key_lookup': {}}

fcrb_healthcare_providers_1, fcrb_healthcare_providers_2
fcrb_tags = [fcrb_wearable_1, fcrb_wearable_2, fcrb_diagnostic_1, fcrb_diagnostic_2, fcrb_medication, fcrb_patient_details_1, fcrb_patient_details_2, fcrb_patient_address, fcrb_patient_appointments_1, fcrb_patient_address, fcrb_treatments_1, fcrb_treatments_2, fcrb_healthcare_providers_1, fcrb_healthcare_providers_2, fcrb_personal, fcrb_all_1, fcrb_all_2, fcrb_all_3, fcrb_all_4, fcrb_all_5, fcrb_all_6, fcrb_all_7, fcrb_all_8, fcrb_all_9, fcrb_all_10]

# fcrb_personal = {'tag': 'personal', 'table': 'fcrb.patient', 'fields': ['patnr', 'gschl', 'vname', 'gbdat', 'gbnam', 'glrand']}
# fcrb_patient_details_1 = {'tag': 'patient_details', 'table': 'fcrb.patient', 'fields': ['patnr', 'gschl', 'nname', 'vname', 'gbdat', 'gbnam', 'namzu', 'glrand', 'famst', 'telf1', 'rvnum']}
# fcrb_patient_details_2 = {'tag': 'patient_details', 'table': 'fcrb.patient_address', 'fields': ['patnr', 'pstlz', 'stras', 'land', 'ort', 'floor', 'adrnr']}
# fcrb_wearable = {'tag': 'wearable', 'table': 'fcrb.vital_signs', 'fields': ['patnr', 'falnr', 'idvs', 'vppid', 'dttyp', 'erdat', 'typevs', 'vwert', 'vbem']}

# fcrb_tags = [fcrb_personal, fcrb_patient_details_1, fcrb_patient_details_2, fcrb_wearable]