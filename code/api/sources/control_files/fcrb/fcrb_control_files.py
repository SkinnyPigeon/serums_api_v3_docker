from sources.control_files.fcrb.fcrb_diagnostic_control_file import *
from sources.control_files.fcrb.fcrb_episode_control_file import *
from sources.control_files.fcrb.fcrb_medical_specialty_control_file import *
from sources.control_files.fcrb.fcrb_medication_control_file import *
from sources.control_files.fcrb.fcrb_monitoring_parameters_control_file import *
from sources.control_files.fcrb.fcrb_order_entry_control_file import *
from sources.control_files.fcrb.fcrb_patient_address_control_file import *
from sources.control_files.fcrb.fcrb_patient_control_file import *
from sources.control_files.fcrb.fcrb_professional_control_file import *
from sources.control_files.fcrb.fcrb_vital_signs_control_file import *

fcrb_controls = {
    'fcrb.diagnostic': {
        'hubs': fcrb_diagnostic_hubs,
        'satellites': fcrb_diagnostic_satellites,
        'links': fcrb_diagnostic_links 
    },
    'fcrb.episode': {
        'hubs': fcrb_episode_hubs,
        'satellites': fcrb_episode_satellites,
        'links': fcrb_episode_links 
    },
    'fcrb.medical_specialty': {
        'hubs': fcrb_medical_specialty_hubs,
        'satellites': fcrb_medical_specialty_satellites,
        'links': fcrb_medical_specialty_links 
    },
    'fcrb.medication': {
        'hubs': fcrb_medication_hubs,
        'satellites': fcrb_medication_satellites,
        'links': fcrb_medication_links 
    },
    'fcrb.monitoring_parameters': {
        'hubs': fcrb_monitoring_parameters_hubs,
        'satellites': fcrb_monitoring_parameters_satellites,
        'links': fcrb_monitoring_parameters_links 
    },
    'fcrb.order_entry': {
        'hubs': fcrb_order_entry_hubs,
        'satellites': fcrb_order_entry_satellites,
        'links': fcrb_order_entry_links 
    },
    'fcrb.patient_address': {
        'hubs': fcrb_patient_address_hubs,
        'satellites': fcrb_patient_address_satellites,
        'links': fcrb_patient_address_links 
    },
    'fcrb.patient': {
        'hubs': fcrb_patient_hubs,
        'satellites': fcrb_patient_satellites,
        'links': fcrb_patient_links 
    },
    'fcrb.professional': {
        'hubs': fcrb_professional_hubs,
        'satellites': fcrb_professional_satellites,
        'links': fcrb_professional_links 
    },
    'fcrb.vital_signs': {
        'hubs': fcrb_vital_signs_hubs,
        'satellites': fcrb_vital_signs_satellites,
        'links': fcrb_vital_signs_links 
    }
}