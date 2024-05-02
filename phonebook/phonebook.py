# Becki's Totally Awesome Phonebook App!
# Now with ~even more awesome~

import sqlite3
from sqlite3 import Error
from pytablewriter import SpaceAlignedTableWriter
import phonenumbers

# Create database if it doesn't exist; otherwise, connect to it
def create_connection():
    try:
        connection = sqlite3.connect('bta-phonebook.db')
        return connection
    except Error as e:
        print("❗️ Sorry, we encountered an error: ", e)
        connection.close()
        exit(1)

# Create contacts table if it doesn't exist
def create_contacts_table(conn):
    try:
        cursor = conn.cursor()
        cursor.execute(""" CREATE TABLE IF NOT EXISTS contacts (
                        contact_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        first_name TEXT NOT NULL,
                        last_name TEXT,
                        phone TEXT,
                        email TEXT
                        ); """)
        conn.commit()
        cursor.close()
    except Error as e:
        print("❗️ Sorry, we encountered an error creating the table: ", e)
        print("Please contact becki.lee@gmail.com with details so I can help you troubleshoot!")
        conn.close()
        exit(1)

# Create favorites table if it doesn't exist
def create_faves_table(conn):
    try:
        cursor = conn.cursor()
        cursor.execute(""" CREATE TABLE IF NOT EXISTS favorites (
                        favorite_id INTEGER PRIMARY KEY,
                        contact_id INTEGER UNIQUE,
                        FOREIGN KEY (contact_id) REFERENCES contacts(contact_id) ON DELETE CASCADE
                        ); """)
        conn.commit()
        cursor.close()
    except Error as e:
        print("❗️ Sorry, we encountered an error creating the table: ", e)
        print("Please contact becki.lee@gmail.com with details so I can help you troubleshoot!")
        conn.close()
        exit(1)

# Validate phone number.
# Normalize the phone number to E164 format, or format as international,
# based on parameters from calling function
def normalize_or_format_phone(raw_phone, operation, default_region="US"):
    if operation == "normalize":
        phone_format = phonenumbers.PhoneNumberFormat.E164
    elif operation == "format":
        phone_format = phonenumbers.PhoneNumberFormat.INTERNATIONAL
    else:
        raise ValueError
    try:
        phone_number = phonenumbers.parse(raw_phone, default_region)
        if phonenumbers.is_valid_number(phone_number) is True and phonenumbers.is_possible_number(phone_number) is True:
            phone = phonenumbers.format_number(phone_number, phone_format)
            return phone
    except phonenumbers.phonenumberutil.NumberParseException as n:
        print("❗️ Sorry, we encountered an error: ", n)
    except ValueError as v:
        print("❗️ Sorry, we encountered a value error: ", v)
    except Error as e:
        print("❗️ Sorry, we encountered a general error: ", e)

# Search by name, phone, or email, then show results. Support partial matches.
def search_contacts(conn):
    cursor = conn.cursor()
    while True:
        choice = input("Enter N to search by name, P to search by phone, or E to search by email: ")
        if choice.upper() != "N" and choice.upper() != "P" and choice.upper() != "E":
            print("")
            print("Sorry, that's not a valid menu option. Please try again.")
            continue
        query = input("Enter a search term. Partial matches are supported: ")
        category_query = f"%{query}%"
        cursor = conn.cursor()
        if choice.upper() == "N":
            sql = f""" SELECT (f.contact_id IS NOT NULL) as is_favorite,
                                c.contact_id,
                                c.first_name,
                                c.last_name,
                                c.phone,
                                c.email
                            FROM contacts c
                            LEFT JOIN favorites f ON c.contact_id = f.contact_id
                            WHERE c.first_name LIKE ? OR c.last_name LIKE ?; """
            cursor.execute(sql, (category_query, category_query))
        elif choice.upper() == "P":
            sql = """ SELECT (f.contact_id IS NOT NULL) as is_favorite,
                                c.contact_id,
                                c.first_name,
                                c.last_name,
                                c.phone,
                                c.email
                            FROM contacts c
                            LEFT JOIN favorites f ON c.contact_id = f.contact_id
                            WHERE c.phone LIKE ?; """
            cursor.execute(sql, (category_query, ))
        elif choice.upper() == "E":
            sql = """ SELECT (f.contact_id IS NOT NULL) as is_favorite,
                                c.contact_id,
                                c.first_name,
                                c.last_name,
                                c.phone,
                                c.email
                            FROM contacts c
                            LEFT JOIN favorites f ON c.contact_id = f.contact_id
                            WHERE c.email LIKE ?; """
            cursor.execute(sql, (category_query, ))
        rows = cursor.fetchall()
        print("")
        print("Entries matching '" + query + "':")
        display_contacts_table(rows)
        break

