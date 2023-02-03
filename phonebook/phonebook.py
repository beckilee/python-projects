# Becki's Totally Awesome Phonebook!

import sys

# Function to delete an entry from the phonebook, using the current phonebook as argument
def delete_entry(delete_entry_list):
    confirm = False
    found = False
    # Loop until user enters appropriate input: a user ID to delete, return to main menu, or display list of contacts
    while True:
        delete_id = input("If you know the unique ID of the user you want to delete, enter the ID. Or, enter M to return to the main menu, or D to display the list of contacts: ")
        # Print list of contacts
        if delete_id.lower() == "d":
            display_all(delete_entry_list)
            print("")
            continue
        # Return the argument unchanged
        if delete_id.lower() == "m":
            return delete_entry_list
        # Try to list the contact according to ID, or handle exception if it is the wrong type or doesn't exist
        try:
            # Loop through phonebook to find the user with the given ID
            for entry in delete_entry_list:
                # Print favorites with a unicode heart instead of a "y", print non-favorites with a blank space
                if entry["id"] == int(delete_id):
                    if entry["fave"] == "y":
                        fave = "❤️"
                    else:
                        fave = " "
                    # The ID number (minus 1) corresponds to the index in the list, so convert it to a string
                    id_str = str(delete_entry_list[int(delete_id) - 1]["id"])
                    # Print corresponding contact on a single line
                    print(fave + " " + id_str + ". " + delete_entry_list[int(delete_id) - 1]["first_name"] + " " + delete_entry_list[int(delete_id) - 1]["last_name"], end=", ")
                    # This is part of the same line; print all phone numbers
                    for phone in delete_entry_list[int(delete_id) - 1]["phone"]:
                        print(phone, end=", ")
                    # This is part of the same line; add comma after each email address except the last one
                    for i in range(0, len(delete_entry_list[int(delete_id) - 1]["email"])):
                        if i == len(delete_entry_list[int(delete_id) - 1]["email"]) - 1:
                            print(delete_entry_list[int(delete_id) - 1]["email"][i], end="\n")
                        else:
                            print(delete_entry_list[int(delete_id) - 1]["email"][i], end=", ")
                    # Since we found the matching contact, set flag to True
                    found = True
            # Since we didn't find the matching contact, print nice error message
            if found == False:
                    print("Sorry, that ID doesn't exist. Please try again.")
                    continue
        # Catch exception
        except:
            print("Sorry, that wasn't a number. Please try again.")
            continue
        # If the user confirms the user shown is correct, continue with deletion workflow; if they say no or if they enter an incorrect option, start loop over
        confirm_id = input("Do you want to delete this user? Enter Y for yes, N for no: ")
        if confirm_id.lower() == "y" or confirm_id.lower() == "yes":
            confirm = True
            break
        elif confirm_id.lower() == "n" or confirm_id.lower() == "no":
            print("OK, we won't delete that user. Let's try again.")
            continue
        else:
            print("Sorry, that's not an option. Please try again.")
            continue
    # If the user confirmed the deletion, delete the entry and call function to sort the remaining contacts to be in alphabetical order by last name, renumbering IDs accordingly
    if confirm == True:
        del delete_entry_list[int(delete_id) - 1]
        sorted_delete_entry_list = sort_contact(delete_entry_list)
    print("Contact has been deleted.\n")

    # Return the updated and sorted contact list
    return sorted_delete_entry_list


