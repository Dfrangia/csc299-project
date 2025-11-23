import json
import os
import tempfile
import pytest
import tasks3

@pytest.fixture
def temp_data_dir(monkeypatch):
    with tempfile.TemporaryDirectory() as tmpdir:
        original_dir = os.getcwd()
        os.chdir(tmpdir)
        tasks_file = os.path.join(tmpdir, "tasks.json")
        notes_file = os.path.join(tmpdir, "notes.json")
        monkeypatch.setattr(tasks3, "DATA_FILE", "tasks.json")
        monkeypatch.setattr(tasks3, "NOTES_FILE", "notes.json")
        yield tmpdir
        os.chdir(original_dir)

def test_add_task(temp_data_dir):
    tasks3.add_task("Test task", "high", ["test"], "2025-12-01")
    tasks = tasks3.load_tasks()
    assert len(tasks) == 1
    assert tasks[0]["description"] == "Test task"
    assert tasks[0]["priority"] == "high"
    assert tasks[0]["tags"] == ["test"]
    assert tasks[0]["deadline"] == "2025-12-01"
    assert tasks[0]["completed"] == False

def test_complete_task(temp_data_dir):
    tasks3.add_task("Test task")
    tasks = tasks3.load_tasks()
    assert tasks[0]["completed"] == False
    
    tasks3.complete_task(1)
    tasks = tasks3.load_tasks()
    assert tasks[0]["completed"] == True

def test_add_note(temp_data_dir):
    tasks3.add_note("Test Note", "This is test content", ["test"])
    notes = tasks3.load_notes()
    assert len(notes) == 1
    assert notes[0]["title"] == "Test Note"
    assert notes[0]["content"] == "This is test content"
    assert notes[0]["tags"] == ["test"]