# List contacts, or print message if no contacts exist
def list_contacts(conn, contacts_list_type):
    if contacts_list_type == "all":
        sql = """ SELECT f.favorite_id,
                                c.contact_id,
                                c.first_name,
                                c.last_name,
                                c.phone,
                                c.email
                            FROM contacts c
                            LEFT JOIN favorites f ON c.contact_id = f.contact_id; """
    elif contacts_list_type == "faves":
        sql = """ SELECT f.favorite_id,
                                c.contact_id,
                                c.first_name,
                                c.last_name,
                                c.phone,
                                c.email
                            FROM contacts c
                            JOIN favorites f ON c.contact_id = f.contact_id
                            ORDER BY c.contact_id ASC; """
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        print("")
        display_contacts_table(rows)
        cursor.close()
    except Error as e:
        print("❗️ Sorry, we encountered an error: ", e)
        print("")

# Display the contacts table nicely
def display_contacts_table(rows):
    if len(rows) == 0:
        print("No contacts found.")
        print("")
        return False
    else:
        value_matrix = [[str(row[0]), str(row[1]), row[2] + " " + row[3], normalize_or_format_phone(row[4], operation="format"), row[5]] for row in rows]
        for column in value_matrix:
            if column[0] != "None" and column[0] != "0":
                column[0] = "💖"
            else:
                column[0] = ""
        writer = SpaceAlignedTableWriter(
            table_name="Contacts",
            headers=["💖", "ID", "NAME", "PHONE", "EMAIL"],
            value_matrix=value_matrix,
            margin=1
        )
        writer.write_table()
        writer.close()
        print("")

# Add a new contact
def add_contact(conn):
    try:
        print("Enter the contact's information.")
        first_name = input("Enter FIRST NAME: ")
        last_name = input("Enter LAST NAME: ")
        while True:
            unformatted_phone = input("Enter PHONE NUMBER. Non-US phone numbers must begin with\n    a plus sign and country code (for example, +44): ")
            phone = normalize_or_format_phone(unformatted_phone, operation="normalize")
            if phone is None:
                print("Please enter a valid phone number.")
                continue
            else:
                break
        email = input("Enter EMAIL ADDRESS: ")
        is_favorite = confirm_contact("favorite", "skip")
        sql_contacts = """ INSERT into contacts (first_name, last_name, phone, email)
                VALUES(?,?,?,?) """
        sql_favorites = "INSERT into favorites (contact_id) VALUES(?)"
        cursor = conn.cursor()
        cursor.execute(sql_contacts, (first_name, last_name, phone, email))
        conn.commit()
        contact_id = cursor.lastrowid
        if is_favorite is True:
            cursor.execute(sql_favorites, (contact_id,))
            conn.commit()
        cursor.close()
        print("")
        print("👍 Contact added!")
        print("")
        return cursor.lastrowid
    except Error as e:
        print(e)
        print("")

# Look up contact by ID, or print message if ID does not exist
def look_up_contact_by_id(conn, id):
    is_found = False
    cursor = conn.cursor()
    try:
        cursor.execute(""" SELECT (f.contact_id IS NOT NULL) as is_favorite,
                                c.contact_id,
                                c.first_name,
                                c.last_name,
                                c.phone,
                                c.email
                            FROM contacts c
                            LEFT JOIN favorites f ON c.contact_id = f.contact_id
                            WHERE c.contact_id = ?; """, (id,))
        rows = cursor.fetchall()
        print("")
        display_contacts_table(rows)
        print("")
        if len(rows) != 0:
            is_found = True
    except Error as e:
        print("❗️ Sorry, we encountered an error: ", e)
        print("")
        is_found = False
    return is_found

# Delete or update the contact, depending on parameter passed from calling function
def delete_or_update(conn, operation):
    while True:
        choice = input("Enter an ID to " + operation + " a contact, L to list contacts, or Q to quit: ")
        if choice.upper() == "L":
            list_contacts(conn, "all")
        elif choice.upper() == "Q":
            print("")
            print("Canceled " + operation + ". Returning to main menu.")
            print("")
            break
        else:
            if not choice.isdigit():
                print("")
                print("Please enter a numeric ID.")
                print("")
                continue
            contact_id = int(choice)
            if not look_up_contact_by_id(conn, contact_id):
                continue
            if operation == "update":
                if confirm_contact("update", "cancel"):
                    perform_contact_update(conn, contact_id)
                    break
            elif operation == "delete":
                print("⚠️ Delete this contact?")
                if confirm_contact("delete", "cancel"):
                    perform_contact_delete(conn, contact_id)
                    break
            else:
                print("")
                print("Contact was not updated.")

