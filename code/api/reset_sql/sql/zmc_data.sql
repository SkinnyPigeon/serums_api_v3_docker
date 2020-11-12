insert into zmc.patient_details (patnr,gschl,nname,nnams,vname,titel,namzu,gbdat,gbnam,gbnas,gland,natio,land,pstlz,ort,stras,telf1
) values (1075835,2,'Calimerass','CALIMERASS','TSTO',NULL,NULL,'04.01.1980','Test PTE - IMS Team.','TESTPTE-IMSTEAM.','NL','NL','NL','2986 VA','Ridderkerk','Koolmees 13 A bus 5','06-21185097');


-- insert into zmc.wearable (patnr,day_nr,time_total,time_passive,time_active,time_sit,time_stand,time_walk,time_cycle,time_hi,nr_sst,steps_total,cadence,cyc_rot,cyc_rpm
-- ) values (1075835,1,41300,35849,5449,31045,4804,5071,378,0,45,6047,77,245,39);

-- insert into zmc.wearable (patnr,day_nr,time_total,time_passive,time_active,time_sit,time_stand,time_walk,time_cycle,time_hi,nr_sst,steps_total,cadence,cyc_rot,cyc_rpm
-- ) values (1075835,2,42674,37939,4733,31227,6712,4733,0,0,39,5885,80,0,0);

-- insert into zmc.wearable (patnr,day_nr,time_total,time_passive,time_active,time_sit,time_stand,time_walk,time_cycle,time_hi,nr_sst,steps_total,cadence,cyc_rot,cyc_rpm
-- ) values (1075835,3,41071,36401,4668,31652,4749,4668,0,0,33,5892,76,0,0);

-- insert into zmc.wearable (patnr,day_nr,time_total,time_passive,time_active,time_sit,time_stand,time_walk,time_cycle,time_hi,nr_sst,steps_total,cadence,cyc_rot,cyc_rpm
-- ) values (1075835,4,45420,40762,4655,34417,6345,4655,0,0,46,6000,81,0,0);

insert into zmc.wearable (patnr, datum, duur_meting, tijd_gezeten, tijd_gelopen, aantal_keren_opgestaan_uit_een_stoel, aantal_stappen_gezet, gemiddeld_aantal_stappen_per_minuut)
values (1075835, '2020-11-16', '16:09:00', '08:46:37', '00:32:49', 31, 2923, 107);
insert into zmc.wearable (patnr, datum, duur_meting, tijd_gezeten, tijd_gelopen, aantal_keren_opgestaan_uit_een_stoel, aantal_stappen_gezet, gemiddeld_aantal_stappen_per_minuut)
values (1075835, '2020-11-17', '10:23:14', '07:35:43', '00:23:57', 43, 2202, 115);
insert into zmc.wearable (patnr, datum, duur_meting, tijd_gezeten, tijd_gelopen, aantal_keren_opgestaan_uit_een_stoel, aantal_stappen_gezet, gemiddeld_aantal_stappen_per_minuut)
values (1075835, '2020-11-18', '11:14:46', '07:06:27', '00:29:34', 20, 2872, 120);
insert into zmc.wearable (patnr, datum, duur_meting, tijd_gezeten, tijd_gelopen, aantal_keren_opgestaan_uit_een_stoel, aantal_stappen_gezet, gemiddeld_aantal_stappen_per_minuut)
values (1075835, '2020-11-19', '10:49:25', '07:07:31', '00:36:19', 20, 3775, 115);
insert into zmc.wearable (patnr, datum, duur_meting, tijd_gezeten, tijd_gelopen, aantal_keren_opgestaan_uit_een_stoel, aantal_stappen_gezet, gemiddeld_aantal_stappen_per_minuut)
values (1075835, '2020-11-20', '09:03:09', '04:16:57', '00:41:44', 12, 4001, 111);
insert into zmc.wearable (patnr, datum, duur_meting, tijd_gezeten, tijd_gelopen, aantal_keren_opgestaan_uit_een_stoel, aantal_stappen_gezet, gemiddeld_aantal_stappen_per_minuut)
values (1075835, '2020-11-21', '12:28:43', '09:30:42', '00:52:50', 31, 5199, 111);
insert into zmc.wearable (patnr, datum, duur_meting, tijd_gezeten, tijd_gelopen, aantal_keren_opgestaan_uit_een_stoel, aantal_stappen_gezet, gemiddeld_aantal_stappen_per_minuut)
values (1075835, '2020-11-22', '14:41:52', '09:24:12', '01:31:35', 40, 8593, 100);


insert into zmc.patient_measurements (patnr, height, weight, date) values (1075835, 195, 90, '2018-09-20');


insert into zmc.patient_documents (patnr, report_title, department, date, content) values (1075835, 'GP Referral', 'Doctor''s note', '2020-08-20', 'Patient should go for consultation with specialist');


