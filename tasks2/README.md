# Tasks2 - Task Management & Knowledge System

An improved command-line application combining task management and personal knowledge management (PKMS) features with a chat-style interactive interface.

## Features

- Interactive chat-style terminal interface
- Task management with priorities, tags, deadlines, and completion status
- Personal knowledge management: store and manage notes/documents
- Link tasks to notes for better organization
- Search functionality for both tasks and notes

## Requirements

- Python 3.x

## Usage

### Chat-Style Interface (Recommended)

Run the application without arguments to start the interactive chat interface:

```powershell
python tasks.py
```

This will start an interactive session where you can type commands:

```
Task Management & Knowledge System - Chat Interface
Type 'help' for commands or 'exit' to quit

> add "Complete homework assignment"
Task added: Complete homework assignment

> add-note "Study Notes" "Important concepts to review..."
Note added: Study Notes

> link 1 1
Task 1 linked to note 1

> list
1. [ ] [MEDIUM] Complete homework assignment

> list-notes
1. Study Notes

> exit
Goodbye!
```

### Command-Line Interface

You can also use the application with command-line arguments:

```powershell
python tasks.py <command> [arguments]
```

### Commands

**Add a task:**
```powershell
python tasks.py add "Complete homework assignment"
```

**Add a task with priority:**
```powershell
python tasks.py add "Study for exam" --priority high
```

**Add a task with tags:**
```powershell
python tasks.py add "Finish project" --tags school,urgent
```

**Add a task with deadline:**
```powershell
python tasks.py add "Submit assignment" --deadline 2025-11-03
```

**Add a task with all options:**
```powershell
python tasks.py add "Final exam preparation" --priority high --tags school,exam --deadline 2025-11-24
```

**List all tasks:**
```powershell
python tasks.py list
```

**List only completed tasks:**
```powershell
python tasks.py list --completed
```

**List only incomplete tasks:**
```powershell
python tasks.py list --incomplete
```

**List tasks by priority:**
```powershell
python tasks.py list --priority high
```

**List tasks by tag:**
```powershell
python tasks.py list --tag school
```

**Mark task as complete:**
```powershell
python tasks.py complete 1
```

**Mark task as incomplete:**
```powershell
python tasks.py uncomplete 1
```

**Search tasks:**
```powershell
python tasks.py search "homework"
```

**Add a note:**
```powershell
python tasks.py add-note "Note Title" "Note content here" --tags study,important
```

**List all notes:**
```powershell
python tasks.py list-notes
```

**Show a note:**
```powershell
python tasks.py show-note 1
```

**Search notes:**
```powershell
python tasks.py search-notes "keyword"
```

**Link a task to a note:**
```powershell
python tasks.py link 1 1
```

## Data Storage

Tasks are stored in `tasks.json` and notes are stored in `notes.json` in the same directory as the script. These files are created automatically when you add your first task or note.

## Improvements over Tasks1

- Interactive chat-style terminal interface
- Task completion status can be toggled
- Priority levels (high, medium, low)
- Tags for categorization
- Deadlines for tasks
- Filtering options when listing tasks
- Personal knowledge management: notes/documents storage
- Linking between tasks and notes
- Search functionality for notes

