zmc_personal = {'tag': 'personal', 'table': 'zmc.patient_details', 'fields': ['patnr','gschl','nname','nnams','gbdat','natio']}
zmc_patient_details = {'tag': 'patient_details', 'table': 'zmc.patient_details', 'fields': ['patnr','gschl','nnams','nname','vname','titel','namzu','gbdat','gbnam','gbnas','gland','natio','land','pstlz','ort','stras','telf1']}
zmc_wearable = {'tag': 'wearable', 'table': 'zmc.wearable','fields': ['patnr','day_nr','time_total','time_passive','time_active','time_sit','time_stand','time_walk','time_cycle','time_hi','nr_sst','steps_total','cadence','cyc_rot','cyc_rpm']}

zmc_tags = [zmc_personal, zmc_patient_details, zmc_wearable]