insert into zmc.patient_appointments (patnr, type, date, notes) values (1075835, 'Consultation', '2020-09-01', 'Debiliating pain on the rights side of the hip. Needs an operation');
insert into zmc.patient_appointments (patnr, type, date, notes) values (1075835, 'Control Appointment', '2020-10-26', 'Progress measured via Activity Monitor. No physical appointment needed');


insert into zmc.patient_operations (patnr, anatomical_location, date, notes) values (1075835, 'Right hip', '2020-09-20', 'See operation report');


insert into zmc.patient_warnings (patnr, alerts, begin_date, type) values (1075835, 'Pacemaker', '2015-06-01', 'Conditie');


insert into zmc.patient_functional_state (patnr, name, value, date) values (1075835, 'Finding related to hearing', 'Hearing problems', '2018-08-25');


insert into zmc.patient_living_situation (patnr, house_type, description) values (1075835, 'Single-family house', NULL);


insert into zmc.patient_drug_use (patnr, substance, quantity, description) values (1075835, NULL, NULL, NULL);


insert into zmc.patient_alcohol_use (patnr, usage_status, quantity,description) values (1075835, NULL, NULL, NULL);


insert into zmc.patient_tobacco_use (patnr, substance, description) values (1075835, 'Smokes cigarettes (Ex-smoker)', 20);


insert into zmc.patient_allergies_intolerance (patnr, caustic_substance, critical, description) values (1075835, 'Iodine', 'Medium', 'Local irritation, itch');


insert into zmc.patient_diagnostic (patnr, type, name, anatomical_location, laterality, begin_date, end_date) values (1075835, 'Diagnosis', 'Coxartrose', 'Right Hip', 'No', '2020-09-01', '2020-11-27');


-- insert into zmc.patient_rules (rule_id, serums_id, tags, filters) values ('9a8sdn8asj89dfs', 1, ARRAY['wearable', 'patient_details'], '{}');
insert into zmc.patient_rules (rule_id, serums_id, tags, filters) values ('abc', 1, ARRAY['all'], '{}');

insert into zmc.serums_ids (serums_id, patnr) values (1, 1075835);

insert into zmc.hospital_tags (tags) values (ARRAY['wearable', 'diagnostic', 'patient_details', 'patient_address', 'appointments', 'operations', 'documents', 'drugs_and_alcohol', 'allergies', 'additional_information', 'treatments', 'personal', 'all']);
-- insert into zmc.translated_tags (tags) values ('{"0": {"tag": "wearable", "translation": "Wearable/Sensor"}, "1": {"tag": "diagnostic", "translation": "Diagnostiek"}, "2": {"tag": "patient_details", "translation": "Patiënten informatie"}, "3": {"tag": "patient_address", "translation": "Adres van de patiënt"}, "4": {"tag": "appointments", "translation": "Afspraken"}, "5": {"tag": "operations", "translation": "Operaties"}, "6": {"tag": "documents", "translation": "Documenten"}, "7": {"tag": "drugs_and_alcohol", "translation": "Drugs en alcohol"}, "8": {"tag": "allergies", "translation": "Allergieën"}, "9": {"tag": "additional_information", "translation": "Additionele informatie"}, "10": {"tag": "treatments", "translation": "Behandelingen"}, "11": {"tag": "personal", "translation": "Persoonlijke informatie"}, "12": {"tag": "all", "translation": "Alle"}}');
insert into zmc.translated_tags (tags) values ('{"wearable": {"translation": "Wearable/Sensor"}, "diagnostic": {"translation": "Diagnostiek"}, "patient_details": {"translation": "Patiënten informatie"}, "patient_address": {"translation": "Adres van de patiënt"}, "appointments": {"translation": "Afspraken"}, "operations": {"translation": "Operaties"}, "documents": {"translation": "Documenten"}, "drugs_and_alcohol": {"translation": "Drugs en alcohol"}, "allergies": {"translation": "Allergieën"}, "additional_information": {"translation": "Additionele informatie"}, "treatments": {"translation": "Behandelingen"}, "personal": {"translation": "Persoonlijke informatie"}, "all": {"translation": "Alle"}}');


insert into zmc.hospital_doctors (id, name, specialism) values (1, 'Lucas De Vries', 1);
insert into zmc.hospital_doctors (id, name, specialism) values (2, 'Milan Van de Berg', 1);
insert into zmc.hospital_doctors (id, name, specialism) values (3, 'Emma Bakker', 1);
insert into zmc.hospital_doctors (id, name, specialism) values (4, 'Sophie Janssen', 1);
insert into zmc.hospital_doctors (id, name, specialism) values (5, 'Levi Van Dijk', 2);
insert into zmc.hospital_doctors (id, name, specialism) values (6, 'Julia Visser', 2);
insert into zmc.hospital_doctors (id, name, specialism) values (7, 'Sem Jansen', 2);
insert into zmc.hospital_doctors (id, name, specialism) values (8, 'Mila Meyer', 3);
insert into zmc.hospital_doctors (id, name, specialism) values (9, 'Anna Smit', 3);
insert into zmc.hospital_doctors (id, name, specialism) values (10, 'Daan De Jong', 3);



