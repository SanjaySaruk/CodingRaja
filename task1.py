import json
import os
from datetime import datetime

# File to store task data
DATA_FILE = "todo_data.json"

# Function to load task data from file
def load_data():
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Function to save task data to file
def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

# Function to add a task
def add_task(tasks):
    task_name = input("Enter task name: ")
    priority = input("Enter priority (high, medium, low): ").lower()
    due_date_str = input("Enter due date (YYYY-MM-DD): ")
    try:
        due_date = datetime.strptime(due_date_str, "%Y-%m-%d").date()
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return

    tasks.append({"name": task_name, "priority": priority, "due_date": due_date, "completed": False})
    print("Task added successfully.")
    save_data(tasks)

# Function to remove a task
def remove_task(tasks):
    print_tasks(tasks)
    try:
        index = int(input("Enter the index of the task to remove: "))
        if 1 <= index <= len(tasks):
            del tasks[index - 1]
            print("Task removed successfully.")
            save_data(tasks)
        else:
            print("Invalid index. Please enter a valid index.")
    except ValueError:
        print("Invalid input. Please enter a number.")

# Function to mark a task as completed
def complete_task(tasks):
    print_tasks(tasks)
    try:
        index = int(input("Enter the index of the task to mark as completed: "))
        if 1 <= index <= len(tasks):
            tasks[index - 1]["completed"] = True
            print("Task marked as completed.")
            save_data(tasks)
        else:
            print("Invalid index. Please enter a valid index.")
    except ValueError:
        print("Invalid input. Please enter a number.")

# Function to print tasks
def print_tasks(tasks):
    if not tasks:
        print("No tasks.")
    else:
        print("Tasks:")
        for i, task in enumerate(tasks, start=1):
            status = "[X]" if task["completed"] else "[ ]"
            print(f"{i}. {status} {task['name']} - Priority: {task['priority']}, Due Date: {task['due_date']}")

# Main function
def main():
    tasks = load_data()

    while True:
        print("\n===== To-Do List =====")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Mark Task as Completed")
        print("4. View Tasks")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            remove_task(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            print_tasks(tasks)
        elif choice == "5":
            print("Thank you for using the To-Do List. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()
