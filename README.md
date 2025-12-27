# Todo Console Application

A Python console-based todo application with in-memory storage, developed using Spec-Driven Development (SDD) with Spec-Kit Plus.

## Features

- **Add Task**: Create tasks with title and optional description
- **View Tasks**: Display all tasks with ID, title, description, and status
- **Update Task**: Modify task title and/or description by ID
- **Delete Task**: Remove tasks by ID
- **Mark Complete/Incomplete**: Toggle task completion status

## Requirements

- Python 3.13+
- UV package manager

## Installation

```bash
# Clone the repository
git clone https://github.com/Muhammad-Yousuf3/console_todo_python.git
cd console_todo_python

# Install dependencies
uv sync --dev
```

## Usage

```bash
# Run the application
uv run python -m src.main
```

### Menu Options

```
=== Todo Application ===

1. Add task
2. View all tasks
3. Update task
4. Delete task
5. Mark complete
6. Mark incomplete
7. Quit
```

### Example Session

```
Welcome to Todo Console Application!

=== Todo Application ===

1. Add task
...

Enter choice (1-7): 1
Enter task title: Buy groceries
Enter description (optional): Milk, eggs, bread
✓ Task created with ID 1

Enter choice (1-7): 2

ID  | Title                          | Description                      | Status
----|--------------------------------|----------------------------------|------------
1   | Buy groceries                  | Milk, eggs, bread                | incomplete

Enter choice (1-7): 5
Enter task ID: 1
✓ Task 1 marked as complete

Enter choice (1-7): 7
Goodbye!
```

## Project Structure

```
console_todo_python/
├── src/
│   ├── __init__.py
│   ├── main.py              # Application entry point
│   ├── models/
│   │   ├── __init__.py
│   │   ├── task.py          # Task dataclass & TaskStatus enum
│   │   └── exceptions.py    # Custom exceptions
│   ├── services/
│   │   ├── __init__.py
│   │   └── task_service.py  # Business logic (CRUD operations)
│   └── cli/
│       ├── __init__.py
│       ├── menu.py          # Menu display & user prompts
│       └── formatters.py    # Output formatting helpers
├── tests/
│   ├── unit/
│   │   ├── test_task.py
│   │   └── test_task_service.py
│   └── integration/
│       └── test_cli.py
├── specs/
│   └── 001-todo-console/    # Spec-Kit Plus artifacts
│       ├── spec.md          # Feature specification
│       ├── plan.md          # Implementation plan
│       ├── tasks.md         # Task breakdown
│       └── ...
└── history/
    └── prompts/             # Prompt History Records (PHRs)
```

## Running Tests

```bash
# Run all tests
uv run pytest

# Run with verbose output
uv run pytest -v

# Run with coverage
uv run pytest --cov=src
```

## Development Methodology

This project was developed using **Spec-Kit Plus** (Spec-Driven Development):

1. **Constitution** (`/sp.constitution`): Established project principles
2. **Specification** (`/sp.specify`): Defined feature requirements
3. **Planning** (`/sp.plan`): Created architecture and design decisions
4. **Task Generation** (`/sp.tasks`): Broke down into executable tasks
5. **Implementation** (`/sp.implement`): Executed tasks with TDD approach

### Core Principles

- **Spec-First Development**: All code preceded by formal specification
- **No Manual Coding**: All code generated via Claude Code
- **In-Memory Only**: No persistence beyond runtime
- **Deterministic Behavior**: Predictable, reproducible results
- **Minimal Viable Implementation**: YAGNI enforced
- **Test-Driven Validation**: Red-Green-Refactor cycle

## Architecture

```
┌─────────────────┐
│     main.py     │  Entry Point
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│   cli/menu.py   │  User Interface
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  task_service   │  Business Logic
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│   models/task   │  Data Model
└─────────────────┘
```

## License

MIT

---

Built with [Claude Code](https://claude.com/claude-code) using Spec-Kit Plus methodology.
