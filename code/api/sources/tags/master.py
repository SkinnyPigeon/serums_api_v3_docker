tags = {
    'wearable': {
        'fcrb': [
            {
                'table': 'vital_signs',
                'fields': ['all']
            },
            {
                'table': 'monitoring_parameters',
                'fields': ['all']
            }
        ],
        
        'ustan': [],
        'zmc': [
            {
                'table': 'wearable',
                'fields': ['all']
            }
        ]
    },
    'diagnostic': {
        'fcrb': [
            {
                'table': 'diagnostic',
                'fields': ['all']
            },
            {
                'table': 'episode',
                'fields': ['all']
            }
        ],
        'ustan': [
            {
                'table': 'chemocare_toxicity',
                'fields': ['all']
            },
            {
                'table': 'ndc_charlson',
                'fields': ['incidence_year', 'simd1', 'simd', 'conf_heart_fail_flag', 'dementia_flag', 'pulmonary_flag', 'con_tiss_disease_flag', 'diabetes_flag', 'para_hemiplegia_flag', 'renal_flag', 'liver_flag', 'aids_hiv_flag', 'charlson_quan_score']
            },
            {
                'table': 'ndc_smr06',
                'fields': ['all']
            },
            {
                'table': 'ndc_smr01',
                'fields': ['main_condition', 'other_condition_1', 'other_condition_2', 'other_condition_3', 'other_condition_4', 'age_at_diagnosis']
            }
        ],
        'zmc': [
            {
                'table': 'patient_diagnostic',
                'fields': ['all']
            },
            {
                'table': 'patient_documents',
                'fields': ['all']
            }
        ]
    },
    'medication': {
        'fcrb': [
            {
                'table': 'medication',
                'fields': ['all']
            }
        ],
        'ustan': [
            {
                'table': 'chemocare_treatment',
                'fields': ['intention', 'regime_code', 'cycle', 'cycle_id', 'drug_type', 'drug_name', 'drug_dose', 'required_dose', 'drug_status']
            }
        ],
        'zmc': [
            {
                'table': 'patient_medication',
                'fields': ['all']
            }
        ]
    },
    'patient_details': {
        'fcrb': [
            {
                'table': 'patient',
                'fields': ['all']
            },
            {
                'table': 'patient_address',
                'fields': ['all']
            }
        ],
        'ustan': [
            {
                'table': 'ndc_smr01', 
                'fields': ['sex', 'age_in_years', 'ethnic_group', 'marital_status', 'postcode', 'height', 'weight']
            },
            {
                'table': 'ndc_charlson', 
                'fields': ['postcode']
            }
        ],
        'zmc': [
            {
                'table': 'patient_details',
                'fields': ['all']
            },
            {
                'table': 'patient_measurements',
                'fields': ['all']
            }
        ]
    },
    'patient_address': {
        'fcrb': [
            {
                'table': 'patient_address',
                'fields': ['all']
            }
        ],
        'ustan': [
            {
                'table': 'ndc_charlson', 
                'fields': ['postcode']
            }
        ],
        'zmc': [
            {
                'table': 'patient_details',
                'fields': ['land', 'pstlz', 'ort', 'stras', 'telf1']
            }
        ]
    },
    'appointments': {
        'fcrb': [
            {
                'table': 'episode',
                'fields': ['all']
            },
            {
                'table': 'order_entry',
                'fields': ['all']
            }
        ],
        'ustan': [
            {
                'table': 'chemocare_treatment',
                'fields': ['all']
            },
            {
                'table': 'ndc_smr01',
                'fields': ['all']
            }
        ],
        'zmc': [
            {
                'table': 'patient_appointments',
                'fields': ['all']
            }
        ]
    },
    'operations': {
        'fcrb': [],
        'ustan': [
            {
                'table': 'ndc_smr01',
                'fields': ['admission_date', 'discharge_date', 'length_of_stay', 'main_condition', 'other_condition_1', 'other_condition_2', 'other_condition_3', 'other_condition_4', 'main_operation_a', 'main_operation_b', 'age_at_diagnosis']
            }
        ],
        'zmc': [
            {
                'table': 'patient_operations',
                'fields': ['all']
            }
        ]
    },
    'documents': {
        'fcrb': [],
        'ustan': [],
        'zmc': [
            {
                'table': 'patient_documents',
                'fields': ['all']
            }
        ]
    },
    'healthcare_providers': {
        'fcrb': [
            {
                'table': 'professional',
                'fields': ['all']
            },
            {
                'table': 'medical_specialty',
                'fields': ['all']
            }
        ],
        'ustan': [
            {
                'table': 'chemocare_treatment',
                'fields': ['consultant_code']
            }
        ],
        'zmc': []
    },
    'drugs_and_alcohol': {
        'fcrb': [],
        'ustan': [],
        'zmc': [
            {
                'table': 'patient_drug_use',
                'fields': ['all']
            },
            {
                'table': 'patient_alcohol_use',
                'fields': ['all']
            },
            {
                'table': 'patient_tobacco_use',
                'fields': ['all']
            }
        ]
    },
    'allergies': {
        'fcrb': [],
        'ustan': [],
        'zmc': [
            {
                'table': 'patient_allergies_intolerance',
                'fields': ['all']
            }
        ]
    },
    'additional_information': {
        'fcrb': [],
        'ustan': [],
        'zmc': [
            {
                'table': 'patient_warnings',
                'fields': ['all']
            },
            {
                'table': 'patient_functional_state',
                'fields': ['all']
            },
            {
                'table': 'patient_living_situation',
                'fields': ['all']
            }
        ]
    },
    'treatments': {
        'fcrb': [
            {
                'table': 'medication',
                'fields': ['all']
            },
            {
                'table': 'medical_specialty',
                'fields': ['all']
            }
        ],
        'ustan': [
            {
                'table': 'chemocare_treatment',
                'fields': ['all']
            }
        ],
        'zmc': [
            {
                'table': 'patient_operations',
                'fields': ['all']
            },
            {
                'table': 'patient_documents',
                'fields': ['all']
            }
        ]
    },
    'personal': {
        'fcrb': [
            {
                'table': 'patient',
                'fields': ['patnr', 'gschl', 'vname', 'gbdat', 'gbnam', 'glrand']
            }
        ],
        'ustan': [
            {
                'table': 'ndc_smr01',
                'fields': ['sex', 'height', 'weight']
            }
        ],
        'zmc': [
            {
                'table': 'patient_details',
                'fields': ['patnr','gschl','nname','nnams','gbdat','natio']
            }
        ]
    },
    'all': {
        'fcrb': [
            {
                'table': 'diagnostic',
                'fields': ['einri', 'patnr', 'falnr', 'pernr', 'lfdnr', 'dkey1']
            },
            {
                'table': 'episode',
                'fields': ['einri', 'falnr', 'patnr', 'pernr', 'bekat', 'falar', 'statu', 'krzan', 'storn', 'casetx', 'enddtx', 'einzg', 'fatnx']
            },
            {
                'table': 'medical_specialty',
                'fields': ['orgid', 'orgna']
            },
            {
                'table': 'medication',
                'fields': ['einri', 'patnr', 'falnr', 'pernr', 'motx', 'mostx', 'motypid', 'mpresnr', 'storn', 'stusr', 'stoid', 'erdat', 'stdat']
            },
            {
                'table': 'monitoring_parameters',
                'fields': ['patnr', 'falnr', 'vppid', 'pernr', 'vbem', 'datyp', 'wertogr', 'wertugr', 'wertmax', 'wertmin']
            },
            {
                'table': 'order_entry',
                'fields': ['einri', 'falnr', 'patnr', 'orgid', 'pernr', 'idodr', 'erdat']
            },
            {
                'table': 'patient',
                'fields': ['patnr', 'gschl', 'nname', 'vname', 'gbdat', 'gbnam', 'namzu', 'glrand', 'famst', 'telf1', 'rvnum', 'decdat']
            },
            {
                'table': 'patient_address',
                'fields': ['patnr', 'pstlz', 'stras', 'land', 'ort', 'floor', 'adrnr']
            },
            {
                'table': 'professional',
                'fields': ['pernr', 'orgid', 'erusr', 'gbdat', 'rank', 'begdt', 'enddt', 'erdat']
            },
            {
                'table': 'vital_signs',
                'fields': ['patnr', 'falnr', 'vppid', 'idvs', 'dttyp', 'typevs', 'vwert', 'vbem', 'erdat', 'vptim']
            }
        ],
        'ustan': [
            {
                'table': 'chemocare_toxicity',
                'fields': ['chi', 'date1', 'nausea', 'vomiting', 'diarrhoea', 'constipation', 'oral_mucostis', 'oesophasitis', 'neurotoxicity', 'hand_foot', 'skin', 'hypersensitivity', 'fatigue', 'performance_status', 'issues_since_last_visit', 'last_visit_issue_description']
            },
            {
                'table': 'chemocare_treatment',
                'fields': ['chi', 'appointment_date', 'last_toxicity_date', 'tumour_group', 'age_at_diagnosis', 'height', 'weight', 'surface_area', 'patient_type', 'consultant_code', 'intention', 'regime_code', 'cycle', 'cycle_id', 'drug_type', 'drug_name', 'required_dose', 'drug_status']
            },
            {
                'table': 'ndc_charlson',
                'fields': ['chi', 'postcode', 'simd', 'simd1', 'incidence_year', 'conf_heart_fail_flag', 'dementia_flag', 'pulmonary_flag', 'con_tiss_disease_flag', 'diabetes_flag', 'para_hemiplegia_flag', 'renal_flag', 'liver_flag', 'aids_hiv_flag', 'charlson_quan_score']
            },
            {
                'table': 'ndc_smr01',
                'fields': ['chi','admission_date', 'discharge_date', 'length_of_stay', 'sex', 'age_in_years', 'ethnic_group', 'marital_status', 'postcode', 'age_at_diagnosis', 'height', 'weight', 'main_condition', 'other_condition_1', 'other_condition_2', 'other_condition_3', 'other_condition_4', 'main_operation_a', 'main_operation_b']
            },
            {
                'table': 'ndc_smr06',
                'fields': ['chi', 'incidence_date', 'tumour_site_icd10', 'oestrogen_receptor_er_status', 'her2_status_code', 'stage_clinical_t_code', 'stage_clinical_n_code', 'stage_clinical_m_code', 'pathological_tumour_size']
            }
        ],
        'zmc': [
            {
                'table': 'patient_alcohol_use',
                'fields': ['patnr', 'usage_status', 'quantity', 'description']
            },
            {
                'table': 'patient_allergies_intolerance',
                'fields': ['patnr', 'caustic_substance', 'critical', 'description']
            },
            {
                'table': 'patient_appointments',
                'fields': ['patnr', 'type', 'date', 'notes']
            },
            {
                'table': 'patient_details',
                'fields': ['patnr', 'gschl', 'nname', 'nnams', 'vname', 'titel', 'namzu', 'gbdat', 'gbnam', 'gbnas', 'gland', 'natio', 'land', 'telf1', 'pstlz', 'ort', 'stras']
            },
            {
                'table': 'patient_diagnostic',
                'fields': ['patnr', 'type', 'name', 'anatomical_location', 'laterality', 'begin_date', 'end_date']
            },
            {
                'table': 'patient_documents',
                'fields': ['patnr', 'report_title', 'department', 'date', 'content']
            },
            {
                'table': 'patient_drug_use',
                'fields': ['patnr', 'substance', 'quantity', 'description']
            },
            {
                'table': 'patient_functional_state',
                'fields': ['patnr', 'name', 'value', 'date']
            },
            {
                'table': 'patient_living_situation',
                'fields': ['patnr', 'house_type', 'description']
            },
            {
                'table': 'patient_measurements',
                'fields': ['patnr', 'height', 'weight', 'date']
            },
            {
                'table': 'patient_operations',
                'fields': ['patnr', 'anatomical_location', 'date', 'notes']
            },
            {
                'table': 'patient_tobacco_use',
                'fields': ['patnr', 'substance', 'description']
            },
            {
                'table': 'patient_warnings',
                'fields': ['patnr', 'alerts', 'type', 'begin_date']
            },
            {
                'table': 'wearable',
                'fields': ['patnr', 'nr_sst', 'steps_total', 'cadence', 'cyc_rot', 'cyc_rpm', 'day_nr', 'time_total', 'time_passive', 'time_active', 'time_sit', 'time_stand', 'time_walk', 'time_cycle', 'time_hi']
            }
        ]
    }
}