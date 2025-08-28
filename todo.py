import json
import os

# ------------------ Task Class ------------------
class Task:
    def __init__(self, title, description, category, completed=False):
        self.title = title
        self.description = description
        self.category = category
        self.completed = completed

    def mark_completed(self):
        self.completed = True


# ------------------ File Handling ------------------
def save_tasks(tasks, filename="tasks.json"):
    with open(filename, 'w') as f:
        json.dump([task.__dict__ for task in tasks], f, indent=4)

def load_tasks(filename="tasks.json"):
    if not os.path.exists(filename):
        return []
    with open(filename, 'r') as f:
        return [Task(**data) for data in json.load(f)]


# ------------------ User Functions ------------------
def add_task(tasks):
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    category = input("Enter category (Work/Personal/Urgent): ")
    tasks.append(Task(title, description, category))
    print("✅ Task added successfully!")

def view_tasks(tasks):
    if not tasks:
        print("⚠️ No tasks found.")
        return
    for i, task in enumerate(tasks, start=1):
        status = "✔️ Completed" if task.completed else "❌ Pending"
        print(f"{i}. {task.title} ({task.category}) - {status}")
        print(f"   Description: {task.description}")

def mark_task_completed(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        task_num = int(input("Enter task number to mark as completed: "))
        tasks[task_num - 1].mark_completed()
        print("✅ Task marked as completed!")
    except (IndexError, ValueError):
        print("⚠️ Invalid input.")

def delete_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        task_num = int(input("Enter task number to delete: "))
        deleted = tasks.pop(task_num - 1)
        print(f"🗑️ Task '{deleted.title}' deleted successfully!")
    except (IndexError, ValueError):
        print("⚠️ Invalid input.")


# ------------------ Main CLI Loop ------------------
def main():
    tasks = load_tasks()

    while True:
        print("\n===== Personal To-Do List =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task Completed")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            mark_task_completed(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            save_tasks(tasks)
            print("💾 Tasks saved. Exiting...")
            break
        else:
            print("⚠️ Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
