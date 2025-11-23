import pytest
from typer.testing import CliRunner
from tasks3 import app

runner = CliRunner()

def test_chat_exit():
    inputs = "help\nexit\n"
    result = runner.invoke(app, ["chat"], input=inputs)
    assert result.exit_code == 0
    assert "Task Commands:" in result.output
    assert "Goodbye!" in result.output

def test_chat_quit():
    inputs = "list\nquit\n"
    result = runner.invoke(app, ["chat"], input=inputs)
    assert result.exit_code == 0
    assert "Goodbye!" in result.output

def test_chat_add_task():
    inputs = 'add "Test task from chat"\nlist\nexit\n'
    result = runner.invoke(app, ["chat"], input=inputs)
    assert result.exit_code == 0
    assert "Task added: Test task from chat" in result.output
    assert "Test task from chat" in result.output

