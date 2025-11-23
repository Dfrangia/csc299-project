import json
import sys
import os

DATA_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(DATA_FILE, 'w') as f:
        json.dump(tasks, f, indent=2)

def add_task(description):
    tasks = load_tasks()
    task = {
        "id": len(tasks) + 1,
        "description": description,
        "completed": False
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task added: {description}")

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return
    for task in tasks:
        status = "✓" if task["completed"] else " "
        print(f"{task['id']}. [{status}] {task['description']}")

def search_tasks(query):
    tasks = load_tasks()
    results = [task for task in tasks if query.lower() in task["description"].lower()]
    if not results:
        print(f"No tasks found matching '{query}'")
        return
    for task in results:
        status = "✓" if task["completed"] else " "
        print(f"{task['id']}. [{status}] {task['description']}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python tasks.py <command> [arguments]")
        print("Commands:")
        print("  add <description>  - Add a new task")
        print("  list              - List all tasks")
        print("  search <query>    - Search tasks by description")
        return

    command = sys.argv[1].lower()

    if command == "add":
        if len(sys.argv) < 3:
            print("Error: Please provide a task description")
            return
        description = " ".join(sys.argv[2:])
        add_task(description)
    elif command == "list":
        list_tasks()
    elif command == "search":
        if len(sys.argv) < 3:
            print("Error: Please provide a search query")
            return
        query = " ".join(sys.argv[2:])
        search_tasks(query)
    else:
        print(f"Unknown command: {command}")

if __name__ == "__main__":
    main()

