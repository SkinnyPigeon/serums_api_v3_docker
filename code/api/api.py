from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_restplus import Api, Resource, fields
from dotenv import load_dotenv
from pathlib import Path

import os
import json
from functions.validate_request import *
from functions.setup_sources import *
from functions.data_vault import create_data_vault, copy_to_dv
from functions.apply_rules_to_data_vault import *
from functions.encryption import encrypt_patient_record
from functions.formatter import format_data
from functions.handle_users import add_user_to_serums, remove_user_from_serums
from functions.handle_rules import add_rule_to_hospital_db

# Setting up environment

FLASK_DEBUG=1

project_folder = os.path.expanduser('~/code/api/')
load_dotenv(os.path.join(project_folder, '.env'))
PASSWORD = os.getenv('PASSWORD')

app = Flask(__name__)
app.config['ERROR_404_HELP'] = False
CORS(app)
api = Api(
    app, 
    version='1.0', 
    title='Smart Patient Health Record API',
    description='Return the encrypted Smart Patient Health Record from the Serums data lake',
)

# Models

hello = api.model('Server Check', {
    'hello': fields.String(required=True, description='Quick check that the server is on', example='Welcome to the SPHR API. The server is on')
})

request_fields = api.model('Request', {
    'serums_id': fields.Integer(required=True, description='The Serums ID for the patient', example=123),
    'rule_id': fields.Integer(required=True, description='Rule to be executed', example=456),
    'hospital_id': fields.Integer(required=True, description='The id of the hospital for the source data', example=789)
})

