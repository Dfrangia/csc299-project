import json
import os
from typing import List
from .models import Task
from .atomic import atomic_write


def get_tasks_file() -> str:
    return os.getenv("TASKS_FILE", "tasks.json")


def load_tasks() -> List[Task]:
    filepath = get_tasks_file()
    if not os.path.exists(filepath):
        return []
    
    try:
        with open(filepath, 'r') as f:
            data = json.load(f)
            return [Task.from_dict(item) for item in data]
    except (json.JSONDecodeError, KeyError):
        return []


def save_tasks(tasks: List[Task]) -> None:
    filepath = get_tasks_file()
    data = [task.to_dict() for task in tasks]
    content = json.dumps(data, indent=2)
    atomic_write(filepath, content)


def get_next_id(tasks: List[Task]) -> int:
    if not tasks:
        return 1
    return max(task.id for task in tasks) + 1

