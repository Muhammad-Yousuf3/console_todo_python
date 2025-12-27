# Quickstart: Todo In-Memory Console Application

**Feature**: 001-todo-console
**Date**: 2025-12-27

## Prerequisites

- Python 3.13+
- UV package manager

## Installation

```bash
# Clone repository (if not already done)
cd Console_TODO

# Install dependencies with UV
uv sync
```

## Running the Application

```bash
# From repository root
uv run python -m src.main
```

## Usage

### Main Menu

After starting, you'll see:

```text
=== Todo Application ===

1. Add task
2. View all tasks
3. Update task
4. Delete task
5. Mark complete
6. Mark incomplete
7. Quit

Enter choice (1-7):
```

### Adding a Task

1. Select option `1`
2. Enter task title (required)
3. Enter task description (optional, press Enter to skip)

```text
Enter choice (1-7): 1
Enter task title: Buy groceries
Enter description (optional): Milk, eggs, bread
✓ Task created with ID 1
```

### Viewing Tasks

Select option `2` to see all tasks:

```text
Enter choice (1-7): 2

ID  | Title          | Description      | Status
----|----------------|------------------|----------
1   | Buy groceries  | Milk, eggs, bread| incomplete
2   | Call mom       |                  | complete
```

### Updating a Task

1. Select option `3`
2. Enter task ID
3. Enter new title (or press Enter to keep current)
4. Enter new description (or press Enter to keep current)

```text
Enter choice (1-7): 3
Enter task ID: 1
Current title: Buy groceries
Enter new title (or Enter to keep): Get groceries
Enter new description (or Enter to keep):
✓ Task 1 updated
```

### Deleting a Task

1. Select option `4`
2. Enter task ID

```text
Enter choice (1-7): 4
Enter task ID: 2
✓ Task 2 deleted
```

### Marking Task Complete/Incomplete

Select option `5` to mark complete, or `6` to mark incomplete:

```text
Enter choice (1-7): 5
Enter task ID: 1
✓ Task 1 marked as complete
```

### Quitting

Select option `7` to exit:

```text
Enter choice (1-7): 7
Goodbye!
```

## Error Handling

### Invalid Menu Choice

```text
Enter choice (1-7): 9
✗ Invalid choice. Please enter 1-7.
```

### Empty Title

```text
Enter task title:
✗ Title cannot be empty
```

### Task Not Found

```text
Enter task ID: 99
✗ Task not found
```

### Invalid ID Format

```text
Enter task ID: abc
✗ Invalid task ID
```

## Running Tests

```bash
# Run all tests
uv run pytest

# Run with coverage
uv run pytest --cov=src

# Run specific test file
uv run pytest tests/unit/test_task_service.py
```

## Project Structure

```text
Console_TODO/
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── task.py
│   ├── services/
│   │   ├── __init__.py
│   │   └── task_service.py
│   └── cli/
│       ├── __init__.py
│       ├── menu.py
│       └── formatters.py
├── tests/
│   ├── unit/
│   └── integration/
└── specs/
    └── 001-todo-console/
```

## Notes

- All data is stored in memory only
- Data is lost when the application exits
- Task IDs are sequential and never reused within a session