reply_fields = api.model('Successful Response', {
    'key': fields.String(required=True, description='The encrypted Fernet key', example="BqKQKHWaCMOozw8U77Cvh0Mj8S+HnvkjuOYzZKrF9L4unP+S9xosAiBF0lJ1hOgZ5mfo0EfyxFdyuBh0ywNBNSUxJdCdnQ+ocwkd14IjsE54VmwTXdTFVcdepR1tjudcIyvVCy+Mxymt4vPh1P7pYTl92wYkEovEpHrs28l++EsaPOgZUiAD7LD5lZ0jZCW5fyFtyBwm8n+aAhNlb0YKnoYKDb88bg9DFyQxazX8SVBBwfmJEklSunVe5s9FULm50BeY1eDS87noQ4nM+so1EPsN5GuBM41KmeySwZZCVYiLh5NfwY+f5efMPbtV683pCL3YoJ89ojYeTlMLJEug=="),
    'data': fields.String(required=True, description='The encrypted patient record', example="gAAAAABeneOIy6q3QxfwmHTjxMjZdP5rxKaQFDbYT-KtJOzgsqZYdnct3qsRcNcAzIrmcnDluR-Q6RLLi8CUthGsa_-7b-VCZrkRO3cLcGKLNuPi2v109dSzXeQ27EazKf49oss4IE11khs6tLZt-yqYCZTz_R84gK6X0BMc0pzoYP-3Qr_h1rV_I6DD3oWHpnbRE4vn86HSR77YajYsi3BGbqPfh-_FJYlgaPWG5USiIXoQYTvJCtHj8kcM9jdhkNICGdlnLkuSZ2A60zx8XpcHImQYd5YzbxENMvWl0Q6SamziiZ5Kl5UXzlyY3IHGpTM-K9T-ycmZj6dkr0hzzqr8lAiWNSinZR2YZDM-diGM7tr8b10hGLF2D1_7-ArvuP12f_aznLgonn4kZtDpro2ImGmzsg-oz01B0pZjNkTvkmOaz32e1ntmvWHBD16yLLHPFdQDw--z0R4i7n_WNJB0Jn3M0sgyHsIkBIB53Pg8ZFKoAxnfACiKIaPJ26JtrVEQ9es6VupfDCT4nUM2WPIiegZ5LmQDXuGBwvw9NrfEW4pC5Sg7CoRv6RvTuT_ywSrhCnd2jePxpdIk0FqTdUsAqancd09IWEnFWQpLxTr348Qq3Dplk5L_dws2H2y8e--AAkBoy08Q-OpT5o8DFS1i9nO84r0KXgWIo4APcmH0UOL53INsgULZDSohzcT675zV8wWxfaja_b3CIVsj54iKs--XgdoSQHijhgasW1UqYgSRqGjW18BTPHUfA1uJ4397U3ZBjZTKCwzgzhr4YBVSBhxMGqEWw8sJCLBXLGxr0MUl1kDRmSptBsc2k7EerGm8JlKI4Xu6XbmXJy3Mjq4aa7Q0elayCnr5izbh9-VJoOEnXMkNgS4PcsEPm3yQdlyk1AlkXK71S4gfUW0DVzfh3NJxWS-xnHPGafu0WnvDdl42wUl-prt6A8AAHWQOQZW1hrGi3gxwCJqQ5vOcqmxXuMdGdCd7xEdBaeuzOFBZSLW5AF1i_0gvmMQAr7YYsV33ZKfX59UHuQG7-Ia9WNRhCRvm2N35jZBQz-F2uenNHd5RFB4h28OvJ5yIVKHVmDAVxrAfq2tf6liqdhECPwqV1BUf13TfF-LDwm93zp4Sp4Enbjur4egN1Pyl2lkGQNQKSWHgAgzq60uNPuzeS-DUm0OvnxmDGaJ-S966lBl7FmPOnoZCJZTk3uXB96m3N4qJ6dZddgqKQDfhBG_Zd87wVQbLjR4bYdBqcH3NY51s1mqjurRzy5RCEqsZCZQL7xCRh5uwyjWZC-oqIp9XBTyqvu7E_j6kWIGX4P0FispRPOxc-LJLoau6Fu1Fp1ZcxBLYBJyRfBAnwIaoRHpoM_zlWUVzkEx_ChUYFkxjCBEJMqf027087_aTB5rdFNxm7etW5RQBPcWwc5KtxTcWo9ae5XfE1aJmRVX17P2rlkXmYD9oiZdOxt21hUktNKM1Y3ZXmbfKLsgteFHv1G8KTN52xPz4y0AYmORD2U1jFn_e0DeQulYQrdgcTys9WLmteZZe1CE7VgBmj-Pd_U9zDMJ8OI8jj3Y7enuWa1TiIyCuHzwnNcT7wDnlcbrpxQfz3zztsdAw6qO1HfJm4VgA0K1UeCQzggySjMUaYMQa20euqLIko-TmdoWPjgIPG0BcVKXbbwyeW178M8ZOMZ32Y-zoZoWs26GwzrKZFolX4EHiNvZlKBa5FJmi4l6aGjT5r4Ipe68EYwsojCCNdtTVO4Ds1tfeNqDT3FmuBktg3aLAwQggQj_Jinjc9hLglTqfKm5TSUEl1iIvt3t9jxv5UKJ06LgXru2YZxX6f255wPmtHVxqqBggVLmhpRKTV2ifq6bQ0AWSexN3PKQ6XXIpsF2UWmtUJABiJmRuy4UOg85uZC4V56JjJFEwiAjw9VBYf5I0nbSOaBEQkSx7-qSF2fXOkYKw7fl09ur9Q40ZkvVDcCtJRemPMpult7sVB_lg3eINTwSq8tqN6AOrsBQpk4UjidQlXatgXKtXWahkINCruy_PHlQQSYCLL9UxUMhA9Xw1WDircweDeS_4IwoSWqrApu1FBRYQemHvGpWO1kGrdhJCph9V548iRIJd5-6q5lWDZiGGWVs5_drjS6LlBgWNOrkxV80Hv1EI0eKm_G9N08HvpEHhcOu1tpRZhLFzPP5PvWlEecXUTbrxJ6RJEJVBRxTDnzW2ngSoHSC10rZdAwcTV6nkeGYcUv_TH-TJxsBe6-3p8kMpJaGaGIJ83e9av0Uegonl0KGbv0XGcmI2MR2rAvgyPN4oSDtsCqu2pYVeIjF8JJq-WmJfKpP8TwiFGQgXRJSyAkOSDfQF3K4f3ucjW-Vca5YMX7q7b3jtV_YyVZDB-pUve6qaRFcgKw7ZDoQAVMY04yNMG61YWpjetPHl4sf3j39_CMinVq5UGHZgvlTErEqBIVaFksee5QDL5M552-ksp9XHuxOewK-QzpKqK7WalNnwI9YxlRJEu1utoOrp3y5ZO-HtLLTGjunL9bwSaFQ_M1MqqNqDHMOUEwuZuiF0zLq61UDT5Z00JXsYbMBRHFqYam6KkTrEub6Dx9pljsQW-J-S0LAJWO5pnsRSCQuoHu6tx3cTnPeCJQMMA1ThqFcrELxmM3EYv4pUZ6AiugwaTmq2Ym4f_UF9hgIr74O8M2xgTUOc2eoLaMuPInf55EzzKtWNuDrGvKsEJAgKzCDn7w==")
})

add_user_fields = api.model('Add User', {
    'serums_id': fields.Integer(required=True, description='The Serums ID for the patient', example=123),
    'hospitals': fields.List(fields.Integer(required=True, description='The id of the hospital for the source data', example=789))
})

remove_user_fields = api.model('Remove User', {
    'serums_id': fields.Integer(required=True, description='The Serums ID for the patient', example=123),
    'patient_id': fields.Integer(required=True, description="The Patient's ID in the host hospital to be linked to the Serums ID", example=456),
    'hospital_id': fields.Integer(required=True, description='The id of the hospital for the source data', example=789)
})

add_rules_fields = api.model('Add Rule', {
    'rule_id': fields.Integer(required=True, description='Rule to be executed', example=456),
    'hospital_id': fields.Integer(required=True, description='The id of the hospital for the source data', example=789),
    'tags': fields.List(fields.String(required=True, description='The tags that the patient has selected to control their data', example='[wearable, patient_details]')),
    'filters': fields.String(required=False, description='The filters to apply to any requested data', example="einri=101")
})

