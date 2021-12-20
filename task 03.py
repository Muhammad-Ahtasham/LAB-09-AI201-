# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 16:05:55 2021

@author: SELAB
"""

def encrypt(key, message):
    message = message.upper()
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""

    for letter in message:
        if letter in alpha: #if the letter is actually a letter
            #find the corresponding ciphertext letter in the alphabet
            letter_index = (alpha.find(letter) + key) % len(alpha)

            result = result + alpha[letter_index]
        else:
            result = result + letter

    return result

def decrypt(key, message):
    message = message.upper()
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""

    for letter in message:
        if letter in alpha: #if the letter is actually a letter
            #find the corresponding ciphertext letter in the alphabet
            letter_index = (alpha.find(letter) - key) % len(alpha)

            result = result + alpha[letter_index]
        else:
            result = result + letter

    return result

word = "Ahtasham"
#encrypt "BILLY" with a key of 3
encrypted = encrypt(3,word)
print(encrypted) #should print "ELOOB"

#decrypt "ELOOB" with a key of 3
decrypted = decrypt(3,encrypted)
print(decrypted) #should print "BILLY"

