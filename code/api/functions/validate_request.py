def validate_sphr_request(request):
    invalid_fields = {}
    check_for_data_types(request, invalid_fields)
    check_for_empty_fields(request, invalid_fields)
    check_for_public_key(request['public_key'], invalid_fields)

    valid = is_valid(invalid_fields)

    return invalid_fields

def is_valid(invalid_fields):
    if len(invalid_fields) > 0:
        return False
    else:
        return True

def check_for_empty_fields(request, invalid_fields):
    for key in request:
        if request[key] == '' or request[key] == None:
            invalid_fields.update({key: 'Cannot be empty'})

def check_for_data_types(request, invalid_fields):
    correct_types = {
        'public_key': str,
        'serums_id': int,
        'rule_id': str,
        'hospital_id': str
    }
    for key in request:
        if not isinstance(request[key], correct_types[key]):
            invalid_fields.update({key: 'Must be of datatype {correct_type}'\
                .format(correct_type=correct_types[key])})
    

def check_for_public_key(public_key, invalid_fields):
    if "-----BEGIN PUBLIC KEY-----" not in public_key \
    or "-----END PUBLIC KEY-----" not in public_key:
        invalid_fields.update({'public_key': 'Public key is not in correct format'})