insert into zmc.patient_details (patnr,gschl,nname,nnams,vname,titel,namzu,gbdat,gbnam,gbnas,gland,natio,land,pstlz,ort,stras,telf1
) values (1075835,'male','Peter','Tester','P.J.','Dhr',NULL,'04.01.1950', NULL,'Peter','NL','NL','NL','2986 VA','Ridderkerk','Koolmees 13 A','06-21185097');

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


insert into zmc.patient_measurements (patnr, height, weight, date) values (1075835, 165, 75, '2018-09-20');


insert into zmc.patient_documents (patnr, report_title, department, date, content) values (1075835, 'Verwijzing van Huisarts', 'Doctor''s brief', '2020-08-20', 'Patiënt heeft een stekende pijn bij rechter heup en heeft een consult nodig met de specialist');


insert into zmc.patient_appointments (patnr, type, date, notes) values (1075835, 'Consult', '2020-09-01', 'Stekende pijn aan de rechterkant van de heup. Heeft totale heup vervanging nodig');
insert into zmc.patient_appointments (patnr, type, date, notes) values (1075835, '6 Weekse controle', '2020-10-26', 'Voortgang bijgehouden m.b.v Activity Monitor. Geen fysiek consult nodig');


insert into zmc.patient_operations (patnr, anatomical_location, date, notes) values (1075835, 'Rechter heup', '2020-09-20', 'Zie operatieverslag');


insert into zmc.patient_warnings (patnr, alerts, begin_date, type) values (1075835, 'Pacemaker', '2015-06-01', 'Conditie');


insert into zmc.patient_functional_state (patnr, name, value, date) values (1075835, 'Bevindingen t.a.v. gehoor', 'Gehoor problemen', '2018-08-25');


insert into zmc.patient_living_situation (patnr, house_type, description) values (1075835, 'Eengezinswoning', NULL);


insert into zmc.patient_drug_use (patnr, substance, quantity, description) values (1075835, NULL, NULL, NULL);


insert into zmc.patient_alcohol_use (patnr, usage_status, quantity,description) values (1075835, NULL, NULL, NULL);


insert into zmc.patient_tobacco_use (patnr, substance, description) values (1075835, 'Sigaretten (Ex-roker)', 20);


insert into zmc.patient_allergies_intolerance (patnr, caustic_substance, critical, description) values (1075835, 'Jodium', 'Gemiddeld', 'Lokale irritaties en jeuk');


insert into zmc.patient_diagnostic (patnr, type, name, anatomical_location, laterality, begin_date, end_date) values (1075835, 'Diagnosis', 'Coxartrose', 'Rechter heup', 'Nee', '2020-09-01', '2020-11-27');


insert into zmc.patient_rules (rule_id, serums_id, tags, filters) values ('abc', 1, ARRAY['all'], '{}');

insert into zmc.serums_ids (serums_id, patnr) values (1, 1075835);

insert into zmc.hospital_tags (tags) values (ARRAY['wearable', 'diagnostic', 'patient_details', 'patient_address', 'appointments', 'operations', 'documents', 'drugs_and_alcohol', 'allergies', 'additional_information', 'treatments', 'personal', 'all']);

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



