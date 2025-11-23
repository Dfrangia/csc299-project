import json
import sys
import os
import shlex
from datetime import datetime
import typer

def inc(n: int) -> int:
    return n + 1

DATA_FILE = "tasks.json"
NOTES_FILE = "notes.json"

def load_tasks():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(DATA_FILE, 'w') as f:
        json.dump(tasks, f, indent=2)

def add_task(description, priority="medium", tags=None, deadline=None):
    tasks = load_tasks()
    task = {
        "id": len(tasks) + 1,
        "description": description,
        "completed": False,
        "priority": priority,
        "tags": tags if tags else [],
        "deadline": deadline
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task added: {description}")

def complete_task(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            save_tasks(tasks)
            print(f"Task {task_id} marked as complete")
            return
    print(f"Task {task_id} not found")

def uncomplete_task(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = False
            save_tasks(tasks)
            print(f"Task {task_id} marked as incomplete")
            return
    print(f"Task {task_id} not found")

def list_tasks(filter_completed=None, filter_priority=None, filter_tag=None):
    tasks = load_tasks()
    
    if filter_completed is not None:
        tasks = [t for t in tasks if t["completed"] == filter_completed]
    
    if filter_priority:
        tasks = [t for t in tasks if t.get("priority") == filter_priority]
    
    if filter_tag:
        tasks = [t for t in tasks if filter_tag in t.get("tags", [])]
    
    if not tasks:
        print("No tasks found.")
        return
    
    for task in tasks:
        status = "✓" if task["completed"] else " "
        priority = task.get("priority", "medium").upper()
        tags = ", ".join(task.get("tags", [])) if task.get("tags") else ""
        deadline = f" (due: {task['deadline']})" if task.get("deadline") else ""
        tag_str = f" [{tags}]" if tags else ""
        print(f"{task['id']}. [{status}] [{priority}] {task['description']}{tag_str}{deadline}")

def search_tasks(query):
    tasks = load_tasks()
    results = [task for task in tasks if query.lower() in task["description"].lower()]
    if not results:
        print(f"No tasks found matching '{query}'")
        return
    for task in results:
        status = "✓" if task["completed"] else " "
        priority = task.get("priority", "medium").upper()
        tags = ", ".join(task.get("tags", [])) if task.get("tags") else ""
        deadline = f" (due: {task['deadline']})" if task.get("deadline") else ""
        tag_str = f" [{tags}]" if tags else ""
        print(f"{task['id']}. [{status}] [{priority}] {task['description']}{tag_str}{deadline}")

def load_notes():
    if os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, 'r') as f:
            return json.load(f)
    return []

def save_notes(notes):
    with open(NOTES_FILE, 'w') as f:
        json.dump(notes, f, indent=2)

def add_note(title, content, tags=None):
    notes = load_notes()
    note = {
        "id": len(notes) + 1,
        "title": title,
        "content": content,
        "tags": tags if tags else [],
        "linked_tasks": []
    }
    notes.append(note)
    save_notes(notes)
    print(f"Note added: {title}")

def list_notes(filter_tag=None):
    notes = load_notes()
    
    if filter_tag:
        notes = [n for n in notes if filter_tag in n.get("tags", [])]
    
    if not notes:
        print("No notes found.")
        return
    
    for note in notes:
        tags = ", ".join(note.get("tags", [])) if note.get("tags") else ""
        linked = f" (linked to tasks: {', '.join(map(str, note.get('linked_tasks', [])))})" if note.get("linked_tasks") else ""
        tag_str = f" [{tags}]" if tags else ""
        print(f"{note['id']}. {note['title']}{tag_str}{linked}")

def show_note(note_id):
    notes = load_notes()
    for note in notes:
        if note["id"] == note_id:
            print(f"\nNote {note_id}: {note['title']}")
            print("-" * 50)
            print(note["content"])
            tags = ", ".join(note.get("tags", [])) if note.get("tags") else ""
            if tags:
                print(f"\nTags: {tags}")
            linked = note.get("linked_tasks", [])
            if linked:
                print(f"Linked tasks: {', '.join(map(str, linked))}")
            return
    print(f"Note {note_id} not found")

def search_notes(query):
    notes = load_notes()
    results = [note for note in notes if query.lower() in note["title"].lower() or query.lower() in note["content"].lower()]
    if not results:
        print(f"No notes found matching '{query}'")
        return
    for note in results:
        tags = ", ".join(note.get("tags", [])) if note.get("tags") else ""
        tag_str = f" [{tags}]" if tags else ""
        print(f"{note['id']}. {note['title']}{tag_str}")

def link_task_note(task_id, note_id):
    tasks = load_tasks()
    notes = load_notes()
    
    task_found = False
    note_found = False
    
    for task in tasks:
        if task["id"] == task_id:
            task_found = True
            if "linked_notes" not in task:
                task["linked_notes"] = []
            if note_id not in task["linked_notes"]:
                task["linked_notes"].append(note_id)
            break
    
    for note in notes:
        if note["id"] == note_id:
            note_found = True
            if note_id not in note.get("linked_tasks", []):
                if "linked_tasks" not in note:
                    note["linked_tasks"] = []
                note["linked_tasks"].append(task_id)
            break
    
    if not task_found:
        print(f"Task {task_id} not found")
        return
    if not note_found:
        print(f"Note {note_id} not found")
        return
    
    save_tasks(tasks)
    save_notes(notes)
    print(f"Task {task_id} linked to note {note_id}")

def execute_command(command, args_list):
    command = command.lower()
    
    if command == "add":
        description = ""
        priority = "medium"
        tags = []
        deadline = None
        
        i = 0
        while i < len(args_list):
            if args_list[i] == "--priority" and i + 1 < len(args_list):
                priority = args_list[i + 1].lower()
                i += 2
            elif args_list[i] == "--tags" and i + 1 < len(args_list):
                tags = [tag.strip() for tag in args_list[i + 1].split(",")]
                i += 2
            elif args_list[i] == "--deadline" and i + 1 < len(args_list):
                deadline = args_list[i + 1]
                i += 2
            else:
                if description:
                    description += " "
                description += args_list[i]
                i += 1
        
        if not description:
            print("Error: Please provide a task description")
            return
        add_task(description, priority, tags, deadline)
    
    elif command == "list":
        filter_completed = None
        filter_priority = None
        filter_tag = None
        
        i = 0
        while i < len(args_list):
            if args_list[i] == "--completed":
                filter_completed = True
                i += 1
            elif args_list[i] == "--incomplete":
                filter_completed = False
                i += 1
            elif args_list[i] == "--priority" and i + 1 < len(args_list):
                filter_priority = args_list[i + 1].lower()
                i += 2
            elif args_list[i] == "--tag" and i + 1 < len(args_list):
                filter_tag = args_list[i + 1]
                i += 2
            else:
                i += 1
        
        list_tasks(filter_completed, filter_priority, filter_tag)
    
    elif command == "complete":
        if not args_list:
            print("Error: Please provide a task ID")
            return
        try:
            task_id = int(args_list[0])
            complete_task(task_id)
        except ValueError:
            print("Error: Task ID must be a number")
    
    elif command == "uncomplete":
        if not args_list:
            print("Error: Please provide a task ID")
            return
        try:
            task_id = int(args_list[0])
            uncomplete_task(task_id)
        except ValueError:
            print("Error: Task ID must be a number")
    
    elif command == "search":
        if not args_list:
            print("Error: Please provide a search query")
            return
        query = " ".join(args_list)
        search_tasks(query)
    
    elif command == "add-note":
        if len(args_list) < 2:
            print("Error: Please provide a note title and content")
            print("Usage: add-note \"<title>\" \"<content>\" [--tags tag1,tag2]")
            return
        
        title = args_list[0].strip('"\'')
        content = args_list[1].strip('"\'')
        tags = []
        
        i = 2
        while i < len(args_list):
            if args_list[i] == "--tags" and i + 1 < len(args_list):
                tags = [tag.strip() for tag in args_list[i + 1].split(",")]
                i += 2
            else:
                i += 1
        
        add_note(title, content, tags)
    
    elif command == "list-notes":
        filter_tag = None
        
        i = 0
        while i < len(args_list):
            if args_list[i] == "--tag" and i + 1 < len(args_list):
                filter_tag = args_list[i + 1]
                i += 2
            else:
                i += 1
        
        list_notes(filter_tag)
    
    elif command == "show-note":
        if not args_list:
            print("Error: Please provide a note ID")
            return
        try:
            note_id = int(args_list[0])
            show_note(note_id)
        except ValueError:
            print("Error: Note ID must be a number")
    
    elif command == "search-notes":
        if not args_list:
            print("Error: Please provide a search query")
            return
        query = " ".join(args_list)
        search_notes(query)
    
    elif command == "link":
        if len(args_list) < 2:
            print("Error: Please provide task ID and note ID")
            print("Usage: link <task_id> <note_id>")
            return
        try:
            task_id = int(args_list[0])
            note_id = int(args_list[1])
            link_task_note(task_id, note_id)
        except ValueError:
            print("Error: Task ID and Note ID must be numbers")
    
    elif command in ["exit", "quit", "q"]:
        return "exit"
    
    elif command == "help":
        print("Task Commands:")
        print("  add \"<description>\"              - Add a new task (use quotes for multi-word descriptions)")
        print("  add \"<description>\" --priority high  - Add task with priority (high/medium/low)")
        print("  add \"<description>\" --tags tag1,tag2 - Add task with tags")
        print("  list                            - List all tasks")
        print("  list --completed                - List completed tasks")
        print("  list --priority high            - List tasks by priority")
        print("  complete <id>                   - Mark task as complete")
        print("  uncomplete <id>                 - Mark task as incomplete")
        print("  search \"<query>\"                  - Search tasks (use quotes for multi-word)")
        print()
        print("Note Commands:")
        print("  add-note \"<title>\" \"<content>\"  - Add a new note (use quotes)")
        print("  list-notes                      - List all notes")
        print("  show-note <id>                  - Show note content")
        print("  search-notes \"<query>\"            - Search notes (use quotes for multi-word)")
        print("  link <task_id> <note_id>        - Link task to note")
        print()
        print("Other:")
        print("  help                            - Show this help")
        print("  exit/quit/q                     - Exit program")
    
    else:
        print(f"Unknown command: {command}. Type 'help' for available commands.")

def chat_loop():
    print("Task Management & Knowledge System - Chat Interface")
    print("Type 'help' for commands or 'exit' to quit")
    print()
    
    while True:
        try:
            user_input = input("> ").strip()
            if not user_input:
                continue
            
            parts = shlex.split(user_input)
            if not parts:
                continue
            
            command = parts[0]
            args = parts[1:] if len(parts) > 1 else []
            
            result = execute_command(command, args)
            if result == "exit":
                print("Goodbye!")
                break
            print()
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except EOFError:
            print("\nGoodbye!")
            break

app = typer.Typer()

@app.command()
def chat():
    chat_loop()

@app.command()
def add(
    description: str = typer.Argument(...),
    priority: str = typer.Option("medium", "--priority", "-p"),
    tags: str = typer.Option(None, "--tags", "-t"),
    deadline: str = typer.Option(None, "--deadline", "-d")
):
    tag_list = [tag.strip() for tag in tags.split(",")] if tags else None
    add_task(description, priority, tag_list, deadline)

@app.command(name="list")
def list_cmd(
    completed: bool = typer.Option(None, "--completed"),
    incomplete: bool = typer.Option(None, "--incomplete"),
    priority: str = typer.Option(None, "--priority", "-p"),
    tag: str = typer.Option(None, "--tag")
):
    filter_completed = None
    if completed:
        filter_completed = True
    elif incomplete:
        filter_completed = False
    list_tasks(filter_completed, priority, tag)

@app.command()
def complete(task_id: int = typer.Argument(...)):
    complete_task(task_id)

@app.command()
def uncomplete(task_id: int = typer.Argument(...)):
    uncomplete_task(task_id)

@app.command()
def search(query: str = typer.Argument(...)):
    search_tasks(query)

@app.command(name="add-note")
def add_note_cmd(
    title: str = typer.Argument(...),
    content: str = typer.Argument(...),
    tags: str = typer.Option(None, "--tags", "-t")
):
    tag_list = [tag.strip() for tag in tags.split(",")] if tags else None
    add_note(title, content, tag_list)

@app.command(name="list-notes")
def list_notes_cmd(tag: str = typer.Option(None, "--tag")):
    list_notes(tag)

@app.command(name="show-note")
def show_note_cmd(note_id: int = typer.Argument(...)):
    show_note(note_id)

@app.command(name="search-notes")
def search_notes_cmd(query: str = typer.Argument(...)):
    search_notes(query)

@app.command()
def link(task_id: int = typer.Argument(...), note_id: int = typer.Argument(...)):
    link_task_note(task_id, note_id)

def main() -> None:
    if len(sys.argv) < 2:
        chat_loop()
    else:
        app()
