insert into ustan.general_data (chi) values (1);

insert into ustan.chemocare_toxicity (date1, nausea, vomiting, diarrhoea, constipation, oral_mucostis, oesophasitis, neurotoxicity, hand_foot, skin, hypersensitivity, fatigue, performance_status, issues_since_last_visit, last_visit_issue_description, chi
) values ('2020-08-01', 2, 3, 4, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 'Feeling better', 1);


insert into ustan.chemocare_treatment (appointment_date, last_toxicity_date, tumour_group, age_at_diagnosis, height, weight, surface_area, patient_type, consultant_code, intention, regime_code, cycle, cycle_id, drug_type, drug_name, drug_dose, required_dose, drug_status, chi
) values ('2020-07-04', '2020-01-23', 'Mixed', 47, 167, 78, 52, 'patient_type', 'consultant_code', 'intention', 'regime_code', 1, 1, 'drug_type', 'drug_name', 50, 50, 'taken', 1);

insert into ustan.chemocare_treatment (appointment_date, last_toxicity_date, tumour_group, age_at_diagnosis, height, weight, surface_area, patient_type, consultant_code, intention, regime_code, cycle, cycle_id, drug_type, drug_name, drug_dose, required_dose, drug_status, chi
) values ('2020-08-04', '2020-01-23', 'Mixed', 47, 167, 78, 52, 'patient_type', 'consultant_code', 'intention', 'regime_code', 1, 2, 'drug_type', 'drug_name', 50, 50, 'taken', 1);


insert into ustan.ndc_charlson (postcode, incidence_year, simd1, simd, conf_heart_fail_flag, dementia_flag, pulmonary_flag, con_tiss_disease_flag, diabetes_flag, para_hemiplegia_flag, renal_flag, liver_flag, aids_hiv_flag, charlson_quan_score, chi) 
values ('EH6', 2020, 4, 5, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1);


insert into ustan.ndc_smr01 (admission_date, discharge_date, length_of_stay, sex, age_in_years, ethnic_group, marital_status, postcode, main_condition, other_condition_1, other_condition_2, other_condition_3, other_condition_4, main_operation_a, main_operation_b, chi, age_at_diagnosis, height, weight)
 values ('2020-08-04', 20200807, 3, 1, 47, 'ethnic_group', 'marital_status', 'postcode', 'main_condition', 'other_condition_1', 'other_condition_2', 'other_condition_3', 'other_condition_4', 'main_operation_a', 'main_operation_b', 1, 57, 167, 78);

insert into ustan.ndc_smr06 (incidence_date, tumour_site_icd10, oestrogen_receptor_er_status, her2_status_code, stage_clinical_t_code, stage_clinical_n_code, stage_clinical_m_code, pathological_tumour_size, chi) 
values ('2020-07-04', 'tumour_site_icd10', 5, 3, 'stage_clinical_t_code', 'stage_clinical_n_code', 'stage_clinical_m_code', 1, 1);


insert into ustan.serums_ids (serums_id, chi) values (1, 1);


insert into ustan.patient_rules (rule_id, tags, filters) values ('h8asdasja8jskalc', ARRAY['patient_details', 'treatments'], '{}');

insert into ustan.hospital_tags (tags) values (ARRAY['diagnostic', 'medication', 'patient_details', 'patient_address', 'appointments', 'patient_details', 'healthcare_providers', 'treatments', 'personal']);

insert into ustan.hospital_doctors (id, name, specialism) values (1, 'Isla MacDonald', 1);
insert into ustan.hospital_doctors (id, name, specialism) values (2, 'Charles Stewart', 1);
insert into ustan.hospital_doctors (id, name, specialism) values (3, 'Oliver Wilson', 1);
insert into ustan.hospital_doctors (id, name, specialism) values (4, 'Emily Scott', 1);
insert into ustan.hospital_doctors (id, name, specialism) values (5, 'Ella Murray', 2);
insert into ustan.hospital_doctors (id, name, specialism) values (6, 'James Campbell', 2);
insert into ustan.hospital_doctors (id, name, specialism) values (7, 'Charlotte Watson', 2);
insert into ustan.hospital_doctors (id, name, specialism) values (8, 'Amelia Clark', 3);
insert into ustan.hospital_doctors (id, name, specialism) values (9, 'Noah Thomson', 3);
insert into ustan.hospital_doctors (id, name, specialism) values (10, 'Jack Smith', 3);