# Confirm operation (can be update, delete, or set favorite)
def confirm_contact(action, cancel_action):
    is_confirmed = False
    while True:
        choice_confirm = input("Enter Y to " + action + " this contact, or N to " + cancel_action + ": ")
        if choice_confirm.upper() == "Y":
            print("")
            is_confirmed = True
            break
        elif choice_confirm.upper() == "N":
            break
        else:
            print("")
            print("Please enter Y for yes, or N for no.")
            continue
    return is_confirmed

# Request new contact details from user
def get_updated_contact_details(existing_contact_info):
    new_first_name = input("Enter FIRST NAME, or leave blank to keep current value: ") or existing_contact_info[0]
    new_last_name = input("Enter LAST NAME, or leave blank to keep current value: ") or existing_contact_info[1]
    while True:
        new_phone = input("Enter PHONE NUMBER, or leave blank to keep current value. Non-US phone numbers must\n      begin with plus sign and country code (for example, +44): ") or existing_contact_info[2]
        if not normalize_or_format_phone(new_phone, operation="normalize"):
            print("Please enter a valid phone number.")
            continue
        else:
            break
    new_email = input("Enter EMAIL ADDRESS, or leave blank to keep current value: ") or existing_contact_info[3]
    updated_contact_info = (new_first_name, new_last_name, new_phone, new_email)
    return updated_contact_info

# Ask user if they want to set the contact as a favorite.
# Check whether the contact is already a favorite.
def update_favorites(conn, contact_id):
    cursor = conn.cursor()
    is_favorite = confirm_contact("favorite", "skip")
    sql_look_up_favorites = "SELECT favorite_id FROM favorites WHERE contact_id = ?"
    sql_favorites = "INSERT into favorites (contact_id) VALUES(?)"
    cursor.execute(sql_look_up_favorites, (contact_id, ))
    favorite_exists = cursor.fetchone()
    if is_favorite is True and favorite_exists is None:
        cursor.execute(sql_favorites, (contact_id, ))
        conn.commit()
    elif is_favorite is False and favorite_exists is not None:
        cursor.execute("DELETE FROM favorites WHERE contact_id = ?", (contact_id, ))
        conn.commit()
        print("")

# Commit update operation
def perform_contact_update(conn, contact_id):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT first_name, last_name, phone, email FROM contacts WHERE contact_id = ?", (contact_id,))
        existing_contact_info = cursor.fetchone()
        updated_contact_info = get_updated_contact_details(existing_contact_info)
        sql_contacts = """ UPDATE contacts
                SET first_name = ?,
                    last_name = ?,
                    phone = ?,
                    email = ?
                WHERE contact_id = ? """
        cursor.execute(sql_contacts, (updated_contact_info[0], updated_contact_info[1], updated_contact_info[2], updated_contact_info[3], contact_id))
        conn.commit()
        update_favorites(conn, contact_id)
        cursor.close()
        print("👍 Contact updated!")
        print("")
        return cursor.lastrowid
    except Error as e:
        print("❗️ Sorry, we encountered an error: ", e)
        print("")

# Commit delete operation
def perform_contact_delete(conn, id):
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM contacts WHERE contact_id = ?", (id,))
        conn.commit()
        print("🗑️ Contact deleted!")
        print("")
        cursor.close()
    except Error as e:
        print("❗️ Sorry, we encountered an error: ", e)
        print("")

# Close database connection
def close_connection(conn):
    if conn:
        conn.close()

# Print the main menu and loop until user chooses to exit
def main_menu(conn):
    print("============= ✨ BECKI'S TOTALLY AWESOME PHONEBOOK APP ✨ ==============")
    print("")
    print("S - 🔎 SEARCH contacts")
    print("L - 📋 LIST all contacts")
    print("F - 💖 Show FAVORITE contacts")
    print("A - ➕ ADD a new contact")
    print("U - ☝️  UPDATE a contact")
    print("D - ❌ DELETE a contact")
    print("Q - 🚪 QUIT this application")
    print("")
    choice = input("Enter a letter to take an action: ")
    if choice.upper() == "S":
        search_contacts(conn)
    elif choice.upper() == "L":
        list_contacts(conn, "all")
    elif choice.upper() == "F":
        list_contacts(conn, "faves")
    elif choice.upper() == "A":
        add_contact(conn)
    elif choice.upper() == "U":
        delete_or_update(conn, "update")
    elif choice.upper() == "D":
        delete_or_update(conn, "delete")
    elif choice.upper() == "Q":
        close_connection(conn)
        print("")
        print("👋 Thanks for using BECKI'S TOTALLY AWESOME PHONEBOOK APP! Goodbye!")
        exit()
    else:
        print("")
        print("Sorry, that's not a valid menu option. Please try again.")
        print("")

# Do the thing!
if __name__ == "__main__":
    connection = create_connection()
    create_contacts_table(connection)
    create_faves_table(connection)
    while True:
        main_menu(connection)