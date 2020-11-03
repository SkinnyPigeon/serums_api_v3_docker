insert into fcrb.diagnostic (einri,	patnr, falnr, lfdnr, dkey1, pernr) values ('HCPB', 4641202, 988392719, 3, 'E11.9', 2827346);

insert into fcrb.diagnostic (einri,	patnr, falnr, lfdnr, dkey1, pernr) values ('HCPB', 4641202, 98823483, 2, 'I25.9', 8405937);


insert into fcrb.episode (einri, falnr, falar, patnr, bekat, einzg, statu, krzan, enddt, erdat, pernr, storn, begdt, casetx, fatnx, enddtx) 
values ('HCPB', 988392719, 1, 4641202, 'HDiabetología', 363814, 'I', '', NULL, '1991-09-23', 2827346, '', '1991-09-23', 'AMBULANTE', 'ENDOCRINOLOGÍA Y NUTRICIÓN', '');

insert into fcrb.episode (einri, falnr, falar, patnr, bekat, einzg, statu, krzan, enddt, erdat, pernr, storn, begdt, casetx, fatnx, enddtx) 
values ('HCPB', 89439002, 1, 4641202, 'CARDIO REPÒS', 84747, 'I', 'X', NULL, '2019-05-15', 8405937, '', '2019-05-15', 'AMBULANTE', 'CARDIOLOGIA', '');

insert into fcrb.episode (einri, falnr, falar, patnr, bekat, einzg, statu, krzan, enddt, erdat, pernr, storn, begdt, casetx, fatnx, enddtx) 
values ('HCPB', 96823483, 1, 4641202, 'Mamografía', 94848, 'I', '', '2015-02-11', '2015-02-11', 1239828,'', '2015-02-11', 'URGENTE', 'ONCOLOGÍA', '');


insert into fcrb.medical_specialty (orgid, orgna) values ('H-END', 'ENDOCRINOLOGIA');
insert into fcrb.medical_specialty (orgid, orgna) values ('H-CAR', 'CARDIOLOGIA');
insert into fcrb.medical_specialty (orgid, orgna) values ('H-MMG', 'R05A MAMOGRAFIES');


insert into fcrb.medication (einri, patnr, falnr, pernr, motx, mostx, motypid, mpresnr, erdat, storn, stusr, stdat, stoid) 
values ('HCPB', 4641202, 98823483, 8405937, 'ENALAPRIL, 100 MG/3 SOBR 5ML', 'Tres al dia durante dos semanas', '', '', '2019-05-15', '', '', '2019-05-30', 'Alta');


insert into fcrb.monitoring_parameters (patnr, falnr, vppid, pernr, vbem, datyp, wertogr, wertugr, wertmax, wertmin) 
values (4641202, 988392719, 'GLIC_CAPIL', 2827346, 'El paciente debe estar entre los límites', '2019-05-05', 180, 60, 190, 50);


