# Research: Todo In-Memory Console Application

**Feature**: 001-todo-console
**Date**: 2025-12-27
**Status**: Complete

## Research Summary

This document captures research decisions made during planning. Since the project uses only Python standard library with in-memory storage, no external technology research was required.

## Decisions

### 1. Data Structure for Task Storage

**Decision**: Use `dict[int, Task]` for task storage

**Rationale**:
- O(1) lookup by task ID (required for update, delete, toggle operations)
- O(1) deletion without shifting elements
- Simple iteration via `.values()` for view all
- Memory overhead is negligible for expected scale (~100 tasks)

**Alternatives Considered**:
- `list[Task]`: Rejected due to O(n) lookup by ID
- `OrderedDict`: Unnecessary since insertion order is preserved in dict (Python 3.7+)

### 2. ID Generation

**Decision**: Monotonic counter stored in TaskService, never reused

**Rationale**:
- Spec explicitly requires "Sequential integers starting from 1, never reused within session"
- Simple to implement with a class attribute `_next_id`
- Predictable for users entering IDs at console

**Alternatives Considered**:
- UUID: Rejected - user-unfriendly for console input
- Reuse deleted IDs: Rejected - violates spec requirement

### 3. Status Representation

**Decision**: Use Python `Enum` for TaskStatus

**Rationale**:
- Type-safe: prevents invalid status values
- IDE support for autocomplete
- Clear string representation for display
- Aligns with deterministic behavior principle (constitution IV)

**Alternatives Considered**:
- Boolean `is_complete`: Less readable in output
- String literals: No type safety

### 4. Error Handling

**Decision**: Custom exception classes

**Rationale**:
- `TaskNotFoundError`: Raised when task ID doesn't exist
- `ValidationError`: Raised for invalid input (empty title, etc.)
- Pythonic pattern for error signaling
- CLI can catch and display user-friendly messages

**Alternatives Considered**:
- Return None/sentinel: Less explicit, requires checking at every call site
- Error codes: Not idiomatic Python

### 5. Input Validation Strategy

**Decision**: Validate in service layer only

**Rationale**:
- Single source of truth for validation rules
- CLI handles exceptions and displays messages
- No duplication between layers
- Follows minimal viable implementation (constitution V)

**Alternatives Considered**:
- CLI-only validation: Would need duplication if service called programmatically
- Both layers: Redundant, violates YAGNI

## Technology Stack Confirmation

| Component | Choice | Reason |
|-----------|--------|--------|
| Language | Python 3.13+ | Per constitution |
| Package Manager | UV | Per constitution |
| Testing | pytest | Standard Python testing framework |
| Dependencies | None | Standard library only per constraints |
| Storage | In-memory dict | Per constitution principle III |

## Outstanding Items

None. All research questions resolved.
