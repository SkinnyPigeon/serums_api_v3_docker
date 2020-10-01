from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.serialization import load_pem_public_key

from cryptography.fernet import Fernet

import base64
import binascii

def encrypt_patient_record(sphr, public_key):
    public_key = public_key.encode()
    public_key = load_pem_public_key(public_key, backend=default_backend())
    sphr = sphr.encode()
    key_to_encrypt = Fernet.generate_key()
    print(key_to_encrypt)
    fernet_encryption = Fernet(key_to_encrypt)
    encrypted_data = fernet_encryption.encrypt(sphr)
    print(encrypted_data)
    return encrypt_and_encode_key_and_data(key_to_encrypt, public_key, encrypted_data)
    
    
def encrypt_and_encode_key_and_data(key_to_encrypt, public_key, encrypted_data):
    encrypted_key = public_key.encrypt(
        key_to_encrypt,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    decoded_data = encrypted_data.decode()
    encoded_key = binascii.b2a_base64(encrypted_key, newline=False)
    decoded_key = encoded_key.decode()
    packet_to_send = {'key': decoded_key, 'data': decoded_data}

    return packet_to_send