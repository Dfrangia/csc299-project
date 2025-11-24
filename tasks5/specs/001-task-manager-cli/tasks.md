# Tasks: Simple Python CLI Task Manager

**Branch**: `001-task-manager-cli` | **Date**: 2025-11-18

## Task Breakdown

### Phase 1: Core Data Models and Storage

- [ ] **T-001**: Create `models.py` with Task dataclass (id, title, description, created_at)
- [ ] **T-002**: Create `storage.py` with functions to load/save tasks from/to JSON file
- [ ] **T-003**: Add atomic write support in `atomic.py` to prevent corruption
- [ ] **T-004**: Write unit tests for storage operations (test_storage.py)

### Phase 2: CLI Interface

- [ ] **T-005**: Create `cli.py` with argparse-based command parser
- [ ] **T-006**: Implement `add` command with --title and optional --description
- [ ] **T-007**: Implement `list` command to display all tasks
- [ ] **T-008**: Implement `show <id>` command to display single task
- [ ] **T-009**: Implement `delete <id>` command to remove task
- [ ] **T-010**: Add error handling and non-zero exit codes for failures

### Phase 3: Testing and Validation

- [ ] **T-011**: Write end-to-end tests (test_cli_end_to_end.py)
- [ ] **T-012**: Test edge cases (empty title, invalid id, missing file)
- [ ] **T-013**: Manual testing and validation against acceptance scenarios

