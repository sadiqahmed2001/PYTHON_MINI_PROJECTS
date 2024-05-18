import os

# File to store tasks
TASKS_FILE = 'tasks.txt'

def load_tasks():
    """Load tasks from the file."""
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, 'r') as file:
        tasks = file.readlines()
    return [task.strip() for task in tasks]

def save_tasks(tasks):
    """Save tasks to the file."""
    with open(TASKS_FILE, 'w') as file:
        for task in tasks:
            file.write(f"{task}\n")

def add_task(tasks):
    """Add a new task."""
    task = input("Enter a new task: ")
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task '{task}' added.")

def view_tasks(tasks):
    """View all tasks."""
    if not tasks:
        print("No tasks found.")
        return
    print("Your tasks:")
    for idx, task in enumerate(tasks, start=1):
        print(f"{idx}. {task}")

def delete_task(tasks):
    """Delete a task by its number."""
    view_tasks(tasks)
    try:
        task_num = int(input("Enter the task number to delete: "))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            save_tasks(tasks)
            print(f"Task '{removed_task}' deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    tasks = load_tasks()
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            delete_task(tasks)
        elif choice == '4':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == '__main__':
    main()