# Function to update an entry in the phonebook, using the current phonebook as argument
def update_entry(update_entry_list):
    confirm = False
    found = False
    # Loop until user enters appropriate input: a user ID to update, return to main menu, or display list of contacts
    while True:
        update_id = input("If you know the unique ID of the user you want to update, enter the ID. Or, enter M to return to the main menu, or D to display the list of contacts: ")
        # Print list of contacts
        if update_id.lower() == "d":
            display_all(update_entry_list)
            print("")
            continue
        # Return the argument unchanged
        if update_id.lower() == "m":
            return update_entry_list
        # Try to list the contact according to ID, or handle exception if it is the wrong type or doesn't exist
        try:
            # Loop through phonebook to find user with the given ID
            for entry in update_entry_list:
                # Print favorites with a unicode heart instead of a "y", print non-favorites with a blank space
                if entry["id"] == int(update_id):
                    if entry["fave"] == "y":
                        fave = "❤️"
                    else:
                        fave = " "
                    # The ID number (minus 1) corresponds to the index in the list, so convert it to a string
                    id_str = str(update_entry_list[int(update_id) - 1]["id"])
                    # Print corresponding contact on a single line
                    print(fave + " " + id_str + ". " + update_entry_list[int(update_id) - 1]["first_name"] + " " + update_entry_list[int(update_id) - 1]["last_name"], end=", ")
                    # This is part of the same line; print all phone numbers
                    for phone in update_entry_list[int(update_id) - 1]["phone"]:
                        print(phone, end=", ")
                    # This is part of the same line; add comma after each email address except the last one
                    for i in range(0, len(update_entry_list[int(update_id) - 1]["email"])):
                        if i == len(update_entry_list[int(update_id) - 1]["email"]) - 1:
                            print(update_entry_list[int(update_id) - 1]["email"][i], end="\n")
                        else:
                            print(update_entry_list[int(update_id) - 1]["email"][i], end=", ")
                    # Since we found the matching contact, set flag to True
                    found = True
            # Since we didn't find the matching contact, print nice error message
            if found == False:
                    print("Sorry, that ID doesn't exist. Please try again.")
                    continue
        # Catch exception
        except:
            print("Sorry, that wasn't a number. Please try again.")
            continue
        # If the user confirms the user shown is correct, continue with update workflow; if they say no or if they enter an incorrect option, start loop over
        confirm_id = input("Do you want to update this user? Enter Y for yes, N for no: ")
        if confirm_id.lower() == "y" or confirm_id.lower() == "yes":
            confirm = True
            break
        elif confirm_id.lower() == "n" or confirm_id.lower() == "no":
            print("OK, we won't update that user. Let's try again.")
            continue
        else:
            print("Sorry, that's not an option. Please try again.")
            continue
    # If the user confirmed the update, prompt for new information and call function to sort the updated list of contacts to be in alphabetical order by last name, renumbering IDs accordingly
    if confirm == True:
        first = input("Enter the updated contact's first name: ")
        last = input("Enter the contact's last name: ")
        email = ""
        phone = ""
        phone_list = list()
        email_list = list()
        # Loop phone entry until user says they're "done"
        while True:
            if phone.lower() == "done":
                break
            else:
                phone = input("Enter a phone number, or DONE when you're done: ")
                if phone.lower() == "done":
                    continue
                phone_list.append(phone)
                continue
        # Loop email entry until user says they're "done"
        while True:
            if email.lower() == "done":
                break
            else:
                email = input("Enter an email address, or DONE when you're done: ")
                if email.lower() == "done":
                    continue
                email_list.append(email)
                continue
        fave = input("Enter Y if you want to mark this contact as a favorite, otherwise enter anything else: ")
        if fave.lower() == "y":
            fave = "y"
        else:
            fave = "n"
        # Update-in-place the entry corresponding to ID
        update_entry_list[int(update_id) - 1] = { "fave" : fave, "id" : "temp_id", "first_name" : first, "last_name" : last, "phone" : phone_list, "email" : email_list }
        # Call function to sort updated contact list
        sorted_update_entry_list = sort_contact(update_entry_list)
        # Print updated contact details
        print("Updated entry:")
        # The ID number (minus 1) corresponds to the index in the list, so convert it to a string
        id_str = str(sorted_update_entry_list[int(update_id) - 1]["id"])
        # Print favorites with a unicode heart instead of a "y", print non-favorites with a blank space
        if fave == "y":
            fave = "❤️"
        else:
            fave = " "
        # Print corresponding contact on a single line
        print(fave + " " + id_str + ". " + sorted_update_entry_list[int(update_id) - 1]["first_name"] + " " + sorted_update_entry_list[int(update_id) - 1]["last_name"], end=", ")
        # This is part of the same line; print all phone numbers
        for phone in sorted_update_entry_list[int(update_id) - 1]["phone"]:
            print(phone, end=", ")
        # This is part of the same line; add comma after each email address except the last one
        for i in range(0, len(sorted_update_entry_list[int(update_id) - 1]["email"])):
            if i == len(sorted_update_entry_list[int(update_id) - 1]["email"]) - 1:
                print(sorted_update_entry_list[int(update_id) - 1]["email"][i], end="\n")
            else:
                print(sorted_update_entry_list[int(update_id) - 1]["email"][i], end=", ")
    print("")

    # Return the updated and sorted contact list
    return sorted_update_entry_list


