import os
import json
from datetime import datetime

DATA_FILE = "tasks.json"

# ---------------- File Handling ----------------
def load_tasks():
    """Load tasks from JSON file."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    """Save tasks to JSON file."""
    with open(DATA_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

# ---------------- Task Operations ----------------
def add_task(tasks):
    title = input("Enter task title: ")
    deadline = input("Enter deadline (YYYY-MM-DD) or leave blank: ")

    task = {
        "title": title,
        "deadline": deadline if deadline else None,
        "done": False,
        "created": datetime.now().strftime("%Y-%m-%d %H:%M")
    }
    tasks.append(task)
    save_tasks(tasks)
    print("✅ Task added!")

def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return
    print("\nYour Tasks:")
    for i, task in enumerate(tasks, 1):
        status = "✔" if task["done"] else "✗"
        deadline = f"(Deadline: {task['deadline']})" if task['deadline'] else ""
        print(f"{i}. {status} {task['title']} {deadline} | Added: {task['created']}")
    print()

def mark_done(tasks):
    view_tasks(tasks)
    try:
        choice = int(input("Enter task number to mark as done: ")) - 1
        if 0 <= choice < len(tasks):
            tasks[choice]["done"] = True
            save_tasks(tasks)
            print("🎉 Task marked as done!")
        else:
            print("❌ Invalid choice.")
    except ValueError:
        print("⚠ Please enter a number.")

def delete_task(tasks):
    view_tasks(tasks)
    try:
        choice = int(input("Enter task number to delete: ")) - 1
        if 0 <= choice < len(tasks):
            removed = tasks.pop(choice)
            save_tasks(tasks)
            print(f"🗑 Deleted: {removed['title']}")
        else:
            print("❌ Invalid choice.")
    except ValueError:
        print("⚠ Please enter a number.")

# ---------------- Main Menu ----------------
def main():
    tasks = load_tasks()
    while True:
        print("\n===== To-Do List Manager =====")
        print("1. View tasks")
        print("2. Add task")
        print("3. Mark task as done")
        print("4. Delete task")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            view_tasks(tasks)
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
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
