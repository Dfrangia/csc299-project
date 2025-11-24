import os
import tempfile
import subprocess
import sys
import pytest
from tools.task_manager_cli.storage import load_tasks


@pytest.fixture
def temp_file():
    fd, path = tempfile.mkstemp(suffix='.json')
    os.close(fd)
    os.environ['TASKS_FILE'] = path
    yield path
    if os.path.exists(path):
        os.unlink(path)
    del os.environ['TASKS_FILE']


def run_cli(cmd, temp_file):
    env = os.environ.copy()
    env['TASKS_FILE'] = temp_file
    result = subprocess.run(
        [sys.executable, '-m', 'tools.task_manager_cli.cli'] + cmd.split(),
        capture_output=True,
        text=True,
        env=env
    )
    return result


def test_add_and_list_task(temp_file):
    result = run_cli('add --title "Buy milk" --description "2L"', temp_file)
    assert result.returncode == 0
    
    result = run_cli('list', temp_file)
    assert result.returncode == 0
    assert "Buy milk" in result.stdout


def test_show_task(temp_file):
    run_cli('add --title "Test Task" --description "Full description"', temp_file)
    
    result = run_cli('show 1', temp_file)
    assert result.returncode == 0
    assert "Test Task" in result.stdout
    assert "Full description" in result.stdout


def test_delete_task(temp_file):
    run_cli('add --title "Task to delete"', temp_file)
    run_cli('add --title "Keep this"', temp_file)
    
    result = run_cli('delete 1', temp_file)
    assert result.returncode == 0
    
    result = run_cli('list', temp_file)
    assert "Task to delete" not in result.stdout
    assert "Keep this" in result.stdout


def test_add_empty_title_fails(temp_file):
    result = run_cli('add --title ""', temp_file)
    assert result.returncode == 1
    assert "empty" in result.stderr.lower()


def test_show_invalid_id_fails(temp_file):
    result = run_cli('show 999', temp_file)
    assert result.returncode == 1
    assert "not found" in result.stderr.lower()

