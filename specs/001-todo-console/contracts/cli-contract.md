# CLI Contract: Todo In-Memory Console Application

**Feature**: 001-todo-console
**Date**: 2025-12-27

## Overview

This document defines the input/output contract for the console interface. Since this is a console application (not an API), contracts are defined as CLI interactions.

## Menu Contract

### Main Menu Display

**Output Format**:
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

**Valid Inputs**: `1`, `2`, `3`, `4`, `5`, `6`, `7`

**Invalid Input Response**:
```text
✗ Invalid choice. Please enter 1-7.
```

## Operation Contracts

### 1. Add Task

**Prompts**:
```text
Enter task title:
Enter description (optional):
```

**Success Response**:
```text
✓ Task created with ID {id}
```

**Error Responses**:

| Condition | Response |
|-----------|----------|
| Empty/whitespace title | `✗ Title cannot be empty` |

### 2. View All Tasks

**Empty List Response**:
```text
No tasks found.
```

**Non-Empty List Response**:
```text
ID  | Title          | Description      | Status
----|----------------|------------------|----------
{id}| {title}        | {description}    | {status}
```

**Field Formatting**:
- ID: Right-aligned, 3 chars max
- Title: Left-aligned, truncated at 30 chars with `...`
- Description: Left-aligned, truncated at 30 chars with `...`
- Status: `complete` or `incomplete`

### 3. Update Task

**Prompts**:
```text
Enter task ID:
Current title: {current_title}
Enter new title (or Enter to keep):
Current description: {current_description}
Enter new description (or Enter to keep):
```

**Success Response**:
```text
✓ Task {id} updated
```

**Error Responses**:

| Condition | Response |
|-----------|----------|
| Non-integer ID | `✗ Invalid task ID` |
| ID not found | `✗ Task not found` |
| Empty/whitespace new title | `✗ Title cannot be empty` |

### 4. Delete Task

**Prompt**:
```text
Enter task ID:
```

**Success Response**:
```text
✓ Task {id} deleted
```

**Error Responses**:

| Condition | Response |
|-----------|----------|
| Non-integer ID | `✗ Invalid task ID` |
| ID not found | `✗ Task not found` |

### 5. Mark Complete

**Prompt**:
```text
Enter task ID:
```

**Success Response**:
```text
✓ Task {id} marked as complete
```

**Error Responses**:

| Condition | Response |
|-----------|----------|
| Non-integer ID | `✗ Invalid task ID` |
| ID not found | `✗ Task not found` |

### 6. Mark Incomplete

**Prompt**:
```text
Enter task ID:
```

**Success Response**:
```text
✓ Task {id} marked as incomplete
```

**Error Responses**:

| Condition | Response |
|-----------|----------|
| Non-integer ID | `✗ Invalid task ID` |
| ID not found | `✗ Task not found` |

### 7. Quit

**Response**:
```text
Goodbye!
```

**Behavior**: Exit application with code 0

## Service Layer Contract

### TaskService Interface

```text
class TaskService:
    def add_task(title: str, description: str = "") -> Task
        Raises: ValidationError if title empty/whitespace
        Returns: Created Task with assigned ID

    def get_all_tasks() -> list[Task]
        Returns: List of all tasks (empty list if none)

    def get_task(task_id: int) -> Task
        Raises: TaskNotFoundError if ID not found
        Returns: Task with matching ID

    def update_task(task_id: int, title: str | None = None, description: str | None = None) -> Task
        Raises: TaskNotFoundError if ID not found
        Raises: ValidationError if title empty/whitespace
        Returns: Updated Task

    def delete_task(task_id: int) -> None
        Raises: TaskNotFoundError if ID not found

    def mark_complete(task_id: int) -> Task
        Raises: TaskNotFoundError if ID not found
        Returns: Task with status=COMPLETE

    def mark_incomplete(task_id: int) -> Task
        Raises: TaskNotFoundError if ID not found
        Returns: Task with status=INCOMPLETE
```

## Exception Contract

### TaskNotFoundError

**When Raised**: Any operation on non-existent task ID

**Message Format**: `Task with ID {id} not found`

### ValidationError

**When Raised**: Invalid input data

**Message Formats**:
- `Title cannot be empty`
- `Title cannot be whitespace only`
