# Implementation Plan: Todo In-Memory Console Application

**Branch**: `001-todo-console` | **Date**: 2025-12-27 | **Spec**: [spec.md](./spec.md)
**Input**: Feature specification from `/specs/001-todo-console/spec.md`

## Summary

Build a Python console application for managing todo tasks with in-memory storage. The application provides a text-based menu interface for CRUD operations (add, view, update, delete) and status toggling (complete/incomplete). All data exists only during runtime with no persistence.

## Technical Context

**Language/Version**: Python 3.13+
**Primary Dependencies**: None (standard library only)
**Storage**: In-memory (Python dict/list)
**Testing**: pytest
**Target Platform**: Cross-platform console (Linux, macOS, Windows)
**Project Type**: Single project
**Performance Goals**: <1 second response for all operations (per SC-005)
**Constraints**: No external dependencies, no file I/O for data, no database
**Scale/Scope**: Single-user, session-scoped, ~100 operations per session

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Principle | Status | Evidence |
|-----------|--------|----------|
| I. Spec-First Development | ✅ PASS | spec.md exists with 13 FRs, 5 user stories |
| II. No Manual Coding | ✅ PASS | All code will be generated via Claude Code |
| III. In-Memory Only | ✅ PASS | FR-009 mandates in-memory storage only |
| IV. Deterministic Behavior | ✅ PASS | Sequential IDs, predictable operations |
| V. Minimal Viable Implementation | ✅ PASS | Only specified features, no extras |
| VI. Test-Driven Validation | ✅ PASS | Tests will be written per spec acceptance criteria |

**Gate Result**: PASS - Proceeding to Phase 0

## Project Structure

### Documentation (this feature)

```text
specs/001-todo-console/
├── spec.md              # Feature specification (complete)
├── plan.md              # This file
├── research.md          # Phase 0 output
├── data-model.md        # Phase 1 output
├── quickstart.md        # Phase 1 output
└── tasks.md             # Phase 2 output (/sp.tasks command)
```

### Source Code (repository root)

```text
src/
├── __init__.py
├── main.py              # Entry point, main loop
├── models/
│   ├── __init__.py
│   └── task.py          # Task dataclass
├── services/
│   ├── __init__.py
│   └── task_service.py  # Business logic (CRUD, status toggle)
└── cli/
    ├── __init__.py
    ├── menu.py          # Menu display and input handling
    └── formatters.py    # Output formatting for task display

tests/
├── __init__.py
├── unit/
│   ├── __init__.py
│   ├── test_task.py
│   └── test_task_service.py
└── integration/
    ├── __init__.py
    └── test_cli.py
```

**Structure Decision**: Single project structure selected. This is a simple console application with no frontend/backend separation needed. The three-layer architecture (models → services → cli) provides clean separation of concerns while remaining minimal.

## Architecture Overview

```text
┌─────────────────────────────────────────────────────────┐
│                     main.py                              │
│                   (Entry Point)                          │
└─────────────────────┬───────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────┐
│                     cli/menu.py                          │
│              (Menu Display & Input)                      │
│  - show_menu()                                           │
│  - get_user_choice()                                     │
│  - prompt_for_task_details()                             │
└─────────────────────┬───────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────┐
│                 services/task_service.py                 │
│                   (Business Logic)                       │
│  - add_task(title, description) → Task                   │
│  - get_all_tasks() → List[Task]                          │
│  - update_task(id, title?, description?) → Task          │
│  - delete_task(id) → bool                                │
│  - toggle_status(id) → Task                              │
└─────────────────────┬───────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────┐
│                   models/task.py                         │
│                    (Data Model)                          │
│  @dataclass Task:                                        │
│    id: int                                               │
│    title: str                                            │
│    description: str                                      │
│    status: TaskStatus (enum)                             │
└─────────────────────────────────────────────────────────┘
```

## Key Design Decisions

### Decision 1: Task Storage Structure

| Option | Description | Pros | Cons |
|--------|-------------|------|------|
| **A. Dict[int, Task]** | Dictionary keyed by task ID | O(1) lookup by ID, simple deletion | Slightly more memory |
| B. List[Task] | Sequential list of tasks | Simple iteration | O(n) lookup by ID |

