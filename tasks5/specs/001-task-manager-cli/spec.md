# Feature Specification: Simple Python CLI Task Manager

**Feature Branch**: `001-task-manager-cli`  
**Created**: 2025-11-18  
**Status**: Draft  
**Input**: User description: "Create a simple Python CLI Task Manager. The user can add tasks, list tasks, show a single task, and delete tasks. Each task has a title and description. Data must be stored in a local JSON file."

## User Scenarios & Testing *(mandatory)*

> NOTE: This specification MUST reference the Speckit Constitution where applicable (Test-First,
> CLI/Text I/O, Observability, Versioning). Link to `.specify/memory/constitution.md` and explain
> how the feature satisfies or requests exception from any principle.

### User Story 1 - Manage tasks (Priority: P1)

As a user, I want to add, list, view, and delete tasks from my local machine so that I can
manage simple to-dos without needing external services.

**Why this priority**: Core functionality — without these operations the tool is not useful.

**Independent Test**: Executing the CLI with the appropriate commands should create/list/show/delete
tasks in the local JSON store. Tests can run against a temporary JSON file.

**Acceptance Scenarios**:

1. **Given** an empty tasks file, **When** the user runs `task add --title "Buy milk" --description "2L"`, **Then** the task is persisted and listed by `task list`.
2. **Given** multiple tasks, **When** the user runs `task list`, **Then** all tasks are shown with ids, titles, and short description snippets.
3. **Given** an existing task id, **When** the user runs `task show <id>`, **Then** the CLI outputs the full title and description for that task.
4. **Given** an existing task id, **When** the user runs `task delete <id>`, **Then** the task is removed from the store and no longer appears in `task list`.

---

### Edge Cases

- Adding a task with an empty title should be rejected with a clear error.
- Deleting or showing a non-existent id should return a non-zero exit code and an explanatory message.
- Concurrent runs that write to the JSON file should be handled safely (simple file lock or atomic replace).

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: The CLI MUST support `add` with `--title` and optional `--description` flags to create a task.
- **FR-002**: The CLI MUST support `list` to display all tasks with id, title, and a brief description snippet.
- **FR-003**: The CLI MUST support `show <id>` to display the full title and description for a single task.
- **FR-004**: The CLI MUST support `delete <id>` to remove a task by id from the JSON store.
- **FR-005**: Tasks MUST be persisted to a local JSON file (default location: `tasks.json` in current directory), and the path MUST be configurable via an environment variable or CLI flag for tests.
- **FR-006**: The tool MUST return meaningful, non-zero exit codes on errors (invalid input, missing id, IO errors).

### Key Entities

- **Task**: { id: integer, title: string, description: string, created_at: ISO-8601 timestamp }

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Users can add a task and see it listed using `task list` within one command execution (manual test).
- **SC-002**: `task show <id>` returns the exact title and description for the task id (unit testable).
- **SC-003**: `task delete <id>` removes the task so subsequent `task list` does not include it (unit testable).
- **SC-004**: Basic error handling: adding a task with empty title fails with a clear message and non-zero exit code (unit testable).

## Assumptions

- This is a single-user, local CLI — no network or multi-user server synchronization is required.
- For concurrency safety a simple advisory lock or atomic write strategy is acceptable.

