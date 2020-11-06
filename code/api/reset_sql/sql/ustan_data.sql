insert into ustan.chemocare (chi, intention, regime, appointment_date, drug_dose, drug_type, drug_status, outcome) 
values (2606566626, 'Adjuvant', 'FEC-80', '2020-12-01', 777, 'neutral', 'NA', 'NA');
insert into ustan.chemocare (chi, intention, regime, appointment_date, drug_dose, drug_type, drug_status, outcome) 
values (2606566626, 'Adjuvant', 'FEC-80', '2020-12-08', 888, 'low_toxic', 'NA', 'NA');
insert into ustan.chemocare (chi, intention, regime, appointment_date, drug_dose, drug_type, drug_status, outcome) 
values (2606566626, 'Adjuvant', 'FEC-80', '2020-12-15', 777, 'neutral', 'NA', 'NA');


insert into ustan.demographics (chi, name, initial, gp_name, postcode, age, dat_birth, gender, civil_status, religion, ref_hospital, dat_death)
values (2606566626, 'MARIE POPPO', 'R', 'BIAGIONI', 'DG349WU', 41, '1976-06-26', 'F', 9, 9, 593, null);


insert into ustan.diagnosis (chi, first_seen_date, primary_field, age, site, side, histology, stage, tnm_t, tnm_n, tnm_m, perf_stat, metastasis1)
values(2606566626, '2014-05-12', 1, 41, 'C50.9', 2, 8504, '3A', '4B', '2', '0', null, null);


insert into ustan.smr01 (chi, incidence_date, admission_date, length_of_stay, main_condition, other_condition1, other_condition2, other_condition3, main_operation_a, main_operation_b, discharge_date, waiting_list_type, marital_status, ethnic_group)
values (2606566626, '2015-11-30', '2016-01-04', 0, 'C509', 'C773', null, null, 'X729', null, '2016-01-03', 2, 'Z', '1A');
insert into ustan.smr01 (chi, incidence_date, admission_date, length_of_stay, main_condition, other_condition1, other_condition2, other_condition3, main_operation_a, main_operation_b, discharge_date, waiting_list_type, marital_status, ethnic_group)
values (2606566626, '2020-09-11', '2020-10-09', 0, 'C509', 'C773', null, null, 'X729', null, '2019-01-08', 2, null, '1A');


insert into ustan.serums_ids (serums_id, chi) values (1, 2606566626);

-- insert into ustan.patient_rules (rule_id, serums_id, tags, filters) values ('h8asdasja8jskalc', 1, ARRAY['patient_details', 'treatments'], '{}');
insert into ustan.patient_rules (rule_id, serums_id, tags, filters) values ('abc', 1, ARRAY['all'], '{}');

insert into ustan.hospital_tags (tags) values (ARRAY['diagnostic', 'patient_details', 'appointments', 'treatments', 'all']);

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



