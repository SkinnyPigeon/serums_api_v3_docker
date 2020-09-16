from sources.control_files.ustan.ustan_chemocare_toxicity_control_file import *
from sources.control_files.ustan.ustan_chemocare_treatment_control_file import *
from sources.control_files.ustan.ustan_ndc_charlson_control_file import *
from sources.control_files.ustan.ustan_ndc_smr01_control_file import *
from sources.control_files.ustan.ustan_ndc_smr06_control_file import *

ustan_controls = {
    'ustan.chemocare_toxicity': {
        'hubs': ustan_chemocare_toxicity_hubs,
        'satellites': ustan_chemocare_toxicity_satellites,
        'links': ustan_chemocare_toxicity_links
    },
    'ustan.chemocare_treatment': {
        'hubs': ustan_chemocare_treatment_hubs,
        'satellites': ustan_chemocare_treatment_satellites,
        'links': ustan_chemocare_treatment_links
    },
    'ustan.ndc_charlson': {
        'hubs': ustan_ndc_charlson_hubs,
        'satellites': ustan_ndc_charlson_satellites,
        'links': ustan_ndc_charlson_links
    },
    'ustan.ndc_smr01': {
        'hubs': ustan_ndc_smr01_hubs,
        'satellites': ustan_ndc_smr01_satellites,
        'links': ustan_ndc_smr01_links
    },
    'ustan.ndc_smr06': {
        'hubs': ustan_ndc_smr06_hubs,
        'satellites': ustan_ndc_smr06_satellites,
        'links': ustan_ndc_smr06_links
    }
}