import json
import os

# File to store tasks
TASKS_FILE = "tasks.json"

def load_tasks():
    """Load tasks from file, return as a list."""
    if not os.path.exists(TASKS_FILE):
        return []
    try:
        with open(TASKS_FILE, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        print("Error reading tasks file. Starting with an empty list.")
        return []

def save_tasks(tasks):
    """Save tasks to file."""
    try:
        with open(TASKS_FILE, "w") as f:
            json.dump(tasks, f, indent=4)
    except IOError:
        print("Error saving tasks.")

def show_tasks(tasks):
    """Display all tasks."""
    if not tasks:
        print("\n✅ No tasks found.")
    else:
        print("\n📋 Your Tasks:")
        for idx, task in enumerate(tasks, start=1):
            status = "✔" if task["done"] else "❌"
            print(f"{idx}. [{status}] {task['title']}")

def add_task(tasks):
    """Add a new task."""
    title = input("Enter task title: ").strip()
    if not title:
        print("⚠ Task title cannot be empty.")
        return
    tasks.append({"title": title, "done": False})
    save_tasks(tasks)
    print("✅ Task added.")

def mark_done(tasks):
    """Mark a task as done."""
    show_tasks(tasks)
    try:
        choice = int(input("Enter task number to mark as done: "))
        if 1 <= choice <= len(tasks):
            tasks[choice - 1]["done"] = True
            save_tasks(tasks)
            print("✅ Task marked as done.")
        else:
            print("⚠ Invalid task number.")
    except ValueError:
        print("⚠ Please enter a valid number.")

def delete_task(tasks):
    """Delete a task."""
    show_tasks(tasks)
    try:
        choice = int(input("Enter task number to delete: "))
        if 1 <= choice <= len(tasks):
            removed = tasks.pop(choice - 1)
            save_tasks(tasks)
            print(f"🗑 Deleted task: {removed['title']}")
        else:
            print("⚠ Invalid task number.")
    except ValueError:
        print("⚠ Please enter a valid number.")

def main():
    tasks = load_tasks()
    while True:
        print("\n--- TO-DO LIST MENU ---")
        print("1. Show Tasks")
        print("2. Add Task")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()
        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("👋 Goodbye!")
            break
        else:
            print("⚠ Invalid choice. Please select 1-5.")

if __name__ == "__main__":
    main()
