alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

key = 4

def encrypt(text,key):
    encryptedT = ""
    for i in range(len(text)):
        if text[i] == ' ':
            encryptedT += ' '
        elif (alphabet.index(text[i])+key) < (len(alphabet)):
            encryptedT += alphabet[alphabet.index(text[i])+key]
        else:
           encryptedT += alphabet[alphabet.index(text[i])+key-26]
    return encryptedT

def decrypt(encryptedT, key):
    text = ""
    for i in range(len(encryptedT)):
        if encryptedT[i] == ' ':
            text += ' '
        elif (alphabet.index(encryptedT[i])-key) < (len(alphabet)):
            text += alphabet[alphabet.index(encryptedT[i])-key]
        else:
            text += alphabet[alphabet.index(encryptedT[i])-key-26]
    return text