insert into fcrb.vital_signs (patnr, falnr, idvs, vppid, dttyp, erdat, vptim, typevs, vwert, vbem) 
values (4641202 ,988392719 ,6872437 ,'GLIC_CAPIL' ,'INT' ,'2020-03-04' ,'04:44:05' ,'EXTERNO' ,148 ,NULL);	
insert into fcrb.vital_signs (patnr, falnr, idvs, vppid, dttyp, erdat, vptim, typevs, vwert, vbem) 
values (4641202 ,988392719 ,6872608 ,'GLIC_CAPIL' ,'INT' ,'2020-02-08' ,'00:13:18' ,'EXTERNO' ,153 ,'');	
insert into fcrb.vital_signs (patnr, falnr, idvs, vppid, dttyp, erdat, vptim, typevs, vwert, vbem) 
values (4641202 ,988392719 ,6872687 ,'GLIC_CAPIL' ,'INT' ,'2019-10-16' ,'08:06:57' ,'EXTERNO' ,111 ,'');	
insert into fcrb.vital_signs (patnr, falnr, idvs, vppid, dttyp, erdat, vptim, typevs, vwert, vbem) 
values (4641202 ,988392719 ,6872726 ,'GLIC_CAPIL' ,'INT' ,'2019-09-29' ,'17:30:55' ,'EXTERNO' ,77 ,'');	
insert into fcrb.vital_signs (patnr, falnr, idvs, vppid, dttyp, erdat, vptim, typevs, vwert, vbem) 
values (4641202 ,988392719 ,6872873 ,'GLIC_CAPIL' ,'INT' ,'2019-10-16' ,'14:16:25' ,'EXTERNO' ,152 ,'');	
insert into fcrb.vital_signs (patnr, falnr, idvs, vppid, dttyp, erdat, vptim, typevs, vwert, vbem) 
values (4641202 ,988392719 ,6873012 ,'GLIC_CAPIL' ,'INT' ,'2019-04-28' ,'11:21:50' ,'EXTERNO' ,89 ,'');	
insert into fcrb.vital_signs (patnr, falnr, idvs, vppid, dttyp, erdat, vptim, typevs, vwert, vbem) 
values (4641202 ,988392719 ,6873029 ,'GLIC_CAPIL' ,'INT' ,'2019-12-02' ,'12:37:31' ,'EXTERNO' ,100 ,'');	
insert into fcrb.vital_signs (patnr, falnr, idvs, vppid, dttyp, erdat, vptim, typevs, vwert, vbem) 
values (4641202 ,988392719 ,6873221 ,'GLIC_CAPIL' ,'INT' ,'2019-12-16' ,'07:54:52' ,'EXTERNO' ,86 ,'');	
insert into fcrb.vital_signs (patnr, falnr, idvs, vppid, dttyp, erdat, vptim, typevs, vwert, vbem) 
values (4641202 ,988392719 ,6873322 ,'GLIC_CAPIL' ,'INT' ,'2019-05-26' ,'09:51:39' ,'EXTERNO' ,136 ,'');	
insert into fcrb.vital_signs (patnr, falnr, idvs, vppid, dttyp, erdat, vptim, typevs, vwert, vbem) 
values (4641202 ,988392719 ,6873347 ,'GLIC_CAPIL' ,'INT' ,'2019-06-30' ,'07:00:02' ,'EXTERNO' ,137 ,'');	
insert into fcrb.vital_signs (patnr, falnr, idvs, vppid, dttyp, erdat, vptim, typevs, vwert, vbem) 
values (4641202 ,988392719 ,6873524 ,'GLIC_CAPIL' ,'INT' ,'2020-03-29' ,'09:20:19' ,'EXTERNO' ,78 ,'');	
insert into fcrb.vital_signs (patnr, falnr, idvs, vppid, dttyp, erdat, vptim, typevs, vwert, vbem) 
values (4641202 ,988392719 ,6873574 ,'GLIC_CAPIL' ,'INT' ,'2019-12-01' ,'13:42:05' ,'EXTERNO' ,161 ,'');	
insert into fcrb.vital_signs (patnr, falnr, idvs, vppid, dttyp, erdat, vptim, typevs, vwert, vbem) 
values (4641202 ,988392719 ,6873654 ,'GLIC_CAPIL' ,'INT' ,'2019-05-15' ,'15:38:01' ,'EXTERNO' ,164 ,'');	
insert into fcrb.vital_signs (patnr, falnr, idvs, vppid, dttyp, erdat, vptim, typevs, vwert, vbem) 
values (4641202 ,988392719 ,6873789 ,'GLIC_CAPIL' ,'INT' ,'2020-05-10' ,'00:32:50' ,'EXTERNO' ,172 ,'');	
insert into fcrb.vital_signs (patnr, falnr, idvs, vppid, dttyp, erdat, vptim, typevs, vwert, vbem) 
values (4641202 ,988392719 ,6873930 ,'GLIC_CAPIL' ,'INT' ,'2019-04-10' ,'00:16:46' ,'EXTERNO' ,73 ,'');	
insert into fcrb.vital_signs (patnr, falnr, idvs, vppid, dttyp, erdat, vptim, typevs, vwert, vbem) 
values (4641202 ,988392719 ,6874025 ,'GLIC_CAPIL' ,'INT' ,'2019-07-03' ,'12:16:17' ,'EXTERNO' ,178 ,'');	
insert into fcrb.vital_signs (patnr, falnr, idvs, vppid, dttyp, erdat, vptim, typevs, vwert, vbem) 
values (4641202 ,988392719 ,6874110 ,'GLIC_CAPIL' ,'INT' ,'2019-08-23' ,'06:53:54' ,'EXTERNO' ,175 ,'');	
insert into fcrb.vital_signs (patnr, falnr, idvs, vppid, dttyp, erdat, vptim, typevs, vwert, vbem) 
values (4641202 ,988392719 ,6874142 ,'GLIC_CAPIL' ,'INT' ,'2019-08-08' ,'19:38:29' ,'EXTERNO' ,77 ,'');	
insert into fcrb.vital_signs (patnr, falnr, idvs, vppid, dttyp, erdat, vptim, typevs, vwert, vbem) 
values (4641202 ,988392719 ,6874289 ,'GLIC_CAPIL' ,'INT' ,'2019-09-16' ,'10:45:19' ,'EXTERNO' ,166 ,'');	
insert into fcrb.vital_signs (patnr, falnr, idvs, vppid, dttyp, erdat, vptim, typevs, vwert, vbem) 
values (4641202 ,988392719 ,6874417 ,'GLIC_CAPIL' ,'INT' ,'2020-03-26' ,'19:17:22' ,'EXTERNO' ,179 ,'');	
insert into fcrb.vital_signs (patnr, falnr, idvs, vppid, dttyp, erdat, vptim, typevs, vwert, vbem) 
values (4641202 ,988392719 ,6874509 ,'GLIC_CAPIL' ,'INT' ,'2020-02-13' ,'22:25:15' ,'EXTERNO' ,103 ,'');	
insert into fcrb.vital_signs (patnr, falnr, idvs, vppid, dttyp, erdat, vptim, typevs, vwert, vbem) 
values (4641202 ,988392719 ,6874623 ,'GLIC_CAPIL' ,'INT' ,'2019-09-10' ,'14:32:01' ,'EXTERNO' ,93 ,'');	
insert into fcrb.vital_signs (patnr, falnr, idvs, vppid, dttyp, erdat, vptim, typevs, vwert, vbem) 
values (4641202 ,988392719 ,6874690 ,'GLIC_CAPIL' ,'INT' ,'2019-10-18' ,'03:14:30' ,'EXTERNO' ,116 ,'');	
insert into fcrb.vital_signs (patnr, falnr, idvs, vppid, dttyp, erdat, vptim, typevs, vwert, vbem) 
values (4641202 ,988392719 ,6874785 ,'GLIC_CAPIL' ,'INT' ,'2019-12-17' ,'01:11:35' ,'EXTERNO' ,104 ,'');	
insert into fcrb.vital_signs (patnr, falnr, idvs, vppid, dttyp, erdat, vptim, typevs, vwert, vbem) 
values (4641202 ,988392719 ,6874920 ,'GLIC_CAPIL' ,'INT' ,'2019-12-21' ,'20:21:25' ,'EXTERNO' ,103 ,'');	
insert into fcrb.vital_signs (patnr, falnr, idvs, vppid, dttyp, erdat, vptim, typevs, vwert, vbem) 
values (4641202 ,988392719 ,6875043 ,'GLIC_CAPIL' ,'INT' ,'2019-09-06' ,'17:38:38' ,'EXTERNO' ,75 ,'');	
insert into fcrb.vital_signs (patnr, falnr, idvs, vppid, dttyp, erdat, vptim, typevs, vwert, vbem) 
values (4641202 ,988392719 ,6875124 ,'GLIC_CAPIL' ,'INT' ,'2020-01-24' ,'17:15:22' ,'EXTERNO' ,163 ,'');	
insert into fcrb.vital_signs (patnr, falnr, idvs, vppid, dttyp, erdat, vptim, typevs, vwert, vbem) 
values (4641202 ,988392719 ,6875238 ,'GLIC_CAPIL' ,'INT' ,'2019-10-11' ,'18:01:01' ,'EXTERNO' ,72 ,'');	
insert into fcrb.vital_signs (patnr, falnr, idvs, vppid, dttyp, erdat, vptim, typevs, vwert, vbem) 
values (4641202 ,988392719 ,6875260 ,'GLIC_CAPIL' ,'INT' ,'2019-11-15' ,'07:03:01' ,'EXTERNO' ,174 ,'');	
insert into fcrb.vital_signs (patnr, falnr, idvs, vppid, dttyp, erdat, vptim, typevs, vwert, vbem) 
values (4641202 ,988392719 ,6875369 ,'GLIC_CAPIL' ,'INT' ,'2019-07-25' ,'17:38:43' ,'EXTERNO' ,108 ,'');	
insert into fcrb.vital_signs (patnr, falnr, idvs, vppid, dttyp, erdat, vptim, typevs, vwert, vbem) 
values (4641202 ,988392719 ,6875467 ,'GLIC_CAPIL' ,'INT' ,'2019-09-04' ,'17:17:28' ,'EXTERNO' ,153 ,'');	
insert into fcrb.vital_signs (patnr, falnr, idvs, vppid, dttyp, erdat, vptim, typevs, vwert, vbem) 
values (4641202 ,988392719 ,6875588 ,'GLIC_CAPIL' ,'INT' ,'2020-02-12' ,'17:49:03' ,'EXTERNO' ,73 ,'');	
insert into fcrb.vital_signs (patnr, falnr, idvs, vppid, dttyp, erdat, vptim, typevs, vwert, vbem) 
values (4641202 ,988392719 ,6875678 ,'GLIC_CAPIL' ,'INT' ,'2019-04-30' ,'09:35:11' ,'EXTERNO' ,96 ,'');	
insert into fcrb.vital_signs (patnr, falnr, idvs, vppid, dttyp, erdat, vptim, typevs, vwert, vbem) 
values (4641202 ,988392719 ,6875854 ,'GLIC_CAPIL' ,'INT' ,'2019-12-10' ,'03:34:03' ,'EXTERNO' ,137 ,'');	
insert into fcrb.vital_signs (patnr, falnr, idvs, vppid, dttyp, erdat, vptim, typevs, vwert, vbem) 
values (4641202 ,988392719 ,6875887 ,'GLIC_CAPIL' ,'INT' ,'2019-08-17' ,'23:44:13' ,'EXTERNO' ,69 ,'');	
insert into fcrb.vital_signs (patnr, falnr, idvs, vppid, dttyp, erdat, vptim, typevs, vwert, vbem) 
values (4641202 ,988392719 ,6876001 ,'GLIC_CAPIL' ,'INT' ,'2020-01-04' ,'03:42:09' ,'EXTERNO' ,175 ,'');	
insert into fcrb.vital_signs (patnr, falnr, idvs, vppid, dttyp, erdat, vptim, typevs, vwert, vbem) 
values (4641202 ,988392719 ,6876122 ,'GLIC_CAPIL' ,'INT' ,'2020-01-24' ,'03:58:41' ,'EXTERNO' ,98 ,'');	
insert into fcrb.vital_signs (patnr, falnr, idvs, vppid, dttyp, erdat, vptim, typevs, vwert, vbem) 
values (4641202 ,988392719 ,6876204 ,'GLIC_CAPIL' ,'INT' ,'2020-02-12' ,'21:15:01' ,'EXTERNO' ,88 ,'');	
insert into fcrb.vital_signs (patnr, falnr, idvs, vppid, dttyp, erdat, vptim, typevs, vwert, vbem) 
values (4641202 ,988392719 ,6876299 ,'GLIC_CAPIL' ,'INT' ,'2020-03-31' ,'11:18:33' ,'EXTERNO' ,145 ,'');	
insert into fcrb.vital_signs (patnr, falnr, idvs, vppid, dttyp, erdat, vptim, typevs, vwert, vbem) 
values (4641202 ,988392719 ,6876424 ,'GLIC_CAPIL' ,'INT' ,'2020-03-10' ,'09:03:05' ,'EXTERNO' ,125 ,'');	
insert into fcrb.vital_signs (patnr, falnr, idvs, vppid, dttyp, erdat, vptim, typevs, vwert, vbem) 
values (4641202 ,988392719 ,6876505 ,'GLIC_CAPIL' ,'INT' ,'2019-12-18' ,'20:02:03' ,'EXTERNO' ,172 ,'');	
insert into fcrb.vital_signs (patnr, falnr, idvs, vppid, dttyp, erdat, vptim, typevs, vwert, vbem) 
values (4641202 ,988392719 ,6876602 ,'GLIC_CAPIL' ,'INT' ,'2020-01-16' ,'06:48:25' ,'EXTERNO' ,108 ,'');	
insert into fcrb.vital_signs (patnr, falnr, idvs, vppid, dttyp, erdat, vptim, typevs, vwert, vbem) 
values (4641202 ,988392719 ,6876683 ,'GLIC_CAPIL' ,'INT' ,'2019-11-30' ,'18:08:40' ,'EXTERNO' ,151 ,'');	
insert into fcrb.vital_signs (patnr, falnr, idvs, vppid, dttyp, erdat, vptim, typevs, vwert, vbem) 
values (4641202 ,988392719 ,6876835 ,'GLIC_CAPIL' ,'INT' ,'2020-05-28' ,'10:44:29' ,'EXTERNO' ,143 ,'');	
insert into fcrb.vital_signs (patnr, falnr, idvs, vppid, dttyp, erdat, vptim, typevs, vwert, vbem) 
values (4641202 ,988392719 ,6876897 ,'GLIC_CAPIL' ,'INT' ,'2020-03-02' ,'05:50:37' ,'EXTERNO' ,130 ,'');	
insert into fcrb.vital_signs (patnr, falnr, idvs, vppid, dttyp, erdat, vptim, typevs, vwert, vbem) 
values (4641202 ,988392719 ,6877019 ,'GLIC_CAPIL' ,'INT' ,'2019-09-20' ,'10:08:34' ,'EXTERNO' ,164 ,'');	
insert into fcrb.vital_signs (patnr, falnr, idvs, vppid, dttyp, erdat, vptim, typevs, vwert, vbem) 
values (4641202 ,988392719 ,6877097 ,'GLIC_CAPIL' ,'INT' ,'2019-10-22' ,'02:26:41' ,'EXTERNO' ,135 ,'');	
insert into fcrb.vital_signs (patnr, falnr, idvs, vppid, dttyp, erdat, vptim, typevs, vwert, vbem) 
values (4641202 ,988392719 ,6877250 ,'GLIC_CAPIL' ,'INT' ,'2019-04-07' ,'21:30:16' ,'EXTERNO' ,154 ,'');	
insert into fcrb.vital_signs (patnr, falnr, idvs, vppid, dttyp, erdat, vptim, typevs, vwert, vbem) 
values (4641202 ,988392719 ,6877299 ,'GLIC_CAPIL' ,'INT' ,'2019-04-05' ,'06:46:10' ,'EXTERNO' ,79 ,'');	
insert into fcrb.vital_signs (patnr, falnr, idvs, vppid, dttyp, erdat, vptim, typevs, vwert, vbem) 
values (4641202 ,988392719 ,6877401 ,'GLIC_CAPIL' ,'INT' ,'2019-10-22' ,'03:53:56' ,'EXTERNO' ,86 ,'');	
insert into fcrb.vital_signs (patnr, falnr, idvs, vppid, dttyp, erdat, vptim, typevs, vwert, vbem) 
values (4641202 ,98823483 ,9854393 ,'PULSIOX' ,'INT' ,'2019-12-24' ,'18:29:19' ,'EXTERNO' ,95 ,'');	
insert into fcrb.vital_signs (patnr, falnr, idvs, vppid, dttyp, erdat, vptim, typevs, vwert, vbem) 
values (4641202 ,98823483 ,9854445 ,'PULSIOX' ,'INT' ,'2019-04-26' ,'05:34:24' ,'EXTERNO' ,90 ,'');	
insert into fcrb.vital_signs (patnr, falnr, idvs, vppid, dttyp, erdat, vptim, typevs, vwert, vbem) 
values (4641202 ,98823483 ,9854550 ,'PULSIOX' ,'INT' ,'2020-03-26' ,'21:42:26' ,'EXTERNO' ,91 ,'');	
insert into fcrb.vital_signs (patnr, falnr, idvs, vppid, dttyp, erdat, vptim, typevs, vwert, vbem) 
values (4641202 ,98823483 ,9854637 ,'PULSIOX' ,'INT' ,'2019-12-06' ,'17:41:08' ,'EXTERNO' ,86 ,'');	
insert into fcrb.vital_signs (patnr, falnr, idvs, vppid, dttyp, erdat, vptim, typevs, vwert, vbem) 
values (4641202 ,98823483 ,9854713 ,'PULSIOX' ,'INT' ,'2019-06-08' ,'20:08:17' ,'EXTERNO' ,88 ,'');	
insert into fcrb.vital_signs (patnr, falnr, idvs, vppid, dttyp, erdat, vptim, typevs, vwert, vbem) 
values (4641202 ,98823483 ,9854838 ,'PULSIOX' ,'INT' ,'2019-10-27' ,'19:10:23' ,'EXTERNO' ,91 ,'');	
insert into fcrb.vital_signs (patnr, falnr, idvs, vppid, dttyp, erdat, vptim, typevs, vwert, vbem) 
values (4641202 ,98823483 ,9854988 ,'PULSIOX' ,'INT' ,'2019-10-27' ,'08:36:17' ,'EXTERNO' ,88 ,'');	
insert into fcrb.vital_signs (patnr, falnr, idvs, vppid, dttyp, erdat, vptim, typevs, vwert, vbem) 
values (4641202 ,98823483 ,9855095 ,'PULSIOX' ,'INT' ,'2019-09-22' ,'19:39:03' ,'EXTERNO' ,90 ,'');	
insert into fcrb.vital_signs (patnr, falnr, idvs, vppid, dttyp, erdat, vptim, typevs, vwert, vbem) 
values (4641202 ,98823483 ,9855165 ,'PULSIOX' ,'INT' ,'2020-04-30' ,'22:38:48' ,'EXTERNO' ,85 ,'');	
insert into fcrb.vital_signs (patnr, falnr, idvs, vppid, dttyp, erdat, vptim, typevs, vwert, vbem) 
values (4641202 ,98823483 ,9855255 ,'PULSIOX' ,'INT' ,'2020-05-10' ,'04:53:32' ,'EXTERNO' ,89 ,'');	
insert into fcrb.vital_signs (patnr, falnr, idvs, vppid, dttyp, erdat, vptim, typevs, vwert, vbem) 
values (4641202 ,98823483 ,9855386 ,'PULSIOX' ,'INT' ,'2019-05-28' ,'03:03:16' ,'EXTERNO' ,95 ,'');	
insert into fcrb.vital_signs (patnr, falnr, idvs, vppid, dttyp, erdat, vptim, typevs, vwert, vbem) 
values (4641202 ,98823483 ,9855473 ,'PULSIOX' ,'INT' ,'2019-09-12' ,'00:00:53' ,'EXTERNO' ,97 ,'');	
insert into fcrb.vital_signs (patnr, falnr, idvs, vppid, dttyp, erdat, vptim, typevs, vwert, vbem) 
values (4641202 ,98823483 ,9855567 ,'PULSIOX' ,'INT' ,'2019-12-30' ,'17:10:03' ,'EXTERNO' ,87 ,'');	
insert into fcrb.vital_signs (patnr, falnr, idvs, vppid, dttyp, erdat, vptim, typevs, vwert, vbem) 
values (4641202 ,98823483 ,9855666 ,'PULSIOX' ,'INT' ,'2020-01-25' ,'19:39:14' ,'EXTERNO' ,96 ,'');	
insert into fcrb.vital_signs (patnr, falnr, idvs, vppid, dttyp, erdat, vptim, typevs, vwert, vbem) 
values (4641202 ,98823483 ,9855732 ,'PULSIOX' ,'INT' ,'2020-05-26' ,'10:19:56' ,'EXTERNO' ,87 ,'');	
insert into fcrb.vital_signs (patnr, falnr, idvs, vppid, dttyp, erdat, vptim, typevs, vwert, vbem) 
values (4641202 ,98823483 ,9855862 ,'PULSIOX' ,'INT' ,'2019-11-01' ,'19:58:07' ,'EXTERNO' ,98 ,'');	
insert into fcrb.vital_signs (patnr, falnr, idvs, vppid, dttyp, erdat, vptim, typevs, vwert, vbem) 
values (4641202 ,98823483 ,9855977 ,'PULSIOX' ,'INT' ,'2019-10-25' ,'15:55:36' ,'EXTERNO' ,97 ,'');	
insert into fcrb.vital_signs (patnr, falnr, idvs, vppid, dttyp, erdat, vptim, typevs, vwert, vbem) 
values (4641202 ,98823483 ,9856036 ,'PULSIOX' ,'INT' ,'2020-02-21' ,'07:19:29' ,'EXTERNO' ,88 ,'');	
insert into fcrb.vital_signs (patnr, falnr, idvs, vppid, dttyp, erdat, vptim, typevs, vwert, vbem) 
values (4641202 ,98823483 ,9856169 ,'PULSIOX' ,'INT' ,'2019-10-27' ,'23:23:55' ,'EXTERNO' ,93 ,'');	
insert into fcrb.vital_signs (patnr, falnr, idvs, vppid, dttyp, erdat, vptim, typevs, vwert, vbem) 
values (4641202 ,98823483 ,9856246 ,'PULSIOX' ,'INT' ,'2020-05-24' ,'20:51:09' ,'EXTERNO' ,85 ,'');	
insert into fcrb.vital_signs (patnr, falnr, idvs, vppid, dttyp, erdat, vptim, typevs, vwert, vbem) 
values (4641202 ,98823483 ,9856353 ,'PULSIOX' ,'INT' ,'2019-10-24' ,'18:52:38' ,'EXTERNO' ,98 ,'');	
insert into fcrb.vital_signs (patnr, falnr, idvs, vppid, dttyp, erdat, vptim, typevs, vwert, vbem) 
values (4641202 ,98823483 ,9856499 ,'PULSIOX' ,'INT' ,'2020-05-05' ,'18:44:37' ,'EXTERNO' ,86 ,'');	
insert into fcrb.vital_signs (patnr, falnr, idvs, vppid, dttyp, erdat, vptim, typevs, vwert, vbem) 
values (4641202 ,98823483 ,9856553 ,'PULSIOX' ,'INT' ,'2019-07-18' ,'18:06:42' ,'EXTERNO' ,93 ,'');
insert into fcrb.vital_signs (patnr, falnr, idvs, vppid, dttyp, erdat, vptim, typevs, vwert, vbem) 
values (4641202 ,98823483 ,9856698 ,'PULSIOX' ,'INT' ,'2020-02-09' ,'14:10:56' ,'EXTERNO' ,91 ,'');	
insert into fcrb.vital_signs (patnr, falnr, idvs, vppid, dttyp, erdat, vptim, typevs, vwert, vbem) 
values (4641202 ,98823483 ,9856729 ,'PULSIOX' ,'INT' ,'2020-05-28' ,'00:59:59' ,'EXTERNO' ,91 ,'');	
insert into fcrb.vital_signs (patnr, falnr, idvs, vppid, dttyp, erdat, vptim, typevs, vwert, vbem) 
values (4641202 ,98823483 ,9856851 ,'PULSIOX' ,'INT' ,'2019-05-29' ,'15:29:36' ,'EXTERNO' ,94 ,'');	
insert into fcrb.vital_signs (patnr, falnr, idvs, vppid, dttyp, erdat, vptim, typevs, vwert, vbem) 
values (4641202 ,98823483 ,9857020 ,'PULSIOX' ,'INT' ,'2020-04-03' ,'10:37:45' ,'EXTERNO' ,89 ,'');	
insert into fcrb.vital_signs (patnr, falnr, idvs, vppid, dttyp, erdat, vptim, typevs, vwert, vbem) 
values (4641202 ,98823483 ,9857061 ,'PULSIOX' ,'INT' ,'2019-10-03' ,'14:35:32' ,'EXTERNO' ,87 ,'');	
insert into fcrb.vital_signs (patnr, falnr, idvs, vppid, dttyp, erdat, vptim, typevs, vwert, vbem) 
values (4641202 ,98823483 ,9857140 ,'PULSIOX' ,'INT' ,'2019-05-03' ,'00:23:33' ,'EXTERNO' ,94 ,'');	
insert into fcrb.vital_signs (patnr, falnr, idvs, vppid, dttyp, erdat, vptim, typevs, vwert, vbem) 
values (4641202 ,98823483 ,9857233 ,'PULSIOX' ,'INT' ,'2020-04-22' ,'00:41:31' ,'EXTERNO' ,89 ,'');	
insert into fcrb.vital_signs (patnr, falnr, idvs, vppid, dttyp, erdat, vptim, typevs, vwert, vbem) 
values (4641202 ,98823483 ,9857429 ,'PULSIOX' ,'INT' ,'2019-09-24' ,'00:36:20' ,'EXTERNO' ,96 ,'');	
insert into fcrb.vital_signs (patnr, falnr, idvs, vppid, dttyp, erdat, vptim, typevs, vwert, vbem) 
values (4641202 ,98823483 ,9857506 ,'PULSIOX' ,'INT' ,'2020-03-04' ,'17:20:02' ,'EXTERNO' ,85 ,'');	
insert into fcrb.vital_signs (patnr, falnr, idvs, vppid, dttyp, erdat, vptim, typevs, vwert, vbem) 
values (4641202 ,98823483 ,9857549 ,'PULSIOX' ,'INT' ,'2019-05-30' ,'15:59:05' ,'EXTERNO' ,92 ,'');	
insert into fcrb.vital_signs (patnr, falnr, idvs, vppid, dttyp, erdat, vptim, typevs, vwert, vbem) 
values (4641202 ,98823483 ,9857657 ,'PULSIOX' ,'INT' ,'2019-07-16' ,'07:24:31' ,'EXTERNO' ,86 ,'');	
insert into fcrb.vital_signs (patnr, falnr, idvs, vppid, dttyp, erdat, vptim, typevs, vwert, vbem) 
values (4641202 ,98823483 ,9857808 ,'PULSIOX' ,'INT' ,'2019-11-29' ,'07:36:01' ,'EXTERNO' ,87 ,'');	
insert into fcrb.vital_signs (patnr, falnr, idvs, vppid, dttyp, erdat, vptim, typevs, vwert, vbem) 
values (4641202 ,98823483 ,9857907 ,'PULSIOX' ,'INT' ,'2019-08-13' ,'09:54:57' ,'EXTERNO' ,91 ,'');	
insert into fcrb.vital_signs (patnr, falnr, idvs, vppid, dttyp, erdat, vptim, typevs, vwert, vbem) 
values (4641202 ,98823483 ,9858021 ,'PULSIOX' ,'INT' ,'2019-11-03' ,'03:50:19' ,'EXTERNO' ,97 ,'');	
insert into fcrb.vital_signs (patnr, falnr, idvs, vppid, dttyp, erdat, vptim, typevs, vwert, vbem) 
values (4641202 ,98823483 ,9858085 ,'PULSIOX' ,'INT' ,'2019-08-04' ,'20:35:48' ,'EXTERNO' ,98 ,'');	
insert into fcrb.vital_signs (patnr, falnr, idvs, vppid, dttyp, erdat, vptim, typevs, vwert, vbem) 
values (4641202 ,98823483 ,9858207 ,'PULSIOX' ,'INT' ,'2019-06-26' ,'21:20:26' ,'EXTERNO' ,86 ,'');	
insert into fcrb.vital_signs (patnr, falnr, idvs, vppid, dttyp, erdat, vptim, typevs, vwert, vbem) 
values (4641202 ,98823483 ,9858316 ,'PULSIOX' ,'INT' ,'2019-11-18' ,'05:01:35' ,'EXTERNO' ,90 ,'');	
insert into fcrb.vital_signs (patnr, falnr, idvs, vppid, dttyp, erdat, vptim, typevs, vwert, vbem) 
values (4641202 ,98823483 ,9858372 ,'PULSIOX' ,'INT' ,'2020-05-16' ,'23:34:23' ,'EXTERNO' ,94 ,'');	
insert into fcrb.vital_signs (patnr, falnr, idvs, vppid, dttyp, erdat, vptim, typevs, vwert, vbem) 
values (4641202 ,98823483 ,9858489 ,'PULSIOX' ,'INT' ,'2019-08-25' ,'20:03:22' ,'EXTERNO' ,98 ,'');	
insert into fcrb.vital_signs (patnr, falnr, idvs, vppid, dttyp, erdat, vptim, typevs, vwert, vbem) 
values (4641202 ,98823483 ,9858584 ,'PULSIOX' ,'INT' ,'2020-01-26' ,'18:21:54' ,'EXTERNO' ,88 ,'');	
insert into fcrb.vital_signs (patnr, falnr, idvs, vppid, dttyp, erdat, vptim, typevs, vwert, vbem) 
values (4641202 ,98823483 ,9858664 ,'PULSIOX' ,'INT' ,'2019-07-28' ,'13:59:07' ,'EXTERNO' ,98 ,'');	
insert into fcrb.vital_signs (patnr, falnr, idvs, vppid, dttyp, erdat, vptim, typevs, vwert, vbem) 
values (4641202 ,98823483 ,9858764 ,'PULSIOX' ,'INT' ,'2020-03-28' ,'14:18:46' ,'EXTERNO' ,88 ,'');	
insert into fcrb.vital_signs (patnr, falnr, idvs, vppid, dttyp, erdat, vptim, typevs, vwert, vbem) 
values (4641202 ,98823483 ,9858920 ,'PULSIOX' ,'INT' ,'2019-06-30' ,'12:40:48' ,'EXTERNO' ,91 ,'');	
insert into fcrb.vital_signs (patnr, falnr, idvs, vppid, dttyp, erdat, vptim, typevs, vwert, vbem) 
values (4641202 ,98823483 ,9859001 ,'PULSIOX' ,'INT' ,'2019-05-20' ,'03:18:27' ,'EXTERNO' ,87 ,'');	
insert into fcrb.vital_signs (patnr, falnr, idvs, vppid, dttyp, erdat, vptim, typevs, vwert, vbem) 
values (4641202 ,98823483 ,9859134 ,'PULSIOX' ,'INT' ,'2019-05-02' ,'21:16:08' ,'EXTERNO' ,91 ,'');	
insert into fcrb.vital_signs (patnr, falnr, idvs, vppid, dttyp, erdat, vptim, typevs, vwert, vbem) 
values (4641202 ,98823483 ,9859158 ,'PULSIOX' ,'INT' ,'2019-10-15' ,'09:35:23' ,'EXTERNO' ,98 ,'');	
insert into fcrb.vital_signs (patnr, falnr, idvs, vppid, dttyp, erdat, vptim, typevs, vwert, vbem) 
values (4641202 ,98823483 ,9859251 ,'PULSIOX' ,'INT' ,'2019-09-19' ,'15:03:27' ,'EXTERNO' ,93 ,'');	


