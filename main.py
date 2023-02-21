import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
encoding = 'utf-8'
key = os.urandom(32)
iv = os.urandom(16)
cipher = Cipher(algorithms.AES(key), modes.CBC(iv))


def encrypt(msg):
    byte_msg = str.encode(msg)  # encode string to byte
    encryptor = cipher.encryptor()
    return encryptor.update(byte_msg) + encryptor.finalize()


def decrypt(encrypt_msg):
    decryptor = cipher.decryptor()
    decrypt_byte_msg = decryptor.update(encrypt_msg) + decryptor.finalize()
    return decrypt_byte_msg.decode(encoding)  # decode byte to string


def example():
    msg = 'a secret message'
    # Encrypt & Decrypt
    encrypted_msg = encrypt(msg)            # encrypt
    decrypted_msg = decrypt(encrypted_msg)  # decrypt
    # Results
    print('encrypted_msg=', encrypted_msg, type(encrypted_msg))
    print('decrypted_msg=', decrypted_msg, type(decrypted_msg))
    print('Test=', 'Success' if msg==decrypted_msg else 'Fail')


if __name__ == "__main__":
    example()

