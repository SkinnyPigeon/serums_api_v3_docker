from sources.control_files.fcrb.fcrb_control_files import fcrb_controls
from sources.control_files.ustan.ustan_control_files import ustan_controls
from sources.control_files.zmc.zmc_control_files import zmc_controls

from sources.tags.fcrb import fcrb_tags
from sources.tags.ustan import ustan_tags
from sources.tags.zmc import zmc_tags


def find_commonality(list1, list2):
    return list(set(list1).intersection(list2))

def print_source_data(source_data):
    print(source_data)

def hospital_tags_and_controls_picker(hospital_id):
    if hospital_id == 1:
        return fcrb_tags, fcrb_controls
    elif hospital_id == 2:
        return ustan_tags, ustan_controls
    elif hospital_id == 3:
        return zmc_tags, zmc_controls

def apply_tags(patient_tags, hospital_id):
    hospital_tags, controls = hospital_tags_and_controls_picker(hospital_id)
    altered_controls = []
    for tag in hospital_tags:
        try:
            if tag['tag'] in patient_tags:
                for satellite in controls[tag['table']]['satellites']['satellites']:
                    satellite['columns'] = find_commonality(satellite['columns'], tag['fields'])
                altered_controls.append(controls[tag['table']])
        except:
            pass
    return altered_controls