insert into fcrb.order_entry (einri, falnr, idodr, patnr, pernr, erdat, orgid) values ('HCPB', 988392719, 95565900, 4641202, 2827346, '1991-09-23', 'H-END');

insert into fcrb.order_entry (einri, falnr, idodr, patnr, pernr, erdat, orgid) values ('HCPB', 98823483, 80923823, 4641202, 8405937, '2019-05-15', 'H-CAR');


insert into fcrb.patient (patnr, gschl, nname, vname, gbdat, gbnam, namzu, glrand, famst, telf1, rvnum, decdat) 
values (4641202, 2, 'Soler', 'Joana', '1935-05-12', 'Rodríguez', 'Sra.', 'ES','CASADO', 9354764369, 84358426112, NULL);


insert into fcrb.patient_address (patnr, pstlz, stras, land, ort, floor, adrnr) values (4641202, 8005, 'Londres 211', 'ES', 'Barcelona', 211, '3º 2º');


insert into fcrb.professional (pernr, erusr, orgid, gbdat, begdt, enddt, erdat, rank) 
values (2827346, 'GRIOS', 'H-END', '1970-09-23', '1996-02-17',NULL, '1996-02-10', 'A8B');

insert into fcrb.professional (pernr, erusr, orgid, gbdat, begdt, enddt, erdat, rank) 
values (8405937, 'CMARQUEZ', 'H-CAR', '1982-02-18', '2002-11-21', NULL, '2002-11-21', 'E99');

