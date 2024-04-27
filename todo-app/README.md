# Becki's Totally Awesome To-Do List App

**Becki's Totally Awesome To-Do List App** is an interactive Python script that uses a SQLite database to manage a to-do list.

It offers the following features:

- [Add](#add-a-new-task), [update](#update-a-task-name), and [delete](#delete-a-task) a task
- [List](#list-uncompleted-tasks) uncompleted tasks
- [Complete](#complete-a-task) a task
- [Search](#search-tasks) all tasks by a word or phrase

It has one dependency:

- [pytablewriter](https://pytablewriter.readthedocs.io/en/latest/pages/introduction/index.html) displays tasks in a nicely-formatted Unicode table.

## Prerequisites

Ensure you have the following tools installed:

- Python 3.9+
- pip

## Setup

1. Clone this repo:

	```
	git clone https://github.com/beckilee/python-projects.git
	```

2. Move into the `python-projects/todo-app` directory:

	```
	cd python-projects/todo-app
	```

3. Install [pytablewriter](https://pytablewriter.readthedocs.io/en/latest/pages/introduction/index.html):

    ```
    pip install pytablewriter
    ```

## Usage

### Start the application

To start the application, run the following command:

```
python todo-app.py
```

The application looks for a database named `todo.db` in the current working directory and creates one if it does not exist. This is where the application stores your tasks.

The application then displays the main menu:

```
============= ✨ BECKI'S TOTALLY AWESOME TO-DO LIST APP ✨ ==============

A - ➕ ADD a new task
L - 📋 LIST uncompleted tasks
C - ✅ COMPLETE a task
U - ☝️ UPDATE a task name
D - ❌ DELETE a task
S - 🔎 SEARCH all tasks (completed and uncompleted)
X - 🚪 EXIT this application

Enter a letter to take an action:
```

### Add a new task

To add a new task:

1. Enter `A` at the main menu.
2. Enter the name for your task (for example, `Write a to-do list app`).

### List uncompleted tasks

To list all uncompleted tasks:

1. Enter `L` at the main menu.

You'll see output like the following:

```
┌────┬────────────────────────┐
│ ID │          TASK          │
├────┼────────────────────────┤
│  1 │ Write a to-do list app │
└────┴────────────────────────┘
```

The output contains the following columns:

- `ID`: The unique ID of the task.
- `TASK`: The name of the task.

### Complete a task

To complete a task:

1. Enter `C` at the main menu.
2. Enter the ID of the task you plan to complete. You can find its ID by [listing uncompleted tasks](#list-uncompleted-tasks).

You'll see the following output:

```
✅ Task completed. Nice job! Here's a cookie: 🍪
```

### Update a task name

To update the name of a task:

1. Enter `U` at the main menu.
2. Enter the ID of the task you plan to update. You can find its ID by [listing uncompleted tasks](#list-uncompleted-tasks).
3. Enter the new name for your task (for example, `Write an AWESOME to-do list app`).

You'll see the following output:

```
👍 Task updated!
```

### Delete a task

To delete a task:

1. Enter `D` at the main menu.
2. Enter the ID of the task you plan to delete. You can find its ID by [listing uncompleted tasks](#list-uncompleted-tasks).
3. Enter `Y` to confirm deletion, or `N` to cancel.

You'll see the following output upon deletion:

```
🗑️ Task deleted!
```

### Search tasks

To search *all completed and uncompleted* tasks:

1. Enter `S` at the main menu.
2. Enter the term you want to search for, or press `Enter` to return all completed and uncompleted tasks.
   - **Note:** The application supports partial matches. For example, searching for `t` returns all tasks with the letter `t` somewhere in the name.

You'll see output like the following:

```
┌────┬────────────────────────────────────────────┬────────┐
│ ID │                    TASK                    │ DONE?  │
├────┼────────────────────────────────────────────┼────────┤
│  1 │ Write an AWESOME to-do list app            │ ✅ YES │
├────┼────────────────────────────────────────────┼────────┤
│  2 │ Add random quotes when task is completed   │ 🚧 NO  │
├────┼────────────────────────────────────────────┼────────┤
│  3 │ Go grocery shopping                        │ 🚧 NO  │
└────┴────────────────────────────────────────────┴────────┘
```

The output contains the following columns:

- `ID`: The unique ID of the task.
- `TASK`: The name of the task.
- `DONE?`: Whether the task is completed. Values:
  - `✅ YES`
  - `🚧 NO`

### Exit the application

To exit the application:

1. Enter `X` at the main menu.

You'll see the following output:

```
👋 Thanks for using BECKI'S TOTALLY AWESOME TO-DO LIST APP! Goodbye!
```

## Contact me!

If you liked this application, or if you have suggestions for improvements, drop me a line at becki.lee@gmail.com.