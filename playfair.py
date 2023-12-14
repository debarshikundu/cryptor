def generate_playfair_matrix(keyword):
    # Generating the Playfair matrix
    matrix = [[''] * 5 for _ in range(5)]
    alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'  # Skipping 'J'

    keyword = keyword.upper().replace('J', 'I')  # Convert to uppercase and replace 'J' with 'I'
    key_present = set()

    # Fill the matrix with the keyword
    row, col = 0, 0
    for letter in keyword + alphabet:
        if letter not in key_present:
            matrix[row][col] = letter
            key_present.add(letter)
            col += 1
            if col == 5:
                col = 0
                row += 1

    return matrix

def find_positions(matrix, letter):
    # Find positions of a letter in the Playfair matrix
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == letter:
                return i, j

def playfair_encrypt(plaintext, keyword):
    matrix = generate_playfair_matrix(keyword)
    plaintext = plaintext.upper().replace('J', 'I')  # Convert to uppercase and replace 'J' with 'I'
    
    # Prepare plaintext by inserting an 'X' between repeating letters and adding an 'X' at the end if necessary
    plaintext = [plaintext[i] if plaintext[i] != plaintext[i+1] else plaintext[i]+'X' for i in range(0, len(plaintext)-1, 2)]
    plaintext.append(plaintext[-1] if len(plaintext) % 2 == 0 else plaintext[-1]+'X')

    # Encrypt pairs of letters
    ciphertext = ''
    for pair in plaintext:
        first, second = pair[0], pair[1]
        row1, col1 = find_positions(matrix, first)
        row2, col2 = find_positions(matrix, second)

        if row1 == row2:  # Same row
            ciphertext += matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:  # Same column
            ciphertext += matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
        else:  # Forming a rectangle
            ciphertext += matrix[row1][col2] + matrix[row2][col1]

    return ciphertext

def playfair_decrypt(ciphertext, keyword):
    matrix = generate_playfair_matrix(keyword)
    ciphertext = ciphertext.upper().replace('J', 'I')  # Convert to uppercase and replace 'J' with 'I'

    plaintext = ''
    for pair in [ciphertext[i:i+2] for i in range(0, len(ciphertext), 2)]:
        first, second = pair[0], pair[1]
        row1, col1 = find_positions(matrix, first)
        row2, col2 = find_positions(matrix, second)

        if row1 == row2:  # Same row
            plaintext += matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:  # Same column
            plaintext += matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
        else:  # Forming a rectangle
            plaintext += matrix[row1][col2] + matrix[row2][col1]

    return plaintext

# Example usage:
plaintext = "HELLO WORLD"
keyword = "KEYWORD"

encrypted_text = playfair_encrypt(plaintext, keyword)
print("Encrypted text:", encrypted_text)

decrypted_text = playfair_decrypt(encrypted_text, keyword)
print("Decrypted text:", decrypted_text)
