#!/usr/bin/python

shiftamt = 0
enc = int(input("Enter 1 for encryption, 0 for decryption: "))
msg = input("Enter message to evaluate(without punctuation): ").lower()

def shift(char, amt):
    x = ord(char)
    if(char.islower()):
        x = x-97
        char = chr(97+(x+amt)%26)
    else:
        x = x-65
        char = chr(65+(x+amt)%26)
    
    return char


if(enc):
    shiftamt = int(input("Shift amount: "))
    msg = msg.upper()
    ciphertext = ""
    for c in msg:
        ciphertext = ciphertext + shift(c, shiftamt)
    print(ciphertext)
else:
    shiftamt = int(input("Shifted amount: "))
    key = 26-shiftamt
    msg = msg.lower()
    plaintext = ""
    for c in msg:
        plaintext = plaintext + shift(c, key)
    print(plaintext)

