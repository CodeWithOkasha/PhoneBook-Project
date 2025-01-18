                                      # PhoneBook Small Project

# Define Menu Function of PhoneBook
def PhoneMenu():
    print("\n")
    print("\t\t\t PhoneBook Management System \n")
    print(f"={'=' * 20}")
    print("\n1. Add Contact Number")
    print("2. View Contact List")
    print("3. Update Contact Number")
    print("4. Delete Contact Number")
    print("5. Exit The Program")
    print(f"\n={'='*20}")
    

# Initializing Empty dictionary to store contact name and number
PhoneBook = {}   



# 1. Add Contact Number
def AddNumber():
    contact_name = input("Enter the Name of the Person: ")   #initializing Variable and taking input
    if contact_name in PhoneBook:
        print(f"{contact_name} already exists in the list.")  #Use of F-String Here
    else:
        contact_number = input(f"Please enter the contact number for {contact_name}: ")
        if contact_number.isdigit() and len(contact_number) == 11:   #Applying Validation On Contact Number
            PhoneBook[contact_name] = contact_number        #Assigning Contact Number
            print(f"{contact_name} has been added to the contact list.")
        else:
            print("Please enter a valid contact number (length should be 11 digits).")



# 2. View All Contact Numbers
def ViewNumber():
    if not PhoneBook:
        print("Contact List is Empty.")
    else:
        print("Current Phone List")
        print(f"={'='*20}")
        for contact_name, contact_number in PhoneBook.items():
            print(f"{contact_name} : {contact_number}")
        print(f"={'='*20}")



# 3. Update Contact Number
def UpdateNumber():
    contact_name = input("Enter the Name to update the Number: ")
    if contact_name not in PhoneBook:
        print(f"{contact_name} does not exist in the list.")
    else:
        update_number = input(f"Enter the new number to update for {contact_name}: ")
        if update_number.isdigit() and len(update_number) == 11:
            PhoneBook[contact_name] = update_number
            print(f"Your number has been updated to {update_number} for {contact_name}.")
        else:
            print("Invalid Number. It should be 11 digits.")



# 4. Delete Number
def DeleteNumber():
    contact_name = input("Enter the Name to Delete the Number: ")
    if contact_name not in PhoneBook:
        print(f"{contact_name} does not exist in the list.")
    else:
        del PhoneBook[contact_name]
        print(f"Your Contact {contact_name} has been deleted successfully")



        
#Main Function
def main():
    while True:
        PhoneMenu()
        choice = input("Enter your choice (1-5): ").strip()
        if choice.isdigit():
            choice = int(choice)
            if choice == 1:
                AddNumber()
            elif choice == 2:
                ViewNumber()
            elif choice == 3:
                UpdateNumber()
            elif choice == 4:
                DeleteNumber()
            elif choice == 5:
                print("Exiting the program. Goodbye!")
                break
            else:
                print("Invalid choice! Please enter a number between 1 and 5.")
        else:
            print("Invalid input! Please enter a valid number.")



# Run the program
main()
        



            
