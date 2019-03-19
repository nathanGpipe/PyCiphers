#!/usr/bin/python

enc = int(input("Enter 1 for encryption, 0 for decryption: "))
msg = input("Enter message to evaluate(without punctuation): ").lower()
key = input("Enter column key: ").upper()

def build_columns(text, colKey):
    grid = []
    for c in key:
        grid.append([c])

    
    return grid

def alphabatize(key):
    key = key.upper()
    alpha = ""

    for c in key:
        if c > alpha[-1:]:
            alpha = alpha + c
        else:
            alpha = c + alpha

    return alpha


