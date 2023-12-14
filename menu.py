import playfair
import shift
import vigenere

def display_menu():
    print("Choose a cipher:")
    print("1. Vigenère Cipher")
    print("2. Playfair Cipher")
    print("3. Caesar Shift Cipher")
    # Add more cipher options as needed
    print("0. Exit")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            # Call Vigenère cipher functions for encryption/decryption
            # Get user inputs (plaintext, keyword) and call vigenere_cipher.encrypt() or vigenere_cipher.decrypt()

        elif choice == "2":
            # Call Playfair cipher functions for encryption/decryption
            # Get user inputs (plaintext, keyword) and call playfair_cipher.encrypt() or playfair_cipher.decrypt()
            
        # Add more elif blocks for other ciphers
        
        elif choice == "0":
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
