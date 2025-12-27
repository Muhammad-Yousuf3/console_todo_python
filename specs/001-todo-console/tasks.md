# Tasks: Todo In-Memory Console Application

**Input**: Design documents from `/specs/001-todo-console/`
**Prerequisites**: plan.md (required), spec.md (required), data-model.md, contracts/cli-contract.md

**Tests**: Included per constitution principle VI (Test-Driven Validation).

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story?] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (US1, US2, US3, US4, US5)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- Paths follow plan.md structure

---

## Phase 1: Setup

**Purpose**: Project initialization and basic structure

- [x] T001 Create project structure with src/, tests/ directories per plan.md
- [x] T002 Initialize Python project with UV and pyproject.toml
- [x] T003 [P] Create src/__init__.py package marker
- [x] T004 [P] Create src/models/__init__.py package marker
- [x] T005 [P] Create src/services/__init__.py package marker
- [x] T006 [P] Create src/cli/__init__.py package marker
- [x] T007 [P] Create tests/__init__.py package marker
- [x] T008 [P] Create tests/unit/__init__.py package marker
- [x] T009 [P] Create tests/integration/__init__.py package marker

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**CRITICAL**: No user story work can begin until this phase is complete

- [x] T010 Create TaskStatus enum (INCOMPLETE, COMPLETE) in src/models/task.py
- [x] T011 Create Task dataclass with id, title, description, status in src/models/task.py
- [x] T012 [P] Create custom exceptions (TaskNotFoundError, ValidationError) in src/models/exceptions.py
- [x] T013 [P] Export Task, TaskStatus from src/models/__init__.py
- [x] T014 Create TaskService class with _tasks dict and _next_id counter in src/services/task_service.py
- [x] T015 [P] Export TaskService from src/services/__init__.py
- [x] T016 [P] Write unit tests for Task dataclass creation in tests/unit/test_task.py

**Checkpoint**: Foundation ready - user story implementation can now begin

---

## Phase 3: User Story 1 - Add New Task (Priority: P1)

**Goal**: Users can add tasks with title and optional description

**Independent Test**: Launch app, select "Add task", enter title/description, verify task appears in list

### Tests for User Story 1

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [x] T017 [P] [US1] Write unit test for add_task with valid title in tests/unit/test_task_service.py
- [x] T018 [P] [US1] Write unit test for add_task with title and description in tests/unit/test_task_service.py
- [x] T019 [P] [US1] Write unit test for add_task with empty title (ValidationError) in tests/unit/test_task_service.py
- [x] T020 [P] [US1] Write unit test for add_task ID assignment (sequential) in tests/unit/test_task_service.py

### Implementation for User Story 1

- [x] T021 [US1] Implement add_task(title, description) method in src/services/task_service.py
- [x] T022 [US1] Add title validation (empty/whitespace check) in src/services/task_service.py
- [x] T023 [US1] Create prompt_add_task() function in src/cli/menu.py
- [x] T024 [US1] Create display_success(message) helper in src/cli/formatters.py
- [x] T025 [US1] Create display_error(message) helper in src/cli/formatters.py

**Checkpoint**: User Story 1 should be fully functional - can add tasks

---

## Phase 4: User Story 2 - View All Tasks (Priority: P1)

**Goal**: Users can view all tasks with ID, title, description, and status

**Independent Test**: Add multiple tasks, select "View all tasks", verify all display correctly

### Tests for User Story 2

- [x] T026 [P] [US2] Write unit test for get_all_tasks with empty list in tests/unit/test_task_service.py
- [x] T027 [P] [US2] Write unit test for get_all_tasks with multiple tasks in tests/unit/test_task_service.py

### Implementation for User Story 2

- [x] T028 [US2] Implement get_all_tasks() method in src/services/task_service.py
- [x] T029 [US2] Create format_task_list(tasks) function in src/cli/formatters.py
- [x] T030 [US2] Create prompt_view_tasks() function in src/cli/menu.py
- [x] T031 [US2] Handle empty task list display ("No tasks found") in src/cli/menu.py

**Checkpoint**: User Stories 1 AND 2 should work - can add and view tasks (MVP)

---

## Phase 5: User Story 3 - Mark Task Complete/Incomplete (Priority: P2)

**Goal**: Users can toggle task status between complete and incomplete

**Independent Test**: Add task, mark complete, verify status. Mark incomplete, verify reversal.

### Tests for User Story 3

- [x] T032 [P] [US3] Write unit test for mark_complete on incomplete task in tests/unit/test_task_service.py
- [x] T033 [P] [US3] Write unit test for mark_incomplete on complete task in tests/unit/test_task_service.py
- [x] T034 [P] [US3] Write unit test for mark_complete on non-existent ID in tests/unit/test_task_service.py

### Implementation for User Story 3

- [x] T035 [US3] Implement get_task(task_id) helper method in src/services/task_service.py
- [x] T036 [US3] Implement mark_complete(task_id) method in src/services/task_service.py
- [x] T037 [US3] Implement mark_incomplete(task_id) method in src/services/task_service.py
- [x] T038 [US3] Create prompt_mark_complete() function in src/cli/menu.py
- [x] T039 [US3] Create prompt_mark_incomplete() function in src/cli/menu.py
- [x] T040 [US3] Add ID input validation (non-integer handling) in src/cli/menu.py

**Checkpoint**: User Stories 1, 2, 3 should work - can add, view, and toggle status

---

## Phase 6: User Story 4 - Update Task (Priority: P3)

**Goal**: Users can update task title and/or description by ID

**Independent Test**: Add task, update title, verify change persists in view

### Tests for User Story 4

