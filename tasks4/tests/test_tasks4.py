import pytest
from unittest.mock import Mock, patch
from tasks4 import summarize_task, main

def test_summarize_task():
    mock_client = Mock()
    mock_response = Mock()
    mock_response.choices = [Mock()]
    mock_response.choices[0].message.content = "Test summary"
    mock_client.chat.completions.create.return_value = mock_response
    
    result = summarize_task("Test task description", mock_client)
    
    assert result == "Test summary"
    mock_client.chat.completions.create.assert_called_once()
    call_args = mock_client.chat.completions.create.call_args
    assert call_args[1]["model"] == "gpt-4o-mini"
    assert "Summarize this task description" in call_args[1]["messages"][1]["content"]

def test_summarize_task_empty_response():
    mock_client = Mock()
    mock_response = Mock()
    mock_response.choices = [Mock()]
    mock_response.choices[0].message.content = None
    mock_client.chat.completions.create.return_value = mock_response
    
    result = summarize_task("Test task description", mock_client)
    
    assert result == "Summary unavailable"

@patch('tasks4.OpenAI')
@patch('tasks4.os.getenv')
def test_main_with_api_key(mock_getenv, mock_openai):
    mock_getenv.return_value = "test-api-key"
    mock_client = Mock()
    mock_openai.return_value = mock_client
    
    mock_response = Mock()
    mock_response.choices = [Mock()]
    mock_response.choices[0].message.content = "Test summary"
    mock_client.chat.completions.create.return_value = mock_response
    
    main()
    
    assert mock_openai.called
    assert mock_client.chat.completions.create.call_count == 2

@patch('tasks4.os.getenv')
def test_main_no_api_key(mock_getenv, capsys):
    mock_getenv.return_value = None
    
    main()
    
    captured = capsys.readouterr()
    assert "OPENAI_API_KEY" in captured.out
    assert "Error" in captured.out

