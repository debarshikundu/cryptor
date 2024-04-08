def generate_vigenere_table():
    # Generating the Vigenère table
    table = [[0] * 26 for _ in range(26)]
    for i in range(26):
        for j in range(26):
            table[i][j] = chr(((i + j) % 26) + ord('A'))
    return table

def vigenere_encrypt(plaintext, keyword):
    table = generate_vigenere_table()
    plaintext = plaintext.upper()
    keyword = keyword.upper()
    key_repeated = (keyword * (len(plaintext) // len(keyword))) + keyword[:len(plaintext) % len(keyword)]
    
    ciphertext = ''
    for i in range(len(plaintext)):
        if plaintext[i].isalpha():
            row = ord(plaintext[i]) - ord('A')
            col = ord(key_repeated[i]) - ord('A')
            ciphertext += table[row][col]
        else:
            ciphertext += plaintext[i]
    
    return ciphertext

def vigenere_decrypt(ciphertext, keyword):
    table = generate_vigenere_table()
    ciphertext = ciphertext.upper()
    keyword = keyword.upper()
    key_repeated = (keyword * (len(ciphertext) // len(keyword))) + keyword[:len(ciphertext) % len(keyword)]
    
    plaintext = ''
    for i in range(len(ciphertext)):
        if ciphertext[i].isalpha():
            col = ord(key_repeated[i]) - ord('A')
            row = table[col].index(ciphertext[i])
            plaintext += chr(row + ord('A'))
        else:
            plaintext += ciphertext[i]
    
    return plaintext
