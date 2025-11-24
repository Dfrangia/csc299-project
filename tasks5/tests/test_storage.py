import os
import tempfile
import pytest
from tools.task_manager_cli.storage import load_tasks, save_tasks, get_next_id
from tools.task_manager_cli.models import Task
from datetime import datetime


@pytest.fixture
def temp_file():
    fd, path = tempfile.mkstemp(suffix='.json')
    os.close(fd)
    os.environ['TASKS_FILE'] = path
    yield path
    if os.path.exists(path):
        os.unlink(path)
    del os.environ['TASKS_FILE']


def test_load_tasks_empty_file(temp_file):
    tasks = load_tasks()
    assert tasks == []


def test_save_and_load_tasks(temp_file):
    task1 = Task(1, "Test Task", "Description", datetime.now().isoformat())
    task2 = Task(2, "Another Task", "", datetime.now().isoformat())
    
    save_tasks([task1, task2])
    loaded = load_tasks()
    
    assert len(loaded) == 2
    assert loaded[0].title == "Test Task"
    assert loaded[1].title == "Another Task"


def test_get_next_id():
    tasks = []
    assert get_next_id(tasks) == 1
    
    task1 = Task(1, "Task 1", "", datetime.now().isoformat())
    task2 = Task(5, "Task 5", "", datetime.now().isoformat())
    assert get_next_id([task1, task2]) == 6

