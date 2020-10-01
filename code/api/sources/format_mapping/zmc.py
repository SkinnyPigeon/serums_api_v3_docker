zmc_personal_info = {
    "firstName": {
        "field": "nname",
        "location": "sat_person_patient_details",
        "value": "NA"
    },
    "lastName": {
        "field": "nnams",
        "location": "sat_person_patient_details",
        "value": "NA"
    },
    "dateOfBirth": {
        "field": "gbdat",
        "location": "sat_person_patient_details",
        "value": "NA"
    },
    "gender": {
        "field": "gschl",
        "location": "sat_person_patient_details",
        "value": "NA"
    },
    "nationality": {
        "field": "natio",
        "location": "sat_person_patient_details",
        "value": "NA"
    },
    "weight": {
        "field": "weight",
        "location": "sat_person_patient_measurements",
        "value": "NA"
    },
    "height": {
        "field": "height",
        "location": "sat_person_patient_measurements",
        "value": "NA"
    }
}

zmc_event_boilerplate = {
    "eventId": {
        "field": "NA",
        "location": "NA",
        "value": "NA"
    },
    "associatedId": {
        "field": "patnr",
        "location": "hub_person",
        "value": "NA"
    },
    "when": {
        "field": "NA",
        "location": "NA",
        "value": "NA"
    },
    "where": {
        "field": "NA",
        "location": "NA",
        "value": "Zuyderland Medisch Centrum"
    },
    "who": {
        "field": "NA",
        "location": "NA",
        "value": "NA"
    },
    "what":[
        # Put the patient's query tags in here
    ],
    "data_vault_table": "",
    "details":[
        # This is where the actual results go
    ]
}
