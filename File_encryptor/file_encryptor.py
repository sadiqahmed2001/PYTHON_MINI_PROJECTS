import os
from cryptography.fernet import Fernet

# Key file to store the encryption key
KEY_FILE = 'key.key'

def generate_key():
    """Generate and save a new encryption key."""
    key = Fernet.generate_key()
    with open(KEY_FILE, 'wb') as file:
        file.write(key)

def load_key():
    """Load the encryption key."""
    if os.path.exists(KEY_FILE):
        with open(KEY_FILE, 'rb') as file:
            return file.read()
    else:
        print("No encryption key found. Generating a new key...")
        generate_key()
        return load_key()

def encrypt_file(filename, key):
    """Encrypt a file."""
    fernet = Fernet(key)
    with open(filename, 'rb') as file:
        data = file.read()
    encrypted_data = fernet.encrypt(data)
    with open(filename + '.encrypted', 'wb') as file:
        file.write(encrypted_data)
    print(f"File '{filename}' encrypted successfully.")

def decrypt_file(filename, key):
    """Decrypt a file."""
    fernet = Fernet(key)
    with open(filename, 'rb') as file:
        encrypted_data = file.read()
    decrypted_data = fernet.decrypt(encrypted_data)
    with open(filename[:-10], 'wb') as file:
        file.write(decrypted_data)
    print(f"File '{filename}' decrypted successfully.")

def main():
    key = load_key()
    while True:
        print("\nFile Encryption and Decryption Tool")
        print("1. Encrypt File")
        print("2. Decrypt File")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            filename = input("Enter the name of the file to encrypt: ")
            if os.path.exists(filename):
                encrypt_file(filename, key)
            else:
                print("File not found.")
        elif choice == '2':
            filename = input("Enter the name of the file to decrypt: ")
            if os.path.exists(filename):
                decrypt_file(filename, key)
            else:
                print("File not found.")
        elif choice == '3':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

if __name__ == '__main__':
    main()
