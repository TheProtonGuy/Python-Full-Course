"""
Create a program where users can add, 
view, and delete contacts using a dictionary.
"""

contacts = []

# {
#     "name": "John Doe",
#     "Number": "123456"
# }

def add_contact():
    name = input("Enter contact name: ")
    number = input("Enter contact number: ")

    contact = {
        "name": name,
        "number": number
    }

    contacts.append(contact)

def view_contacts():
    print("\nBelow are your saved contacts\n")
    for index, contact in enumerate(contacts):
        print(f"Id:{index} Name: {contact['name']} Number: {contact['number']}")

def delete_contact():
    view_contacts()

    contact_id = int(input("Enter the contact id you want to delete: "))
    contacts.pop(contact_id)

def main():
    print("Below are the operations:\n1. Add contact\n2. View contact\n3. Delete contact\n4. Exit")
    while True:
        print("\n")
        operation = int(input("Enter an operation number: "))

        if operation == 1:
            add_contact()
        elif operation == 2:
            view_contacts()
        elif operation == 3:
            delete_contact()
        elif operation == 4:
            break
main()