# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from cryptography.fernet import Fernet

key = Fernet.generate_key()

f = Fernet(key)

token = f.encrypt(b"A really secret message. Not for prying eyes.")

print("encrpyted data is ", token)
print("decrypted data i s ", f.decrypt(token))