import json
import os

# Define the file to store contacts
CONTACTS_FILE = 'contacts.json'

# Load contacts from file
def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, 'r') as file:
            return json.load(file)
    return {}

# Save contacts to file
def save_contacts(contacts):
    with open(CONTACTS_FILE, 'w') as file:
        json.dump(contacts, file, indent=4)

# Add a new contact
def add_contact(contacts):
    name = input("Enter name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return
    
    if name in contacts:
        print("Contact already exists.")
        return
    
    phone = input("Enter phone number: ").strip()
    if not phone:
        print("phone cannot be empty.")
        return
    length=len(phone)
    if length == 10:
        print("valid phone number")
    else:
        print("Invalid phone number")
    if phone in contacts:
        print("phone already exists.")
    email = input("Enter email: ").strip()
    if not "@" in email:
        print("Invalid email")
        return
    
    contacts[name] = {
        "phone": phone,
        "email": email
    }
    print("Contact added successfully.")

# Search for a contact by name
def search_contact(contacts):
    name = input("Enter name to search: ").strip()
    contact = contacts.get(name)
    if contact:
        print(f"Name: {name}")
        print(f"Phone: {contact['phone']}")
        print(f"Email: {contact['email']}")
    else:
        print("Contact not found.")

# Update a contact
def update_contact(contacts):
    name = input("Enter name to update: ").strip()
    if name not in contacts:
        print("Contact not found.")
        return
    
    phone = input("Enter new phone number : ").strip()

    email = input("Enter new email : ").strip()
    
    if phone:
        contacts[name]["phone"] = phone
    if email:
        contacts[name]["email"] = email
    print("Contact updated successfully.")

# Display menu and get user choice
def display_menu():
    print("\nContact Management System")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Exit")
    choice = input("Enter your choice: ").strip()
    return choice

# Main function to run the contact management system
def main():
    contacts = load_contacts()
    
    while True:
        choice = display_menu()
        
        if choice == '1':
            add_contact(contacts)
            save_contacts(contacts)
        elif choice == '2':
            search_contact(contacts)
        elif choice == '3':
            update_contact(contacts)
            save_contacts(contacts)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()