# Function to add an entry to the phonebook, using the current phonebook as argument
def add_entry(old_entry_list):
    # Prompt for new contact info and call function to sort the updated contacts to be in alphabetical order by last name, renumbering IDs accordingly
    first = input("Enter the new contact's first name: ")
    last = input("Enter the last name: ")
    email = ""
    phone = ""
    phone_list = list()
    email_list = list()
    add_entry_list = list()
    # Loop phone entry until user says they're "done"
    while True:
        if phone.lower() == "done":
            break
        else:
            phone = input("Enter a phone number, or DONE when you're done: ")
            if phone.lower() == "done":
                continue
            phone_list.append(phone)
            continue
    # Loop phone entry until user says they're "done"
    while True:
        if email.lower() == "done":
            break
        else:
            email = input("Enter an email address, or DONE when you're done: ")
            if email.lower() == "done":
                continue
            email_list.append(email)
            continue
    fave = input("Enter Y if you want to mark this contact as a favorite, otherwise enter anything else: ")
    if fave.lower() == "y":
        fave = "y"
    else:
        fave = "n"
    # Assign new contact info to a new entry
    new_entry = { "fave" : fave, "id" : "temp_id", "first_name" : first, "last_name" : last, "phone" : phone_list, "email" : email_list }
    # Add new entry to the list of contacts
    old_entry_list.append(new_entry)
    # Call function to sort the updated contact list
    add_entry_list = sort_contact(old_entry_list)
    print("")

    # Return the updated and sorted contact list
    return add_entry_list


# Function to search contacts by name, using the current phonebook as argument
def name_search(query, search_entry_list):
    print("")
    found = False
    # If the user doesn't enter a query, print all entries
    if query == "":
        print("-------------------------------SEARCH RESULTS-------------------------------")
        print("Favorite | Unique ID | First Name | Last Name | Phone Number(s) | Email Address(es)")
        print("----------------------------------------------------------------------------\n")
        print("No query submitted; printing all entries:\n")
    # If the user enters a query, actually perform the search
    else:
        print("-------------------------------SEARCH RESULTS-------------------------------")
        print("Favorite | Unique ID | First Name | Last Name | Phone Number(s) | Email Address(es)")
        print("----------------------------------------------------------------------------\n")
        print("Entries matching " + query + ":\n")
    # Loop through contact list (list of dicts) to see if the query matches ANY PART of the first name or last name
    for entry in search_entry_list:
        # If there's a match, print each one out on a single line
        if query.lower() in entry["first_name"].lower() or query.lower() in entry["last_name"].lower():
            fave = str()
            # Print favorites with a unicode heart instead of a "y", print non-favorites with a blank space
            if entry["fave"] == "y":
                fave = "❤️"
            else:
                fave = " "
            # The ID number (minus 1) corresponds to the index in the list, so convert it to a string
            id_str = str(entry["id"])
            # Print corresponding contact on a single line
            print(fave + " " + id_str + ". " + entry["first_name"] + " " + entry["last_name"], end=", ")
            # This is part of the same line; print all phone numbers
            for phone in entry["phone"]:
                print(phone, end=", ")
            # This is part of the same line; add comma after each email address except the last one
            for i in range(0, len(entry["email"])):
                if i == len(entry["email"]) - 1:
                    print(entry["email"][i], end="\n")
                else:
                    print(entry["email"][i], end=", ")
            # Since we found a matching contact, set flag to True
            found = True
    # Since we didn't find ANY matching contact, print nice error message
    if found == False:
        print("-------------------------------SEARCH RESULTS-------------------------------")
        print("Favorite | Unique ID | First Name | Last Name | Phone Number(s) | Email Address(es)")
        print("----------------------------------------------------------------------------\n")
        print("No entries found")
    print("")


