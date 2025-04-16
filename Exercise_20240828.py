# (1) The program prompts the user to enter a name (e.g., John Smith) and then a phone number (e.g., 0011220011). 
# (2) The program keeps asking the user to enter more names and phone numbers until the user enters “done”. 
# (3) If the user enters “done”, the program creates a new “contacts.txt”* file and saves the data there.

contacts = []

while True:
    contact = input("Enter contact name (or type 'done' to finish): ").strip()
    if contact == 'done':
        with open('contacts.txt', 'a') as file:
            for contact in contacts:
                file.write(f"{(contact[0])} - {contact[1]}\n")
                pass
        break
    else:
        number = input(f"Enter phone number for {contact}: ").strip()
        contacts.append([contact, number])
        
