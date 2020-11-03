from sources.control_files.ustan.ustan_chemocare_control_file import *
from sources.control_files.ustan.ustan_demographics_control_file import *
from sources.control_files.ustan.ustan_diagnosis_control_file import *
from sources.control_files.ustan.ustan_smr01_control_file import *

ustan_controls = {
    'ustan.chemocare': {
        'hubs': ustan_chemocare_hubs,
        'satellites': ustan_chemocare_satellites,
        'links': ustan_chemocare_links
    },
    'ustan.demographics': {
        'hubs': ustan_demographics_hubs,
        'satellites': ustan_demographics_satellites,
        'links': ustan_demographics_links
    },
    'ustan.diagnosis': {
        'hubs': ustan_diagnosis_hubs,
        'satellites': ustan_diagnosis_satellites,
        'links': ustan_diagnosis_links
    },
    'ustan.smr01': {
        'hubs': ustan_smr01_hubs,
        'satellites': ustan_smr01_satellites,
        'links': ustan_smr01_links
    }
}