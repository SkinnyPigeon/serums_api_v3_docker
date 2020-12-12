from sources.format_mapping.fcrb import *
from sources.format_mapping.ustan import *
from sources.format_mapping.zmc import *
import json

def hospital_picker(hospital_id):
    if hospital_id == 'FCRB':
        return fcrb_personal_info, fcrb_event_boilerplate
    elif hospital_id == 'USTAN':
        return ustan_personal_info, ustan_event_boilerplate
    elif hospital_id == 'ZMC':
        return zmc_personal_info, zmc_event_boilerplate
        
def personal_info_formatter(hospital_id, personal_info, sphr):
    sphr = json.loads(sphr)
    print(sphr)
    print(personal_info)
    for record in sphr:
        try:
            for key, values in record.items():
                for entry, details in personal_info.items():
                    # print(details['location'])
                    if details['location'] == key:
                        personal_info[entry] = record[key]['0'][details['field']]

            if hospital_id == 'ZMC':
                personal_info['weight'] = 75
                personal_info['height'] = 165
        except:
            pass
    
    for key, values in personal_info.items():
        if isinstance(personal_info[key], dict):
            personal_info[key] = "NA" 
    return personal_info


# def format_dates(sphr):
#     for record in sphr:
#         print("DATATYPES: {}".format(record))

#     return sphr

def sphr_formatter(event_boilerplate, sphr, patient_tags):
    sphr = json.loads(sphr)
    # sphr = format_dates(sphr)
    filled_records = []
    output = []

    for record in sphr:
        for key, values in record.items():
            if bool(record[key]):
                filled_records.append(record)

    boilerplate = event_boilerplate.copy()

    avoid_fields = ['what', 'data_vault_table', 'details']
    for record in filled_records:
        for key, values in record.items():
            for entry, details in boilerplate.items():
                if entry not in avoid_fields:
                    try:
                        if details['location'] == key:
                            print(entry)
                            print(record[key]['0'][details['field']])
                            boilerplate[entry] = record[key]['0'][details['field']]
                            avoid_fields.append(entry)
                    except:
                        pass

    for record in filled_records:
        finished_boilerplate = boilerplate.copy()
        for key, values in record.items():
            finished_boilerplate["what"] = patient_tags
            finished_boilerplate["data_vault_table"] = key
            finished_boilerplate["details"] = values
        for key, values in finished_boilerplate.items():
            if key != "details":
                if isinstance(finished_boilerplate[key], dict):
                    finished_boilerplate[key] = "NA" 
        output.append(finished_boilerplate)
    return output


def format_data(hospital_id, sphr, serums_id, patient_tags):
    output = {"serums_id": serums_id}
    personal_info, event_boilerplate = hospital_picker(hospital_id)
    formatted_personal_info = personal_info_formatter(hospital_id, personal_info, sphr)
    formatted_sphr = sphr_formatter(event_boilerplate, sphr, patient_tags)

    output.update({"personalInfo": formatted_personal_info})
    output.update({"events": formatted_sphr})

    return json.dumps(output)

def format_data_decrypted(hospital_id, sphr, serums_id, patient_tags):
    output = {"serums_id": serums_id}
    personal_info, event_boilerplate = hospital_picker(hospital_id)
    formatted_personal_info = personal_info_formatter(hospital_id, personal_info, sphr)
    formatted_sphr = sphr_formatter(event_boilerplate, sphr, patient_tags)

    output.update({"personalInfo": formatted_personal_info})
    output.update({"events": formatted_sphr})

    return output