parser = api.parser()
parser.add_argument('Serums ID', type=list, required=True, help='The Serums ID', location='json')
parser.add_argument('Rule ID', type=list, required=True, help='The Rule to execute', location='json')
parser.add_argument('Hospital ID', type=list, required=True, help='The Hospital where the data is located', location='json')
parser.add_argument('Public Key', type=list, required=True, help='The Public Key', location='json')
parser.add_argument('Hospitals', type=list, required=True, help="The list of hospitals to remove the patient's connection to", location='json')
parser.add_argument('Tags', type=list, required=True, help="The tags which the patient has selected to select subsets of their data", location='json')
parser.add_argument('filters', type=list, required=False, help="Any filters that the patient wants to apply to their data, such as episode number", location='json')



# Routes
ns = api.namespace('api', description='Return the Smart Patient Health Record')

@ns.route('/hello')
class ServerCheck(Resource):
    @api.marshal_with(hello)
    def get(self):
        return {"hello": "Welcome to the SPHR API. The server is on"}

@ns.route("/get_sphr", methods=['post'])
class GetSphr(Resource):
    '''Return the Smart Patient Health Record from the Serums data lake'''
    @api.doc(body=request_fields)
    @api.marshal_with(reply_fields, code=200)

    def post(self):
        req_data = request.get_json()
        invalid_fields = validate_sphr_request(req_data)
        valid = is_valid(invalid_fields)

        if not valid:
            return invalid_fields

        source_data, patient_tags = get_source_data(req_data)  
        control_files = apply_tags(patient_tags, req_data['hospital_id'])
        connection = create_data_vault(req_data['hospital_id'])
        sphr = copy_to_dv(source_data, control_files, connection)
        sphr = format_data(req_data['hospital_id'], sphr, req_data['serums_id'], patient_tags)
        encrypted_record = encrypt_patient_record(sphr, req_data['public_key'])

        connection['engine'].dispose()

        return sphr

@ns.route("/add_user", methods=['post'])
class AddUser(Resource):
    '''Link a patient's hospital ID to their Serums ID'''
    @api.doc(body=add_user_fields)
    # @api.marshal_with(code=200)
    def post(self):
        req_data = request.get_json()
        return add_user_to_serums(req_data)
    
@ns.route("/remove_user", methods=['post'])
class RemoveUser(Resource):
    '''Remove link(s) between a patient's hospital ID(s) and their Serums ID'''
    @api.doc(body=remove_user_fields)
    # @api.marshal_with(code=200)
    def post(self):
        req_data = request.get_json()
        remove_user_from_serums(req_data)
        return json.dumps({"Result": "Success"})

@ns.route("/add_rule", methods=['post'])
class AddRule(Resource):
    '''Add a new rule based on selected tags and filters'''
    @api.doc(body=add_rules_fields)
    # @api.marshal_with(code=200)
    def post(self):
        req_data = request.get_json()
        return add_rule_to_hospital_db(req_data)

# Testing Routes

@ns.route("/get_encrypted", methods=['post'])
class GetEncrypted(Resource):
    '''Return the Smart Patient Health Record from the Serums data lake'''
    @api.doc(body=request_fields)
    @api.marshal_with(reply_fields, code=200)
    def post(self):
        req_data = request.get_json()
        invalid_fields = validate_sphr_request(req_data)
        valid = is_valid(invalid_fields)

        if not valid:
            return invalid_fields

        source_data, patient_tags = get_source_data(req_data)  
        control_files = apply_tags(patient_tags, req_data['hospital_id'])
        connection = create_data_vault(req_data['hospital_id'])
        sphr = copy_to_dv(source_data, control_files, connection)
        sphr = format_data(req_data['hospital_id'], sphr, req_data['serums_id'], patient_tags)
        encrypted_record = encrypt_patient_record(sphr, req_data['public_key'])

        connection['engine'].dispose()
        return encrypted_record


@ns.route("/get_decrypted", methods=['post'])
class GetDecrypted(Resource):
    '''Return the Smart Patient Health Record from the Serums data lake'''
    @api.doc(body=request_fields)
    @api.marshal_with(reply_fields, code=200)
    def post(self):
        req_data = request.get_json()
        invalid_fields = validate_sphr_request(req_data)
        valid = is_valid(invalid_fields)

        if not valid:
            return invalid_fields

        source_data, patient_tags = get_source_data(req_data)  
        control_files = apply_tags(patient_tags, req_data['hospital_id'])
        connection = create_data_vault(req_data['hospital_id'])
        sphr = copy_to_dv(source_data, control_files, connection)
        sphr = format_data(req_data['hospital_id'], sphr, req_data['serums_id'], patient_tags)
        encrypted_record = encrypt_patient_record(sphr, req_data['public_key'])

        connection['engine'].dispose()

        return sphr

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='8080')