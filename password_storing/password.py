import json
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

def encrypt_password(password, key):
    """Encrypt a password."""
    fernet = Fernet(key)
    return fernet.encrypt(password.encode()).decode()

def decrypt_password(encrypted_password, key):
    """Decrypt an encrypted password."""
    fernet = Fernet(key)
    return fernet.decrypt(encrypted_password.encode()).decode()

def save_passwords(passwords, key):
    """Save passwords to a file."""
    with open('passwords.json', 'w') as file:
        json.dump({encrypt_password(account, key): encrypt_password(password, key) for account, password in passwords.items()}, file, indent=4)

def load_passwords(key):
    """Load passwords from a file."""
    if os.path.exists('passwords.json'):
        with open('passwords.json', 'r') as file:
            encrypted_passwords = json.load(file)
            return {decrypt_password(account, key): decrypt_password(password, key) for account, password in encrypted_passwords.items()}
    else:
        return {}

def add_password(passwords, key):
    """Add a new password."""
    account = input("Enter account name: ")
    password = input("Enter password: ")
    passwords[account] = password
    save_passwords(passwords, key)
    print("Password added.")

def view_passwords(passwords):
    """View all passwords."""
    if passwords:
        for account, password in passwords.items():
            print(f"Account: {account}, Password: {password}")
    else:
        print("No passwords found.")

def main():
    key = load_key()
    passwords = load_passwords(key)
    while True:
        print("\nPassword Manager")
        print("1. Add Password")
        print("2. View Passwords")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_password(passwords, key)
        elif choice == '2':
            view_passwords(passwords)
        elif choice == '3':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

if __name__ == '__main__':
    main()
