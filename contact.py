# Task-5 Contact Book in Python

import csv 
import re #used for email validation

names = []; phone_numbers = []; emails = []; addresses = []

# function to load data from csv file    
def loadData():
    filename = 'info.csv'
    names.clear()
    phone_numbers.clear()
    emails.clear()
    addresses.clear()
    try:
        with open(filename, 'r', newline='') as f:
            reader = csv.reader(f)
            try:
                header =  next(reader)
            except StopIteration:
                print("No data  was found...")
                return
            for row in reader:
                names.append(row[0])
                phone_numbers.append(row[1])
                emails.append(row[2])
                addresses.append(row[3])

    except IOError as e:
        print(f"Error : {e}")


# function to save contact information to CSV file
def saveData():
    contacts = zip(names, phone_numbers,  emails, addresses)
    filename = 'info.csv'
    try:
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Name', 'Phone Number', 'Email', 'Address'])
            for contact in contacts:
                writer.writerow(contact)
    except IOError as e:
        print(f"Error saving data: {e}")


def addContact():
    name = input("Enter name: ")
    phone_number=input("Enter phone number:")

    while True: #EMAIL VALIDATION
        email = input("Enter email: ")
        if re.match(r'^[\w\.-]+@[a-zA-Z\d\.-]+\.[a-zA-Z]{2,}$', email):
            break
        else:
            print( "Invalid")

    address = input("Enter address: ")

    names.append(name)
    phone_numbers.append(phone_number)
    emails.append(email)
    addresses.append(address)
    saveData()
    print("\nDetails have been successfully added...")

def viewContact():
    loadData()
    if names:
        for i in range(len(names)):
            print('\nContact:',i+1)
            print("--------------------")
            print("Name:", names[i])
            print("Phone Number:", phone_numbers[i])
            print("Email:",emails[i])
            print("Address:",addresses[i])
            print("--------------------")

def searchContact():
    loadData()
    keyword = input("Enter the name or phone number to search: ")
    found = False

    for i in range(len(names)):
        if keyword.lower() in names[i].lower() or keyword in phone_numbers[i]:
            print("\nWe found the contact...")
            print('\nContact:',i+1)
            print("--------------------")
            print("Name\U000027A1", names[i])
            print("Phone Number\U000027A1",phone_numbers[i])
            print("Email\U000027A1" ,emails[i])
            print("Address\U000027A1" ,addresses[i])
            print("--------------------")
            found = True
    if not found:
        print("No matching contact found.")


def updateContact():
    loadData()
    if names:
        viewContact()
        contactToUpdate = int(input("Choose the no. of contact you want to update: "))

        if 1 <= contactToUpdate <= len(names):
            fieldToUpdate = input("Choose the field you want to update (name, phone_number, email, address): ").lower()

            if fieldToUpdate == 'name':
                updated_name = input("Enter the updated name: ")
                names[contactToUpdate - 1] = updated_name
                print('Name',updated_name,"has been updated.")

            elif fieldToUpdate == 'phone_number':
                updated_phone_number = input("Enter the updated phone number: ")
                phone_numbers[contactToUpdate - 1] = updated_phone_number
                print('Name',updated_phone_number,"has been updated.")
                
            elif fieldToUpdate == 'email':
                updated_email = input("Enter the updated email: ")
                emails[contactToUpdate - 1] = updated_email
                print("Email",updated_email," has been updated.")
            
            elif fieldToUpdate == 'address':
                updated_address = input("Enter the updated address: ")
                addresses[contactToUpdate - 1] = updated_address
                print("Address",updated_address,"has been updated.")
        
        else:
            print("Invalid field name")
    
    else:
        print("Contact list is empty.")
    saveData()

def deleteContact():
    loadData()
    if names:
        viewContact()
        contactToDelete = int(input("Which contact you want to delete: "))
        
        if 1 <= contactToDelete <= len(names):
            deleted_name = names.pop(contactToDelete - 1)
            deleted_phone_number = phone_numbers.pop(contactToDelete - 1)
            deleted_email = emails.pop(contactToDelete - 1)
            deleted_address = addresses.pop(contactToDelete - 1)
            
            print("Contact has been deleted from the list.")
        else:
            print("Invalid")
    else:
        print("Contact list is empty.")
    saveData()

if __name__=="__main__":

    print('\nCONTACT-BOOK \U0001F4F1')

    while True:
        print("\nChoose the operation to be done:")
        print("--------------------------------------")
        print("1. {:<25} {}".format("Add a New Contact \U00002795", "2. View a Contact List\U0001F440"))
        print("3. {:<25} {}".format("Search Contact\U0001F50D", "4.Update a Contact\U0001F4F2"))
        print("5. {:<25} {}".format("Delete a Contact \U0001F5D1", " 6.Exit:\U0001F6D1"))

        choice=input("\nYour Choice:[1/2/3/4/5/6]:")

        if choice=='1': 
            addContact()
        elif choice=='2':
            viewContact()
        elif choice=='3':
            searchContact()
        elif choice=='4':
            updateContact()
        elif choice=='5':
            deleteContact()
        elif choice=='6':
             break
        else:
            print("Wrong Input..")
            
    print("Exiting...")
        
