#!/usr/bin/env python3
import sys
import argparse
from datetime import datetime
from .storage import load_tasks, save_tasks, get_next_id
from .models import Task


def cmd_add(args):
    if not args.title or not args.title.strip():
        print("Error: Title cannot be empty", file=sys.stderr)
        sys.exit(1)
    
    tasks = load_tasks()
    new_task = Task(
        id=get_next_id(tasks),
        title=args.title.strip(),
        description=args.description.strip() if args.description else "",
        created_at=datetime.now().isoformat()
    )
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Task {new_task.id} added: {new_task.title}")


def cmd_list(args):
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return
    
    for task in tasks:
        desc_snippet = task.description[:50] + "..." if len(task.description) > 50 else task.description
        print(f"{task.id}. {task.title}")
        if desc_snippet:
            print(f"   {desc_snippet}")


def cmd_show(args):
    tasks = load_tasks()
    task_id = args.id
    
    task = next((t for t in tasks if t.id == task_id), None)
    if not task:
        print(f"Error: Task {task_id} not found", file=sys.stderr)
        sys.exit(1)
    
    print(f"Task {task.id}: {task.title}")
    if task.description:
        print(f"Description: {task.description}")
    print(f"Created: {task.created_at}")


def cmd_delete(args):
    tasks = load_tasks()
    task_id = args.id
    
    original_count = len(tasks)
    tasks = [t for t in tasks if t.id != task_id]
    
    if len(tasks) == original_count:
        print(f"Error: Task {task_id} not found", file=sys.stderr)
        sys.exit(1)
    
    save_tasks(tasks)
    print(f"Task {task_id} deleted")


def main():
    parser = argparse.ArgumentParser(description="Simple CLI Task Manager")
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    add_parser = subparsers.add_parser('add', help='Add a new task')
    add_parser.add_argument('--title', required=True, help='Task title')
    add_parser.add_argument('--description', help='Task description')
    add_parser.set_defaults(func=cmd_add)
    
    list_parser = subparsers.add_parser('list', help='List all tasks')
    list_parser.set_defaults(func=cmd_list)
    
    show_parser = subparsers.add_parser('show', help='Show a single task')
    show_parser.add_argument('id', type=int, help='Task ID')
    show_parser.set_defaults(func=cmd_show)
    
    delete_parser = subparsers.add_parser('delete', help='Delete a task')
    delete_parser.add_argument('id', type=int, help='Task ID')
    delete_parser.set_defaults(func=cmd_delete)
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        sys.exit(1)
    
    args.func(args)


if __name__ == '__main__':
    main()

