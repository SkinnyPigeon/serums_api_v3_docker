fcrb_personal_info = {
    "firstName": {
        "field": "vname",
        "location": "sat_person_patient_details",
        "value": "NA"
    },
    "lastName": {
        "field": "gbnam",
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
        "field": "glrand",
        "location": "sat_person_patient_details",
        "value": "NA"
    },
    "weight": {
        "field": "NA",
        "location": "NA",
        "value": "NA"
    },
    "height": {
        "field": "NA",
        "location": "NA",
        "value": "NA"
    }
}

fcrb_event_boilerplate = {
    "eventId": {
        "field": "falnr",
        "location": "hub_time",
        "value": "NA"
    },
    "associatedId": {
        "field": "patnr",
        "location": "hub_person",
        "value": "NA"
    },
    "when": {
        "field": "erdat",
        "location": "sat_time_order_date",
        "value": "NA"
    },
    "where": {
        "field": "einri",
        "location": "hub_location",
        "value": "NA"
    },
    "who": {
        "field": "pernr",
        "location": "hub_person",
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
