# todo_manager.py

import os

# File to save the tasks
TODO_FILE = "tasks.txt"

# Function to load tasks from the file
def load_tasks():
    tasks = []
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as file:
            for line in file:
                task, status = line.strip().split(" | ")
                tasks.append({"task": task, "status": status})
    return tasks

# Function to save tasks to the file
def save_tasks(tasks):
    with open(TODO_FILE, "w") as file:
        for task in tasks:
            file.write(f"{task['task']} | {task['status']}\n")

# Function to add a task
def add_task(task_description):
    tasks = load_tasks()
    tasks.append({"task": task_description, "status": "Incomplete"})
    save_tasks(tasks)
    print(f"Task '{task_description}' added.")

# Function to view tasks
def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found!")
        return
    print("\nYour To-Do List:")
    for idx, task in enumerate(tasks, start=1):
        status = "✓" if task["status"] == "Complete" else "✗"
        print(f"{idx}. {task['task']} [{status}]")

# Function to mark a task as completed
def complete_task(task_number):
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        tasks[task_number - 1]["status"] = "Complete"
        save_tasks(tasks)
        print(f"Task '{tasks[task_number - 1]['task']}' marked as completed.")
    else:
        print("Invalid task number!")

# Function to delete a task
def delete_task(task_number):
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        save_tasks(tasks)
        print(f"Task '{removed_task['task']}' deleted.")
    else:
        print("Invalid task number!")

# Main function to display the menu and take user input
def main():
    while True:
        print("\n--- To-Do List Manager ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Choose an option (1-5): ")

        if choice == "1":
            task_description = input("Enter the task description: ")
            add_task(task_description)
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            try:
                task_number = int(input("Enter the task number to mark as completed: "))
                complete_task(task_number)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "4":
            try:
                task_number = int(input("Enter the task number to delete: "))
                delete_task(task_number)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "5":
            print("Exiting To-Do List Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please select from 1 to 5.")

if __name__ == "__main__":
    main()

