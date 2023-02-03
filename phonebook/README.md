# Becki's Totally Awesome Phonebook

Becki's Totally Awesome Phonebook is an interactive Python script that saves contact information that you enter.

It offers the following features:

- [Add](#add-a-new-contact), [update](#update-a-contact), and [delete](#delete-a-contact) a contact
- Mark a contact as a "favorite"
- [List all contacts](#list-all-contacts) or only [favorite contacts](#list-only-favorite-contacts)
- [Search](#search-contacts-by-category) contacts by category

## Setup

1. Clone this repo:

	```
	git clone https://github.com/beckilee/python-projects.git
	```

2. Move into the `python-projects/phonebook` directory:

	```
	cd python-projects/phonebook
	```

## Usage

To run the script:

```
python phonebook.py
```

When you run the script, the application looks for a `bta_phonebook.txt` file in the current working directory and creates one if it does not exist. This is where the application will store the contact information you enter.

You'll see the following message the first time you run the script:

```
Loading bta_phonebook.txt...

NO PHONEBOOK FOUND! Creating a new one.

========================BECKI'S TOTALLY AWESOME PHONEBOOK=======================
===================================MAIN MENU====================================
Welcome to the main menu!
Each letter below corresponds to a task:

s - Search contacts by category
l - List all contacts
f - List favorite contacts
a - Add a new contact
u - Update a contact
d - Delete a contact
x - Save and exit

What would you like to do?
Enter a letter:
```

### Add a new contact

To add a new contact:

1. Enter `a` at the main menu.
2. Enter the following information:
	- First name
	- Last name
	- One or more phone numbers
	- One or more email addresses
	- `Y` to optionally mark the contact as a favorite

After you enter this information, you'll be returned to the main menu.

### List all contacts

To list all contacts, enter `l` at the main menu.

The application displays a table with the following information for each contact:

- A heart emoji, if the contact is a favorite
- Unique ID
- First name
- Last name
- Phone number(s)
- Email address(es)

For example:

```
------------------------------LIST OF ALL CONTACTS------------------------------
Favorite | Unique ID | First Name | Last Name | Phone Number(s) | Email Address(es)
--------------------------------------------------------------------------------

  1. Yusuke Kitagawa, 222-222-2222, yusuke@example.com
❤️ 2. Becki Lee, 123-456-7890, becki.lee@gmail.com
  3. Ryuji Sakamoto, 111-111-1111, ryuji@example.com
  4. Ann Takamaki, 000-000-0000, ann@example.com, ann@example2.com
```

### List only favorite contacts

To list only favorite contacts, enter `f` at the main menu.

### Update a contact

To update a contact:

1. Enter `u` at the main menu.
2. Enter one of the following values:
	- The unique ID of the contact you want to update
	- `M` to return to the main menu
	- `D` to display the list of contacts, so you can find the contact's unique ID
3. When you enter the contact's unique ID, the phonebook displays the contact's information.
4. Enter `Y` to confirm you want to proceed with the update, or enter `N` to select a different contact.
5. After confirming, enter the following information:
	- First name
	- Last name
	- Phone number(s)
	- Email address(es)

The application then returns you to the main menu.

### Search contacts by category

To search contacts by category:

1. Enter `s` at the main menu.
2. Enter the letter for the category you want to search:
	- `n` for name
	- `p` for phone
	- `e` for email
3. Enter the search query.

You'll see output like this:

```
-------------------------------SEARCH RESULTS-------------------------------
Favorite | Unique ID | First Name | Last Name | Phone Number(s) | Email Address(es)
----------------------------------------------------------------------------

Entries matching example:

  1. Yusuke Kitagawa, 222-222-2222, yusuke@example.com
  3. Ryuji Sakamoto, 111-111-1111, ryuji@example.com
  4. Ann Takamaki, 000-000-0000, ann@example.com, ann@example2.com
```

The application then returns you to the main menu.

### Delete a contact

To delete a contact:

1. Enter `d` at the main menu.
2. Enter one of the following values:
	- The unique ID of the contact you want to delete
	- `M` to return to the main menu
	- `D` to display the list of contacts, so you can find the contact's unique ID
3. When you enter the contact's unique ID, the phonebook displays the contact's information.
4. Enter `Y` to confirm you want to proceed with the deletion, or enter `N` to select a different contact.

After you confirm, the application deletes the contact and returns you to the main menu.

### Save and exit

To save and exit, enter `x`. The application saves your data to `bta_phonebook.txt` in the current working directory.

## Contact me!

If you liked this application, or if you have suggestions for improvements, drop me a line at becki.lee@gmail.com.