- [x] T041 [P] [US4] Write unit test for update_task title only in tests/unit/test_task_service.py
- [x] T042 [P] [US4] Write unit test for update_task description only in tests/unit/test_task_service.py
- [x] T043 [P] [US4] Write unit test for update_task both fields in tests/unit/test_task_service.py
- [x] T044 [P] [US4] Write unit test for update_task on non-existent ID in tests/unit/test_task_service.py
- [x] T045 [P] [US4] Write unit test for update_task with empty title (ValidationError) in tests/unit/test_task_service.py

### Implementation for User Story 4

- [x] T046 [US4] Implement update_task(task_id, title, description) method in src/services/task_service.py
- [x] T047 [US4] Create prompt_update_task() function with current value display in src/cli/menu.py

**Checkpoint**: User Stories 1-4 should work - full CRUD except delete

---

## Phase 7: User Story 5 - Delete Task (Priority: P3)

**Goal**: Users can delete tasks by ID

**Independent Test**: Add task, delete by ID, verify it no longer appears in list

### Tests for User Story 5

- [x] T048 [P] [US5] Write unit test for delete_task success in tests/unit/test_task_service.py
- [x] T049 [P] [US5] Write unit test for delete_task on non-existent ID in tests/unit/test_task_service.py
- [x] T050 [P] [US5] Write unit test for delete then re-access (TaskNotFoundError) in tests/unit/test_task_service.py

### Implementation for User Story 5

- [x] T051 [US5] Implement delete_task(task_id) method in src/services/task_service.py
- [x] T052 [US5] Create prompt_delete_task() function in src/cli/menu.py

**Checkpoint**: All user stories functional - complete CRUD and status toggle

---

## Phase 8: Integration (Main Loop)

**Purpose**: Wire all components together into working application

- [x] T053 Create show_menu() function with 7 options in src/cli/menu.py
- [x] T054 Create get_user_choice() function with input validation in src/cli/menu.py
- [x] T055 Create main() function with menu loop in src/main.py
- [x] T056 Wire menu choices to TaskService operations in src/main.py
- [x] T057 Implement graceful quit (option 7) in src/main.py
- [x] T058 Add error handling wrapper for all operations in src/main.py

---

## Phase 9: Integration Tests

**Purpose**: End-to-end validation of user flows

- [x] T059 [P] Write integration test for Add → View flow in tests/integration/test_cli.py
- [x] T060 [P] Write integration test for Add → Update → View flow in tests/integration/test_cli.py
- [x] T061 [P] Write integration test for Add → Delete → View flow in tests/integration/test_cli.py
- [x] T062 [P] Write integration test for Add → Toggle → View flow in tests/integration/test_cli.py
- [x] T063 [P] Write integration test for error handling (invalid ID) in tests/integration/test_cli.py

---

## Phase 10: Polish & Cross-Cutting Concerns

**Purpose**: Final validation and cleanup

- [x] T064 Validate all acceptance scenarios from spec.md pass
- [x] T065 Run full test suite and ensure 100% pass rate
- [x] T066 Verify application responds within 1 second (SC-005)
- [x] T067 Test 100 consecutive operations without crash (SC-007)

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3-7)**: All depend on Foundational phase completion
  - US1 and US2 can run in parallel (both P1 priority)
  - US3 depends on US1 (needs add_task to test toggle)
  - US4 depends on US1 (needs add_task to test update)
  - US5 depends on US1 (needs add_task to test delete)
- **Integration (Phase 8)**: Depends on all user stories complete
- **Integration Tests (Phase 9)**: Depends on Integration phase
- **Polish (Phase 10)**: Depends on Integration Tests

### User Story Dependencies

| Story | Depends On | Can Run In Parallel With |
|-------|-----------|-------------------------|
| US1 (Add) | Foundational | US2 |
| US2 (View) | Foundational | US1 |
| US3 (Toggle) | US1 | US4, US5 |
| US4 (Update) | US1 | US3, US5 |
| US5 (Delete) | US1 | US3, US4 |

### Within Each User Story

1. Tests MUST be written and FAIL before implementation
2. Service methods before CLI handlers
3. Formatters before menu functions
4. Core functionality before error handling

### Parallel Opportunities

**Phase 1 (all parallel)**:
```
T003, T004, T005, T006, T007, T008, T009
```

**Phase 2 (partial parallel)**:
```
T012, T013 (after T010, T011)
T016 (after T011)
```

**US1 Tests (all parallel)**:
```
T017, T018, T019, T020
```

**US2 Tests (all parallel)**:
```
T026, T027
```

**Integration Tests (all parallel)**:
```
T059, T060, T061, T062, T063
```

---

## Implementation Strategy

### MVP First (User Stories 1 + 2 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational
3. Complete Phase 3: User Story 1 (Add Task)
4. Complete Phase 4: User Story 2 (View Tasks)
5. **STOP and VALIDATE**: Test add/view independently
6. Demo MVP: Users can add and view tasks

### Incremental Delivery

| Increment | Stories | Capability |
|-----------|---------|------------|
| MVP | US1 + US2 | Add and view tasks |
| +Status | US3 | Toggle complete/incomplete |
| +Update | US4 | Modify existing tasks |
| +Delete | US5 | Remove tasks |
| Complete | All | Full application |

---

## Summary

| Metric | Count |
|--------|-------|
| Total Tasks | 67 |
| Setup Tasks | 9 |
| Foundational Tasks | 7 |
| US1 Tasks | 9 |
| US2 Tasks | 4 |
| US3 Tasks | 9 |
| US4 Tasks | 7 |
| US5 Tasks | 5 |
| Integration Tasks | 6 |
| Integration Test Tasks | 5 |
| Polish Tasks | 4 |
| Parallel Opportunities | 35 |

**MVP Scope**: Phases 1-4 (US1 + US2) = 29 tasks
**Full Scope**: All phases = 67 tasks

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story is independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
