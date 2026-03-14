import json
import os

FILE = "contacts.json"

def load_contacts():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return {}

def save_contacts(contacts):
    with open(FILE, "w") as f:
        json.dump(contacts, f, indent=4)

def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    contacts[name] = phone
    save_contacts(contacts)
    print("Contact added successfully!")

def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
    for name, phone in contacts.items():
        print(f"{name} : {phone}")

def search_contact(contacts):
    name = input("Enter name to search: ")
    if name in contacts:
        print(f"{name} : {contacts[name]}")
    else:
        print("Contact not found.")

def main():
    contacts = load_contacts()
    while True:
        print("\n1. Add\n2. View\n3. Search\n4. Exit")
        choice = input("Choose option: ")

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
