#!/usr/bin/python

enc = int(input("Enter 1 for encryption, 0 for decryption: "))
msg = input("Enter message to evaluate(without punctuation): ").lower()
key = input("Enter column key: ").upper()

if enc != 0:
    enc = 1

# remove duplicate letters from key
tkey = ""
for c in key:
    if c not in tkey:
        tkey = tkey + c

key = tkey

# remove spaces and punctuation from message
tmsg = ""
for c in msg:
    if c.isalpha():
        tmsg = tmsg + c

msg = tmsg


# Core note: code treats array rows as "columns" in a "columnar" transposition
# keep that in mind or this code could get a little confusing

# create character grid out of plaintext
def enc_columns(text, colKey):
    grid = []
    for c in colKey:
        grid.append([c])
    
    colnum = 0
    for c in text:
        grid[colnum].append(c)
        colnum = (colnum + 1) % len(colKey)
    
    return grid

# TODO create character grid out of ciphertext
def dec_columns(text, colKey):
    grid = []
    for c in colKey:
        grid.append([c])


    
    return grid

# rearrange columns alphabetically
def alphabatize(grid):
    alpha = ""
    tgrid = []

    for c in grid:
        if c[0] > alpha[-1:]:
            alpha = alpha + c[0]
            tgrid.append(c)
        else:
            alpha = c[0] + alpha
            tgrid.insert(0, c)

    return tgrid

# TODO rearrange columns back to message key order
def dealphabatize(grid):
    alpha = ""
    
    
    return tgrid


if enc == 1:
    columns = enc_columns(msg, key)
    alphabatize(columns)
    ciphertext = ""

    for i in range(0, len(msg)):
        col = i % len(columns)
        row = int(i/len(columns))
        ciphertext = columns[col][row]
    
    print(ciphertext)
else:
    print("not yet")

