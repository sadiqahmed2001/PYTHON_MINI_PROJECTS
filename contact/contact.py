import os  
import json

# File to store contacts
CONTACTS_FILE = 'contacts.json'

def load_contacts():
    """Load contacts from the file."""
    if not os.path.exists(CONTACTS_FILE):
        return []
    with open(CONTACTS_FILE, 'r') as file:
        return json.load(file)

def save_contacts(contacts):
    """Save contacts to the file."""
    with open(CONTACTS_FILE, 'w') as file:
        json.dump(contacts, file, indent=4)

def add_contact(contacts):
    """Add a new contact."""
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    contacts.append({
        'name': name,
        'phone': phone,
        'email': email
    })
    save_contacts(contacts)
    print(f"Contact '{name}' added.")

def view_contacts(contacts):
    """View all contacts."""
    if not contacts:
        print("No contacts found.")
        return
    print("Your contacts:")
    for idx, contact in enumerate(contacts, start=1):
        print(f"{idx}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")

def search_contacts(contacts):
    """Search for a contact by name."""
    query = input("Enter the name to search: ")
    results = [contact for contact in contacts if query.lower() in contact['name'].lower()]
    if not results:
        print("No contacts found.")
    else:
        print("Search results:")
        for idx, contact in enumerate(results, start=1):
            print(f"{idx}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")

def delete_contact(contacts):
    """Delete a contact by its number."""
    view_contacts(contacts)
    try:
        contact_num = int(input("Enter the contact number to delete: "))
        if 1 <= contact_num <= len(contacts):
            removed_contact = contacts.pop(contact_num - 1)
            save_contacts(contacts)
            print(f"Contact '{removed_contact['name']}' deleted.")
        else:
            print("Invalid contact number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    contacts = load_contacts()
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contacts")
        print("4. Delete Contact")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_contacts(contacts)
        elif choice == '4':
            delete_contact(contacts)
        elif choice == '5':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == '__main__':
    main()    