# Function to search contacts by phone number, using the current phonebook as argument
def phone_search(query, search_entry_list):
    print("")
    found = False
    # If the user doesn't enter a query, print all entries
    if query == "":
        print("-------------------------------SEARCH RESULTS-------------------------------")
        print("Favorite | Unique ID | First Name | Last Name | Phone Number(s) | Email Address(es)")
        print("----------------------------------------------------------------------------\n")
        print("No query submitted; printing all entries:\n")
        display_all(search_entry_list)
        found = True
    # If the user enters a query, actually perform the search
    else:
        print("-------------------------------SEARCH RESULTS-------------------------------")
        print("Favorite | Unique ID | First Name | Last Name | Phone Number(s) | Email Address(es)")
        print("----------------------------------------------------------------------------\n")
        print("Entries matching " + query + ":\n")
        dupe_list = list()
        # Loop through phone list in contact list (a list of strings in a dict in a list) to see if the query matches ANY PART of any phone numbers in an entry
        for entry in search_entry_list:
            for phone in entry["phone"]:
                for i in range(0, len(phone)):
                    # If there's a match, print each one out on a single line
                    if query in phone:
                        # If the contact already has one phone number that matches, break out of the loop and go to the next contact (to avoid printing the same contact multiple times)
                        if entry["id"] in dupe_list:
                            break
                        # If it's the first time a contact has matched a phone number, add it to a list (to avoid printing the same contact multiple times)
                        dupe_list.append(entry["id"])
                        fave = str()
                        # Print favorites with a unicode heart instead of a "y", print non-favorites with a blank space
                        if entry["fave"] == "y":
                            fave = "❤️"
                        else:
                            fave = " "
                        # The ID number (minus 1) corresponds to the index in the list, so convert it to a string
                        id_str = str(entry["id"])
                        # Print corresponding contact on a single line
                        print(fave + " " + id_str + ". " + entry["first_name"] + " " + entry["last_name"], end=", ")
                        # This is part of the same line; print all phone numbers
                        for phone in entry["phone"]:
                            print(phone, end=", ")
                        # This is part of the same line; add comma after each email address except the last one
                        for i in range(0, len(entry["email"])):
                            if i == len(entry["email"]) - 1:
                                print(entry["email"][i], end="\n")
                            else:
                                print(entry["email"][i], end=", ")
                        # Since we found a matching contact, set flag to True
                        found = True
                    break
    # Since we didn't find ANY matching contact, print nice error message
    if found == False:
        print("-------------------------------SEARCH RESULTS-------------------------------")
        print("Favorite | Unique ID | First Name | Last Name | Phone Number(s) | Email Address(es)")
        print("----------------------------------------------------------------------------\n")
        print("No entries found")
    print("")


