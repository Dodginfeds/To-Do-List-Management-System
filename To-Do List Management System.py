# ---------------------------------------------
# To-Do List Management System
# ---------------------------------------------
# This program allows users to:
# 1. Add tasks to their to-do list.
# 2. View all tasks currently in the list.
# 3. Remove a completed task by its name.
# 4. Clear all tasks if desired.
# 5. Quit the program when done.
# ---------------------------------------------

# List to store tasks
task_list = []

# ---------------------------------------------
# Function to Add a Task
# ---------------------------------------------

def add_task():
    """
    Adds a task to the to-do list.
    """
    try:
        task = input("Enter your task (or type 'Q' to quit): ").strip().lower()

        if task == "q":
            print("Returning to the menu...")
            return

        if task.isnumeric():
            raise ValueError("Input cannot be a number!")

        if task in task_list:
            print("This task is already in your to-do list!")
        else:
            task_list.append(task)
            print(f"Task '{task}' has been added!")

    except ValueError as e:
        print(f"Error: {e} Please enter valid text!")

# ---------------------------------------------
# Function to View Tasks
# ---------------------------------------------

def view_tasks():
    """
    Displays all tasks in the to-do list.
    """
    if not task_list:
        print("\nYou have no tasks in your to-do list!")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(task_list, start=1):
            print(f"{i}. {task}")

# ---------------------------------------------
# Function to Remove a Task
# ---------------------------------------------

def remove_task():
    """
    Removes a specific task from the list or clears all tasks.
    """
    try:
        option = input("Enter the task you want to remove (or type 'clear' to remove all tasks): ").strip().lower()

        if option == "clear":
            task_list.clear()
            print("All tasks have been removed!")
        elif option in task_list:
            task_list.remove(option)
            print(f"Task '{option}' has been removed!")
        else:
            raise ValueError(f"'{option}' is not in the list!")

    except ValueError as e:
        print(f"Error: {e}")

# ---------------------------------------------
# Function to Handle User Menu Choices
# ---------------------------------------------

def menu():
    """
    Provides an interactive menu for managing tasks.
    """
    while True:
        try:
            print("\n--- To-Do List Menu ---")
            print("1. Add a Task")
            print("2. View Tasks")
            print("3. Remove a Task")
            print("4. Quit")

            choice = int(input("Enter your choice (1-4): "))

            if choice == 1:
                add_task()
            elif choice == 2:
                view_tasks()
            elif choice == 3:
                remove_task()
            elif choice == 4:
                confirm = input("Are you sure you want to quit? (Y/N): ").strip().lower()
                if confirm == "y":
                    print("Goodbye! 👋")
                    break
                else:
                    print("Returning to the menu...")
            else:
                print("Invalid option! Please choose a number between 1 and 4.")

        except ValueError:
            print("Invalid input! Please enter a number between 1 and 4.")

# ---------------------------------------------
# Program Entry Point
# ---------------------------------------------

if __name__ == "__main__":
    menu()
