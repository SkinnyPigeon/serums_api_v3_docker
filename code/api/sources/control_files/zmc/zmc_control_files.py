from sources.control_files.zmc.zmc_patient_alcohol_use_control_file import *
from sources.control_files.zmc.zmc_patient_allergies_intolerance_control_file import *
from sources.control_files.zmc.zmc_patient_appointments_control_file import *
from sources.control_files.zmc.zmc_patient_details_control_file import *
from sources.control_files.zmc.zmc_patient_diagnostic_control_file import *
from sources.control_files.zmc.zmc_patient_documents_control_file import *
from sources.control_files.zmc.zmc_patient_drug_use_control_file import *
from sources.control_files.zmc.zmc_patient_functional_state_control_file import *
from sources.control_files.zmc.zmc_patient_living_situation_control_file import *
from sources.control_files.zmc.zmc_patient_measurements_control_file import *
from sources.control_files.zmc.zmc_patient_operations_control_file import *
from sources.control_files.zmc.zmc_patient_tobacco_use_control_file import *
from sources.control_files.zmc.zmc_patient_warnings_control_file import *
from sources.control_files.zmc.zmc_wearable_control_file import *

zmc_controls = {
    'zmc.patient_alcohol_use': {
        'hubs': zmc_patient_alcohol_use_hubs,
        'satellites': zmc_patient_alcohol_use_satellites,
        'links': zmc_patient_alcohol_use_links
    },
    'zmc.patient_allergies_intolerance': {
        'hubs': zmc_patient_allergies_intolerance_hubs,
        'satellites': zmc_patient_allergies_intolerance_satellites,
        'links': zmc_patient_allergies_intolerance_links
    },
    'zmc.patient_appointments': {
        'hubs': zmc_patient_appointments_hubs,
        'satellites': zmc_patient_appointments_satellites,
        'links': zmc_patient_appointments_links
    },
    'zmc.patient_details': {
        'hubs': zmc_patient_details_hubs,
        'satellites': zmc_patient_details_satellites,
        'links': zmc_patient_details_links
    },
    'zmc.patient_diagnostic': {
        'hubs': zmc_patient_diagnostic_hubs,
        'satellites': zmc_patient_diagnostic_satellites,
        'links': zmc_patient_diagnostic_links
    },
    'zmc.patient_documents': {
        'hubs': zmc_patient_documents_hubs,
        'satellites': zmc_patient_documents_satellites,
        'links': zmc_patient_documents_links
    },
    'zmc.patient_drug_use': {
        'hubs': zmc_patient_drug_use_hubs,
        'satellites': zmc_patient_drug_use_satellites,
        'links': zmc_patient_drug_use_links
    },
    'zmc.patient_functional_state': {
        'hubs': zmc_patient_functional_state_hubs,
        'satellites': zmc_patient_functional_state_satellites,
        'links': zmc_patient_functional_state_links
    },
    'zmc.patient_living_situation': {
        'hubs': zmc_patient_living_situation_hubs,
        'satellites': zmc_patient_living_situation_satellites,
        'links': zmc_patient_living_situation_links
    },
    'zmc.patient_measurements': {
        'hubs': zmc_patient_measurements_hubs,
        'satellites': zmc_patient_measurements_satellites,
        'links': zmc_patient_measurements_links
    },
    'zmc.patient_operations': {
        'hubs': zmc_patient_operations_hubs,
        'satellites': zmc_patient_operations_satellites,
        'links': zmc_patient_operations_links
    },
    'zmc.patient_tobacco_use': {
        'hubs': zmc_patient_tobacco_use_hubs,
        'satellites': zmc_patient_tobacco_use_satellites,
        'links': zmc_patient_tobacco_use_links
    },
    'zmc.patient_warnings': {
        'hubs': zmc_patient_warnings_hubs,
        'satellites': zmc_patient_warnings_satellites,
        'links': zmc_patient_warnings_links
    },
    'zmc.wearable': {
        'hubs': zmc_wearable_hubs,
        'satellites': zmc_wearable_satellites,
        'links': zmc_wearable_links
    }
}