# Function to search contacts by email address, using the current phonebook as argument
def email_search(query, search_entry_list):
    print("")
    found = False
    # If the user doesn't enter a query, print all entries
    if query == "":
        print("-------------------------------SEARCH RESULTS-------------------------------")
        print("Favorite | Unique ID | First Name | Last Name | Phone Number(s) | Email Address(es)")
        print("----------------------------------------------------------------------------\n")
        print("No query submitted; printing all entries with email addresses:\n")
        display_all(search_entry_list)
        found = True
    # If the user enters a query, actually perform the search
    else:
        print("-------------------------------SEARCH RESULTS-------------------------------")
        print("Favorite | Unique ID | First Name | Last Name | Phone Number(s) | Email Address(es)")
        print("----------------------------------------------------------------------------\n")
        print("Entries matching " + query + ":\n")
        dupe_list = list()
        # Loop through email list in contact list (a list of strings in a dict in a list) to see if the query matches ANY PART of any email addresses in an entry
        for entry in search_entry_list:
            for email in entry["email"]:
                for i in range(0, len(email)):
                    # If there's a match, print each one out on a single line
                    if query.lower() in email.lower():
                        # If the contact already has one email that matches, break out of the loop and go to the next contact (to avoid printing the same contact multiple times)
                        if entry["id"] in dupe_list:
                            break
                        # If it's the first time a contact has matched an email, add it to a list (to avoid printing the same contact multiple times)
                        dupe_list.append(entry["id"])
                        fave = str()
                        # Print favorites with a unicode heart instead of a "y", print non-favorites with a blank space
                        if entry["fave"] == "y":
                            fave = "❤️"
                        else:
                            fave = " "
                        # The ID number (minus 1) corresponds to the index in the list, so convert it to a string
                        id_str = str(entry["id"])
                        # Print corresponding contact on a single line
                        print(fave + " " + id_str + ". " + entry["first_name"] + " " + entry["last_name"], end=", ")
                        # This is part of the same line; print all phone numbers
                        for phone in entry["phone"]:
                            print(phone, end=", ")
                        # This is part of the same line; add comma after each email address except the last one
                        for i in range(0, len(entry["email"])):
                            if i == len(entry["email"]) - 1:
                                print(entry["email"][i], end="\n")
                            else:
                                print(entry["email"][i], end=", ")
                        # Since we found a matching contact, set flag to True
                        found = True
                    break
    # Since we didn't find ANY matching contact, print nice error message
    if found == False:
        print("No entries found")
    print("")


# Function to display all entries in the phonebook, using the current phonebook as argument
def display_all(display_entry_list):
    print("------------------------------LIST OF ALL CONTACTS------------------------------")
    print("Favorite | Unique ID | First Name | Last Name | Phone Number(s) | Email Address(es)")
    print("--------------------------------------------------------------------------------\n")
    # If there aren't any entries, print a nice error message
    if len(display_entry_list) == 0:
        print("No entries found")
    # If there are any entries, print each on a single line
    else:
        fave = str()
        # Print favorites with a unicode heart instead of a "y", print non-favorites with a blank space
        for entry in display_entry_list:
            if entry["fave"] == "y":
                fave = "❤️"
            else:
                fave = " "
            # Convert the ID to a string
            id_str = str(entry["id"])
            # Print corresponding contact on a single line
            print(fave + " " + id_str + ". " + entry["first_name"] + " " + entry["last_name"], end=", ")
            # This is part of the same line; print all phone numbers
            for phone in entry["phone"]:
                print(phone, end=", ")
            # This is part of the same line; add comma after each email address except the last one
            for i in range(0, len(entry["email"])):
                if i == len(entry["email"]) - 1:
                    print(entry["email"][i], end="\n")
                else:
                    print(entry["email"][i], end=", ")
    print("")


