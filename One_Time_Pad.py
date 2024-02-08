#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Import statements
import os
import sys
import string
from codecs import encode

# Global variables
letters = string.ascii_letters + " "

def main(args):
    print(f"This script encrypts your plaintext using a One-Time Pad and also decrypts it for you as well. The supported characters are: {letters}.")
    
    cleartext = input("\nEnter your cleartext here: ")
    if all(char in letters for char in cleartext):
        print(f"Confirming input: {cleartext}")
    else:
        print("Invalid input. Ending.")
        sys.exit()
    
    print(f"\nRunning encryption scheme based on this text '{cleartext}'. Please wait...")

    cleartext_data = cleartext.encode('utf-8')
    OTP_key = OTP_Gen(len(cleartext_data))

    ciphertext = encrypt(OTP_key, cleartext_data)
    print(f"\nRaw ciphertext encrypted data: {ciphertext}")
    print(f"Formatted ciphertext encrypted data: " + str(encode(ciphertext, 'hex'), 'utf-8'))

    d_message = decrypt(ciphertext, OTP_key).decode('utf-8')
    print(f"\nYour decrypted data: {d_message}\n")

    del OTP_key, cleartext_data, ciphertext, d_message
    print("Data has been secured. All keys have been deleted.\n")

def OTP_Gen(length):
    return os.urandom(length)

def encrypt(OTP_key, cleartext_data):
    return bytes([k ^ m for k, m in zip(OTP_key, cleartext_data)])

def decrypt(ciphertext, OTP_key):
    return bytes([c ^ k for c, k in zip(ciphertext, OTP_key)])

if __name__ == '__main__':
    main(sys.argv[1:])