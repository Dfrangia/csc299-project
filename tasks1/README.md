# Tasks1 - Task Management Prototype

A simple command-line application for managing tasks stored in a JSON file.

## Features

- Add new tasks
- List all tasks
- Search tasks by description

## Requirements

- Python 3.x

## Usage

Run the application using Python:

```powershell
python tasks.py <command> [arguments]
```

### Commands

**Add a task:**
```powershell
python tasks.py add "Complete homework assignment"
```

**List all tasks:**
```powershell
python tasks.py list
```

**Search tasks:**
```powershell
python tasks.py search "homework"
```

## Data Storage

Tasks are stored in `tasks.json` in the same directory as the script. The JSON file is created automatically when you add your first task.

## Example

```powershell
python tasks.py add "Study for exam"
python tasks.py add "Finish project"
python tasks.py list
python tasks.py search "exam"
```

