import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
key = os.urandom(32)
iv = os.urandom(16)
cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
msg = 'a secret message'

def encrypt(msg):
    byte_msg = str.encode(msg)  # encode string to byte
    encryptor = cipher.encryptor()
    return encryptor.update(byte_msg) + encryptor.finalize()

def decrypt(encrypt_msg):
    decryptor = cipher.decryptor()
    decrypt_byte_msg = decryptor.update(encrypt_msg) + decryptor.finalize()
    return decrypt_byte_msg.decode('utf-8')  # decode byte to string

# encrypt
encrypted_msg = encrypt(msg)
print('encrypted_msg=', encrypted_msg, type(encrypted_msg))

# decrypt
decrypted_msg = decrypt(encrypted_msg)
print('decrypted_msg=', decrypted_msg, type(decrypted_msg))

# test
print('success=', msg==decrypted_msg)