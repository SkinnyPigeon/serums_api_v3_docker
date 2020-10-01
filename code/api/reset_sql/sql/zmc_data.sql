insert into zmc.patient_details (patnr,gschl,nname,nnams,vname,titel,namzu,gbdat,gbnam,gbnas,gland,natio,land,pstlz,ort,stras,telf1
) values (1075835,2,'Calimerass','CALIMERASS','TSTO',NULL,NULL,'04.01.1980','Test PTE - IMS Team.','TESTPTE-IMSTEAM.','NL','NL','NL','2986 VA','Ridderkerk','Koolmees 13 A bus 5','06-21185097');


insert into zmc.wearable (patnr,day_nr,time_total,time_passive,time_active,time_sit,time_stand,time_walk,time_cycle,time_hi,nr_sst,steps_total,cadence,cyc_rot,cyc_rpm
) values (1075835,1,41300,35849,5449,31045,4804,5071,378,0,45,6047,77,245,39);

insert into zmc.wearable (patnr,day_nr,time_total,time_passive,time_active,time_sit,time_stand,time_walk,time_cycle,time_hi,nr_sst,steps_total,cadence,cyc_rot,cyc_rpm
) values (1075835,2,42674,37939,4733,31227,6712,4733,0,0,39,5885,80,0,0);

insert into zmc.wearable (patnr,day_nr,time_total,time_passive,time_active,time_sit,time_stand,time_walk,time_cycle,time_hi,nr_sst,steps_total,cadence,cyc_rot,cyc_rpm
) values (1075835,3,41071,36401,4668,31652,4749,4668,0,0,33,5892,76,0,0);

insert into zmc.wearable (patnr,day_nr,time_total,time_passive,time_active,time_sit,time_stand,time_walk,time_cycle,time_hi,nr_sst,steps_total,cadence,cyc_rot,cyc_rpm
) values (1075835,4,45420,40762,4655,34417,6345,4655,0,0,46,6000,81,0,0);


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


insert into zmc.patient_rules (rule_id, tags, filters) values (1, ARRAY['wearable', 'personal'], '{}');
insert into zmc.patient_rules (rule_id, tags, filters) values (2, ARRAY['patient_details'], '{}');
insert into zmc.patient_rules (rule_id, tags, filters) values (3, ARRAY['personal'], '{}');
insert into zmc.patient_rules (rule_id, tags, filters) values (4, ARRAY['wearable', 'personal'], '{"day_nr": 2}');


insert into zmc.serums_ids (serums_id, patnr) values (1, 1075835);