# Function to display all FAVORITE entries in the phonebook, using the current phonebook as argument
def display_faves(fave_entry_list):
    print("---------------------------LIST OF FAVORITE CONTACTS----------------------------")
    print("Favorite | Unique ID | First Name | Last Name | Phone Number(s) | Email Address(es)")
    print("--------------------------------------------------------------------------------\n")
    fave = str()
    is_fave = False
    # If there are any entries, print each on a single line
    for entry in fave_entry_list:
        # Print favorites with a unicode heart instead of a "y", print non-favorites with a blank space
        if entry["fave"] == "y":
            fave = "❤️"
            is_fave = True
            # Convert the ID to a string
            id_str = str(entry["id"])
            # Print corresponding contact on a single line
            print(fave + " " + id_str + ". " + entry["first_name"] + " " + entry["last_name"], end=", ")
            # This is part of the same line; print all phone numbers
            for phone in entry["phone"]:
                print(phone, end=", ")
            # This is part of the same line; add comma after each email address except the last one
            for i in range(0, len(entry["email"])):
                if i == len(entry["email"]) - 1:
                    print(entry["email"][i], end="\n")
                else:
                    print(entry["email"][i], end=", ")
    # If there aren't any favorites, print a nice error message
    if is_fave == False:
        print("No favorites found")
    print("")


# Function to display main menu and prompt user for a choice, using current phonebook as argument
def menu(current_entry_list):
    # Loop main menu list and input prompt until they enter a choice
    while True:
        print("===================================MAIN MENU====================================")
        print("Welcome to the main menu!")
        print("Each letter below corresponds to a task:\n")
        print("s - Search contacts by category")
        print("l - List all contacts")
        print("f - List favorite contacts")
        print("a - Add a new contact")
        print("u - Update a contact")
        print("d - Delete a contact")
        print("x - Save and exit")
        print("")
        print("What would you like to do?")
        # Call the function corresponding to the action the user entered, using the current phone book as argument; user starts loop again after a function is finished
        choice = input("Enter a letter: ")
        if choice.lower() == "s":
            print("")
            search_menu(current_entry_list)
            continue
        if choice.lower() == "l":
            print("")
            display_all(current_entry_list)
            print("")
            continue
        if choice.lower() == "f":
            print("")
            display_faves(current_entry_list)
            print("")
            continue
        if choice.lower() == "a":
            print("")
            current_entry_list = add_entry(current_entry_list)
            continue
        if choice.lower() == "u":
            current_entry_list = update_entry(current_entry_list)
            continue
        if choice.lower() == "d":
            current_entry_list = delete_entry(current_entry_list)
            continue
        if choice.lower() == "x":
            exit_app(current_entry_list)
        # Print nice error message if the user enters anything that doesn't correspond to a menu action
        else:
            print("Sorry, that's not an option. Please try again: ")


# Function to display a menu listing search actions and prompt user for a choice, using current phonebook as argument
def search_menu(current_entry_list):
    print("How would you like to search?")
    print("Each letter below corresponds to a task:\n")
    print("n - Search by name")
    print("p - Search by phone")
    print("e - Search by email\n")
    # Loop search menu list and input prompt until they enter a choice
    while True:
        choice = input("Enter a letter: ")
        # Call the function corresponding to the action the user entered; user returns to main menu after a function is finished
        if choice.lower() == "n":
            query = input("\nEnter a name, or as many letters as you know: ")
            name_search(query, current_entry_list)
            break
        if choice.lower() == "p":
            query = input("\nEnter a phone number, or as many digits as you know: ")
            phone_search(query, current_entry_list)
            break
        if choice.lower() == "e":
            query = input("\nEnter an email address, or as many letters as you know: ")
            email_search(query, current_entry_list)
            break
        # Print nice error message if the user enters anything that doesn't correspond to a menu action, then start loop over
        else:
            print("Sorry, that's not an option. Please try again: ")


