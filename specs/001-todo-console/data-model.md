# Data Model: Todo In-Memory Console Application

**Feature**: 001-todo-console
**Date**: 2025-12-27
**Status**: Complete

## Entities

### TaskStatus (Enum)

An enumeration representing the completion status of a task.

| Value | Display String | Description |
|-------|---------------|-------------|
| INCOMPLETE | "incomplete" | Task is pending (default) |
| COMPLETE | "complete" | Task has been completed |

### Task

A single todo item with the following attributes:

| Attribute | Type | Constraints | Default | Description |
|-----------|------|-------------|---------|-------------|
| id | int | > 0, unique, sequential | Auto-assigned | Unique identifier |
| title | str | 1-200 chars, non-whitespace-only | Required | Task title |
| description | str | 0-1000 chars | "" | Optional task details |
| status | TaskStatus | INCOMPLETE or COMPLETE | INCOMPLETE | Completion status |

## Validation Rules

### Title Validation

| Rule | Error Condition | Error Message |
|------|-----------------|---------------|
| Required | Empty string or None | "Title cannot be empty" |
| Non-whitespace | Whitespace-only string | "Title cannot be empty" |
| Length | > 200 characters | Accepted (truncated in display only) |

### Description Validation

| Rule | Error Condition | Error Message |
|------|-----------------|---------------|
| Optional | None | Converted to empty string |
| Length | > 1000 characters | Accepted (truncated in display only) |

### ID Validation

| Rule | Error Condition | Error Message |
|------|-----------------|---------------|
| Exists | ID not in storage | "Task not found" |
| Type | Non-integer input | "Invalid task ID" |

## State Transitions

```text
                    toggle_status()
     ┌─────────────────────────────────────┐
     │                                     │
     ▼                                     │
┌──────────┐     toggle_status()     ┌──────────┐
│INCOMPLETE│ ◄────────────────────── │ COMPLETE │
└──────────┘                         └──────────┘
     │                                     ▲
     │                                     │
     └─────────────────────────────────────┘
                    toggle_status()
```

## Storage Structure

### In-Memory Store

```text
TaskService._tasks: dict[int, Task]
TaskService._next_id: int (starts at 1)
```

### Operations Complexity

| Operation | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| add_task | O(1) | O(1) |
| get_all_tasks | O(n) | O(n) for copy |
| get_task_by_id | O(1) | O(1) |
| update_task | O(1) | O(1) |
| delete_task | O(1) | O(1) |
| toggle_status | O(1) | O(1) |

## Relationships

This is a single-entity system. The Task entity has no relationships to other entities.

```text
┌────────────────────────────┐
│           Task             │
├────────────────────────────┤
│ • id: int (PK)             │
│ • title: str               │
│ • description: str         │
│ • status: TaskStatus       │
└────────────────────────────┘
```

## Example Data

### Valid Task

```text
Task(
    id=1,
    title="Buy groceries",
    description="Milk, eggs, bread",
    status=TaskStatus.INCOMPLETE
)
```

### Minimal Valid Task

```text
Task(
    id=2,
    title="Call mom",
    description="",
    status=TaskStatus.INCOMPLETE
)
```

### Completed Task

```text
Task(
    id=3,
    title="Submit report",
    description="Q4 financial summary",
    status=TaskStatus.COMPLETE
)
```