insert into fcrb.professional (pernr, erusr, orgid, gbdat, begdt, enddt, erdat, rank) 
values (1239828, 'PCHACON', 'H-MMG', '1991-02-28', '2018-11-21', NULL, '2018-11-21', 'FA3');


insert into fcrb.serums_ids (serums_id, patnr) values (1, 4641202);


insert into fcrb.patient_rules (rule_id, tags, filters) values ('as8sadausd99S', ARRAY['wearable', 'patient_details'], '{}');
insert into fcrb.patient_rules (rule_id, tags, filters) values ('abc', ARRAY['all'], '{}');


insert into fcrb.hospital_tags (tags) values (ARRAY['wearable', 'diagnostic', 'medication', 'patient_details', 'patient_address', 'appointments', 'healthcare_providers', 'treatments', 'personal']);


insert into fcrb.hospital_doctors (id, name, specialism) values (1, 'Mateu Martin Silva', 1);
insert into fcrb.hospital_doctors (id, name, specialism) values (2, 'Lluc Garcia Torres', 1);
insert into fcrb.hospital_doctors (id, name, specialism) values (3, 'Llora Romero Navarro', 1);
insert into fcrb.hospital_doctors (id, name, specialism) values (4, 'Laia Ortega Morales', 1);
insert into fcrb.hospital_doctors (id, name, specialism) values (5, 'Neus Ramos Serrano', 2);
insert into fcrb.hospital_doctors (id, name, specialism) values (6, 'Beatriu Iglesias Delgado', 2);
insert into fcrb.hospital_doctors (id, name, specialism) values (7, 'Carles Sanchez Martinez', 2);
insert into fcrb.hospital_doctors (id, name, specialism) values (8, 'Dolors Sanz Rubio', 3);
insert into fcrb.hospital_doctors (id, name, specialism) values (9, 'Francesc Diaz Ruiz', 3);
insert into fcrb.hospital_doctors (id, name, specialism) values (10, 'Àlex Alonso Romero', 3);



