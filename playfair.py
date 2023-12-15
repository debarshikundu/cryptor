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
    print(f"Letter '{letter}' not found in the matrix.")
    return None


def playfair_encrypt(plaintext, keyword):
    matrix = generate_playfair_matrix(keyword)
    plaintext = plaintext.upper().replace('J', 'I')  # Convert to uppercase and replace 'J' with 'I'

    # Prepare plaintext by forming pairs of letters and adding an 'X' if necessary
    plaintext_pairs = []
    i = 0
    while i < len(plaintext):
        if i == len(plaintext) - 1 or plaintext[i] == plaintext[i + 1]:
            plaintext_pairs.append(plaintext[i] + 'X')
            i += 1
        else:
            plaintext_pairs.append(plaintext[i] + plaintext[i + 1])
            i += 2

    # Encrypt pairs of letters
    ciphertext = ''
    for pair in plaintext_pairs:
        if len(pair) == 2:
            first, second = pair[0], pair[1]
            if first.isalpha() and second.isalpha():
                row1, col1 = find_positions(matrix, first)
                row2, col2 = find_positions(matrix, second)

                if row1 == row2:  # Same row
                    ciphertext += matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
                elif col1 == col2:  # Same column
                    ciphertext += matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
                else:  # Forming a rectangle
                    ciphertext += matrix[row1][col2] + matrix[row2][col1]
            else:
                ciphertext += pair  # Keep non-alphabetic characters as is

    return ciphertext


def playfair_decrypt(ciphertext, keyword):
    matrix = generate_playfair_matrix(keyword)
    ciphertext = ciphertext.upper().replace('J', 'I')  # Convert to uppercase and replace 'J' with 'I'

    # Decrypt pairs of letters
    plaintext = ''
    for pair in [ciphertext[i:i+2] for i in range(0, len(ciphertext), 2)]:
        if len(pair) == 2:
            first, second = pair[0], pair[1]
            if first.isalpha() and second.isalpha():
                row1, col1 = find_positions(matrix, first)
                row2, col2 = find_positions(matrix, second)

                if row1 == row2:  # Same row
                    plaintext += matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
                elif col1 == col2:  # Same column
                    plaintext += matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
                else:  # Forming a rectangle
                    plaintext += matrix[row1][col2] + matrix[row2][col1]
            else:
                plaintext += pair  # Keep non-alphabetic characters as is
        else:
            plaintext += pair  # Append the last character if it's single

    return plaintext


# Example usage:
plaintext = "HELLO WORLD"
keyword = "KEYWORD"

encrypted_text = playfair_encrypt(plaintext, keyword)
print("Encrypted text:", encrypted_text)

decrypted_text = playfair_decrypt(encrypted_text, keyword)
print("Decrypted text:", decrypted_text)
