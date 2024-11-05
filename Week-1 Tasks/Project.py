import json
import os
Contact = "contacts.json"

# Load contacts from the JSON file if it exists
def load_contacts():
    if os.path.exists(Contact):
        with open(Contact, "r") as file:
            return json.load(file)
    return {}

# Save contacts to the JSON file
def save_contacts(contacts):
    with open(Contact, "w") as file:
        json.dump(contacts, file, indent=5)

# Add a new contact
def add(contacts):
    name = input("Enter contact name: ")
    phone = input("Enter contact phone number: ")
    
    if name in contacts:
        print("Contact already exists.")
    else:
        contacts[name] = {"phone": phone}
        save_contacts(contacts)
        print("Contact added successfully.")

# Search for a contact by name
def search(contacts):
    name = input("Enter the name to search: ")
    contact = contacts.get(name)
    
    if contact:
        print(f"Name: {name}")
        print(f"Phone: {contact['phone']}")
    else:
        print("Contact not found.")

# Update a contact's information
def update(contacts):
    name = input("Enter the name of the contact to update: ")
    
    if name in contacts:
        phone = input("Enter new phone number (leave blank to keep current): ")
        
        if phone:
            contacts[name]["phone"] = phone
        save_contacts(contacts)
        print("Contact updated successfully.")
    else:
        print("Contact not found.")

# Display all contacts
def display(contacts):
    if not contacts:
        print("No contacts found.")
    else:
        for name, info in contacts.items():
            print(f"\nName: {name}")
            print(f"Phone: {info['phone']}")
        print("\nAll contacts displayed.")

# Main menu
def main():
    contacts = load_contacts()
    
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Update Contact")
        print("4. Display All Contacts")
        print("5. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            add(contacts)
        elif choice == "2":
            search(contacts)
        elif choice == "3":
            update(contacts)
        elif choice == "4":
            display(contacts)
        elif choice == "5":
            print("Exiting Contact Management System.")
            break
        else:
            print("Invalid option. Please try again.")

#Calling main function
main()