# Function to sort a contact list in alphabetical order by last name (case insensitive) and then by first name, then renumber the contact IDs according to new order, using current phonebook as argument
def sort_contact(raw_entry_list):
    sorted_entry_list = list()
    # Inspiration from https://www.geeksforgeeks.org/ways-sort-list-dictionaries-values-python-using-lambda-function/ and https://docs.python.org/3.7/library/functions.html#sorted
    # Sort by last name, then by first name (case insensitive)
    unsorted_entry_list = sorted(raw_entry_list, key = lambda i: (i["last_name"].lower(), i["first_name"].lower()))
    # Renumber the contact list IDs according to new order
    for i in range(0, len(unsorted_entry_list)):
        unsorted_entry_list[i] = { "fave" : unsorted_entry_list[i]["fave"], "id" : "temp_id", "first_name" : unsorted_entry_list[i]["first_name"], "last_name" : unsorted_entry_list[i]["last_name"], "phone": unsorted_entry_list[i]["phone"], "email": unsorted_entry_list[i]["email"] }
        # Add 1 to the index so ID numbering starts at 1 instead of 0
        unsorted_entry_list[i]["id"] = i + 1
        # Add each updated entry to a new list
        sorted_entry_list.append(unsorted_entry_list[i])

    # Return the sorted contact list
    return sorted_entry_list


# Function to load the phonebook, or create one if it doesn't exist
def load():
    sorted_entry_list = list()
    print("Loading bta_phonebook.txt...\n")
    # Try to load the phonebook file, and handle exception if the file doesn't exist
    try:
        fhand = open("bta_phonebook.txt")
    # If file doesn't exist, create new file and return the blank contact list
    except:
        fhand = open("bta_phonebook.txt", "w")
        print("NO PHONEBOOK FOUND! Creating a new one.\n")
        return sorted_entry_list
    raw_entry_list = list()
    # Loop to process each comma-separated category (and semicolon-separated list within the category items, i.e., phone numbers and email addresses)
    for line in fhand:
        line = line.strip()
        line = line.split(",")
        # If there are not enough categories or too many categories, print nice error message and exit gracefully
        if len(line) != 6:
            print("Sorry, each entry in the phone book should have six categories separated by commas. If you don't want to fill out a category, leave it blank but leave the commas around it. Please check bta_phonebook.txt and run the program again.")
            sys.exit(0)
        # Grab contents of each category
        fave = line[0]
        first_name = line[2]
        last_name = line[3]
        phone = line[4]
        phone = phone.split(";")
        email = line[5]
        email = email.split(";")
        # Assign each category to a dict key-value pair
        unsorted_entry = { "fave" : fave, "first_name" : first_name, "last_name" : last_name, "phone": phone, "email": email }
        # Assign each dict to a list
        raw_entry_list.append(unsorted_entry)
        # Call function to sort list and number IDs accordingly
        sorted_entry_list = sort_contact(raw_entry_list)
    # Close file when done reading from it
    fhand.close()

    # Return the new/sorted contact list
    return sorted_entry_list


# Function to exit the program and save current contact list to phonebook file, using current phonebook as argument
def exit_app(sorted_entry_list):
    f = open("bta_phonebook.txt", "w")
    email_str = str()
    phone_str = str()
    # Loop through entries, convert each ID to string, and if there are multiple phone numbers and/or email addresses, join them with a semicolon
    for entry in sorted_entry_list:
        id_str = str(entry["id"])
        email_str = ";".join(entry["email"])
        phone_str = ";".join(entry["phone"])
        # Write each converted entry to the phonebook file
        f.write(entry["fave"] + "," + id_str + "," + entry["first_name"] + "," + entry["last_name"] + "," + phone_str + "," + email_str + "\n")
    print("\nThanks for using Becki's Totally Awesome Phonebook! Your phonebook has been saved to bta_phonebook.txt.")
    # Close file when done writing to it
    f.close()
    # Exit gracefully
    sys.exit(0)



# Call function to load the phonebook
entry_list = load()

print("========================BECKI'S TOTALLY AWESOME PHONEBOOK=======================")

# Call function to display main menu
menu(entry_list)
