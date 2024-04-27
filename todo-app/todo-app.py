# This is a to-do list app that uses a SQLite database to store task information.

import sqlite3
from sqlite3 import Error
from pytablewriter import UnicodeTableWriter
from pytablewriter.style import Style

# Create the database if it doesn't exist; otherwise, connect to the existing table
def create_connection():
    try:
        connection = sqlite3.connect('todo.db') 
    except Error:
        print(Error)
    return connection

# Create tasks table if it doesn't exist
# There are three columns: ID, NAME, and COMPLETED (Y/N)
def create_task_table(conn):
    try:
        cursor = conn.cursor()
        cursor.execute(""" CREATE TABLE IF NOT EXISTS tasks (
                        id INTEGER PRIMARY KEY,
                        name TEXT NOT NULL,
                        completed TEXT DEFAULT "N" NOT NULL 
                        ); """)
        conn.commit()
        cursor.close()
    except Error:
        print(Error)

# List all UNCOMPLETED tasks in table
def select_all_tasks(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks WHERE completed = 'N'")
    rows = cursor.fetchall()

    if len(rows) == 0:
        print("")
        print("🎉 No uncompleted tasks!")
    else:
        print("")
        value_matrix = [[str(row[0]), row[1]] for row in rows]

        writer = UnicodeTableWriter(
            table_name="Task Table",
            headers=["\033[1mID\033[0m", "\033[1mTASK\033[0m"],
            value_matrix=value_matrix,
            margin=1
        )
        writer.write_table()
        writer.close()

    print("")
    cursor.close()

# Create a task in table
def create_task(conn):
    new_task_name = input("Enter your task name: ")
    sql = """ INSERT INTO tasks(name)
                VALUES(?) """
    cursor = conn.cursor()
    cursor.execute(sql, (new_task_name, ))
    conn.commit()
    cursor.close()
    print("")
    print("👍 Task created!")
    print("")
    return cursor.lastrowid

# Complete a task by ID (set COMPLETED column to "Y")
def complete_task(conn):
    task_to_complete = input("To complete a task, enter its ID: ")
    sql = """ UPDATE tasks
                SET completed = "Y"
                WHERE id = ? """
    cursor = conn.cursor()

    try:
        cursor.execute(sql, (task_to_complete,))
        updated_rows = cursor.rowcount
        conn.commit()
        cursor.close()

        if updated_rows == 0:
            print("")
            print("Sorry! That ID doesn't exist. Returning to main menu.")
            print("")
        else:
            print("")
            print("✅ Task completed. Nice job! Here's a cookie: 🍪")
            print("")
            return cursor.lastrowid
    except Exception as e:
        print(f"Sorry! An error occurred: {e}")
        print("Returning to main menu.")

# Update a task name by its ID
def update_task(conn):
    task_to_update = input("To update a task name, enter its ID: ")
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT * FROM tasks WHERE id = ?", (task_to_update,))
        row = cursor.fetchone()
        # print(str(row[0]) + " | " + row[1])

        updated_task_name = input("Enter the new name for task #" + str(row[0]) + " \"" + row[1] + "\": ")
        sql = """ UPDATE tasks
                    SET name = ?
                    WHERE id = ? """
        cursor.execute(sql, (updated_task_name, task_to_update))
        conn.commit()
        cursor.close()
        print("")
        print("👍 Task updated!")
        print("")
        return cursor.lastrowid
    except Exception as e:
        print("")
        print("Sorry! That ID doesn't exist. Returning to main menu.")
        print("")

# Search all tasks by a term, or list all tasks if no input is provided
def search_tasks(conn):
    search_pattern = input("Enter search term(s), or press Enter to see all tasks: ")
    search_pattern = f"%{search_pattern}%"
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks WHERE name LIKE ?", (search_pattern,))
    rows = cursor.fetchall()
    print("")

    if len(rows) == 0:
        print("No matching tasks found.")
    else:
        value_matrix = [[str(row[0]), row[1], row[2]] for row in rows]

        for col in value_matrix:
            if col[2] == "Y":
                col[2] = "✅ YES"
            else:
                col[2] = "🚧 NO"

        writer = UnicodeTableWriter(
            table_name="Task Table",
            headers=["\033[1mID\033[0m", "\033[1mTASK\033[0m", "\033[1mDONE?\033[0m"],
            value_matrix=value_matrix,
            margin=1
        )
        writer.write_table()
        writer.close()
    cursor.close()
    print("")

# Delete a task by its ID
def delete_task(conn):
    task_to_delete = input("To delete a task, enter its ID: ")
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT * FROM tasks WHERE id = ?", (task_to_delete,))
        row = cursor.fetchone()

        print("Do you really want to delete task #" + str(row[0]) + " \"" + row[1] + "\"?")
        confirm = input("Enter Y or N: ")
        print("")
        if confirm.lower() == "y":
            cursor.execute("DELETE FROM tasks WHERE id = ?", (task_to_delete,))
            print("🗑️ Task deleted!")
            conn.commit()
        else:
            print("⚠️ Did not delete task. Returning to main menu!")
        print("")
        cursor.close()
    except:
        print("")
        print("Sorry! That ID doesn't exist. Returning to main menu.")
        print("")

# Close the DB connection
def close_connection(conn):
    if conn:
        conn.close()

# Print the main menu and loop until user chooses to exit
def main_menu(connection):
    print("============= ✨ BECKI'S TOTALLY AWESOME TO-DO LIST APP ✨ ==============")
    print("")
    print("A - ➕ ADD a new task")
    print("L - 📋 LIST uncompleted tasks")
    print("C - ✅ COMPLETE a task")
    print("U - ☝️  UPDATE a task name")
    print("D - ❌ DELETE a task")
    print("S - 🔎 SEARCH all tasks (completed and uncompleted)")
    print("X - 🚪 EXIT this application")
    print("")
    choice = input("Enter a letter to take an action: ")
    if choice.upper() == "A":
        create_task(connection)
    elif choice.upper() == "L":
        select_all_tasks(connection)
    elif choice.upper() == "C":
        complete_task(connection)
    elif choice.upper() == "U":
        update_task(connection)
    elif choice.upper() == "D":
        delete_task(connection)
    elif choice.upper() == "S":
        search_tasks(connection)
    elif choice.upper() == "X":
        close_connection(connection)
        print("")
        print("👋 Thanks for using BECKI'S TOTALLY AWESOME TO-DO LIST APP! Goodbye!")
        exit()
    else:
        print("")
        print("Sorry, that's not a valid menu option. Please try again.")
        print("")

# Do the thing!
if __name__ == '__main__':
    connection = create_connection()
    create_task_table(connection)
    while True:
        main_menu(connection)