**Selected**: Option A - Dict[int, Task]
**Rationale**: Most operations (update, delete, toggle) require lookup by ID. O(1) access is optimal.

### Decision 2: ID Generation Strategy

| Option | Description | Pros | Cons |
|--------|-------------|------|------|
| **A. Monotonic Counter** | Increment counter, never reuse | Simple, predictable, per spec | Gaps after deletion |
| B. UUID | Random unique IDs | No gaps | User-unfriendly for console input |

**Selected**: Option A - Monotonic Counter
**Rationale**: Spec requires "sequential integers starting from 1, never reused within session" (Edge Cases).

### Decision 3: Status Representation

| Option | Description | Pros | Cons |
|--------|-------------|------|------|
| **A. Enum** | TaskStatus.INCOMPLETE / TaskStatus.COMPLETE | Type-safe, clear | Slight overhead |
| B. Boolean | is_complete: bool | Simple | Less readable |
| C. String | "complete" / "incomplete" | Readable | Not type-safe |

**Selected**: Option A - Enum
**Rationale**: Type safety, explicit states, aligns with constitution principle IV (deterministic behavior).

### Decision 4: Input Validation Location

| Option | Description | Pros | Cons |
|--------|-------------|------|------|
| **A. Service Layer** | Validate in task_service.py | Single point of validation | CLI must handle errors |
| B. CLI Layer | Validate in menu.py | Immediate feedback | Duplicated if service called elsewhere |
| C. Both Layers | Validate at both points | Defense in depth | Redundant code |

**Selected**: Option A - Service Layer
**Rationale**: Minimal viable implementation (constitution V). Service is the single source of truth.

### Decision 5: Error Handling Approach

| Option | Description | Pros | Cons |
|--------|-------------|------|------|
| **A. Custom Exceptions** | TaskNotFoundError, ValidationError | Clear, specific | More classes |
| B. Return Codes | Return None or error tuples | Simple | Less Pythonic |

**Selected**: Option A - Custom Exceptions
**Rationale**: Pythonic, type-safe, clear error messages per FR-010.

## Testing Strategy

### Unit Tests

| Component | Test Focus | Key Scenarios |
|-----------|-----------|---------------|
| Task model | Dataclass creation | Valid creation, default status |
| TaskService.add_task | Creation logic | Valid task, empty title rejection, ID assignment |
| TaskService.get_all_tasks | Retrieval | Empty list, multiple tasks |
| TaskService.update_task | Modification | Title update, description update, not found |
| TaskService.delete_task | Removal | Successful delete, not found |
| TaskService.toggle_status | Status change | Complete→Incomplete, Incomplete→Complete |

### Integration Tests

| Flow | Test Focus | Key Scenarios |
|------|-----------|---------------|
| Add → View | End-to-end add | Task appears in list after add |
| Add → Update → View | Modification flow | Changes persist |
| Add → Delete → View | Removal flow | Task disappears from list |
| Add → Toggle → View | Status flow | Status changes reflect in view |

### Edge Case Tests

| Scenario | Expected Behavior |
|----------|-------------------|
| Empty title | ValidationError raised |
| Whitespace-only title | ValidationError raised |
| 200-char title | Accepted |
| 201-char title | Accepted (truncated in display) |
| Non-existent task ID | TaskNotFoundError raised |
| Delete then re-delete | TaskNotFoundError on second attempt |

## Complexity Tracking

> No constitution violations requiring justification.

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| (none) | — | — |

## Implementation Phases

### Phase 1: Foundation (Setup + Models)
- Project initialization with UV
- Task dataclass with TaskStatus enum
- Custom exceptions (TaskNotFoundError, ValidationError)

### Phase 2: Core Logic (Services)
- TaskService with in-memory dict storage
- CRUD operations (add, get_all, update, delete)
- Status toggle operation
- Input validation in service layer

### Phase 3: User Interface (CLI)
- Main menu display with numbered options
- Input prompts for each operation
- Output formatting for task list
- Error message display

### Phase 4: Integration (Main Loop)
- Main entry point
- Menu loop with graceful exit
- Wire CLI → Service → Model

### Phase 5: Testing & Polish
- Unit tests for models and services
- Integration tests for CLI flows
- Edge case coverage
- Final validation against acceptance criteria
