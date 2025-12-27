"""Unit tests for TaskService."""

import pytest

from src.models import Task, TaskNotFoundError, TaskStatus, ValidationError
from src.services import TaskService


class TestAddTask:
    """Test cases for TaskService.add_task method."""

    def test_add_task_with_valid_title(self) -> None:
        """Test adding a task with valid title only."""
        service = TaskService()

        task = service.add_task("Buy groceries")

        assert task.id == 1
        assert task.title == "Buy groceries"
        assert task.description == ""
        assert task.status == TaskStatus.INCOMPLETE

    def test_add_task_with_title_and_description(self) -> None:
        """Test adding a task with both title and description."""
        service = TaskService()

        task = service.add_task("Call mom", "Wish happy birthday")

        assert task.id == 1
        assert task.title == "Call mom"
        assert task.description == "Wish happy birthday"
        assert task.status == TaskStatus.INCOMPLETE

    def test_add_task_with_empty_title_raises_validation_error(self) -> None:
        """Test that empty title raises ValidationError."""
        service = TaskService()

        with pytest.raises(ValidationError) as exc_info:
            service.add_task("")

        assert "Title cannot be empty" in str(exc_info.value)

    def test_add_task_with_whitespace_title_raises_validation_error(self) -> None:
        """Test that whitespace-only title raises ValidationError."""
        service = TaskService()

        with pytest.raises(ValidationError) as exc_info:
            service.add_task("   ")

        assert "Title cannot be empty" in str(exc_info.value)

    def test_add_task_assigns_sequential_ids(self) -> None:
        """Test that tasks are assigned sequential IDs starting from 1."""
        service = TaskService()

        task1 = service.add_task("Task 1")
        task2 = service.add_task("Task 2")
        task3 = service.add_task("Task 3")

        assert task1.id == 1
        assert task2.id == 2
        assert task3.id == 3

    def test_add_task_strips_whitespace_from_title(self) -> None:
        """Test that title whitespace is stripped."""
        service = TaskService()

        task = service.add_task("  Buy groceries  ")

        assert task.title == "Buy groceries"

    def test_add_task_strips_whitespace_from_description(self) -> None:
        """Test that description whitespace is stripped."""
        service = TaskService()

        task = service.add_task("Task", "  Some description  ")

        assert task.description == "Some description"


class TestGetAllTasks:
    """Test cases for TaskService.get_all_tasks method."""

    def test_get_all_tasks_empty_list(self) -> None:
        """Test getting tasks when none exist."""
        service = TaskService()

        tasks = service.get_all_tasks()

        assert tasks == []

    def test_get_all_tasks_with_multiple_tasks(self) -> None:
        """Test getting all tasks when multiple exist."""
        service = TaskService()
        service.add_task("Task 1")
        service.add_task("Task 2")
        service.add_task("Task 3")

        tasks = service.get_all_tasks()

        assert len(tasks) == 3
        assert tasks[0].title == "Task 1"
        assert tasks[1].title == "Task 2"
        assert tasks[2].title == "Task 3"


class TestMarkComplete:
    """Test cases for TaskService.mark_complete method."""

    def test_mark_complete_on_incomplete_task(self) -> None:
        """Test marking an incomplete task as complete."""
        service = TaskService()
        task = service.add_task("Test task")
        assert task.status == TaskStatus.INCOMPLETE

        updated_task = service.mark_complete(task.id)

        assert updated_task.status == TaskStatus.COMPLETE
        assert updated_task.id == task.id

    def test_mark_complete_on_nonexistent_id_raises_error(self) -> None:
        """Test that marking non-existent task raises TaskNotFoundError."""
        service = TaskService()

        with pytest.raises(TaskNotFoundError) as exc_info:
            service.mark_complete(99)

        assert exc_info.value.task_id == 99


class TestMarkIncomplete:
    """Test cases for TaskService.mark_incomplete method."""

    def test_mark_incomplete_on_complete_task(self) -> None:
        """Test marking a complete task as incomplete."""
        service = TaskService()
        task = service.add_task("Test task")
        service.mark_complete(task.id)
        assert service.get_task(task.id).status == TaskStatus.COMPLETE

        updated_task = service.mark_incomplete(task.id)

        assert updated_task.status == TaskStatus.INCOMPLETE

    def test_mark_incomplete_on_nonexistent_id_raises_error(self) -> None:
        """Test that marking non-existent task raises TaskNotFoundError."""
        service = TaskService()

        with pytest.raises(TaskNotFoundError):
            service.mark_incomplete(99)


class TestUpdateTask:
    """Test cases for TaskService.update_task method."""

    def test_update_task_title_only(self) -> None:
        """Test updating only the title."""
        service = TaskService()
        task = service.add_task("Old title", "Description")

        updated = service.update_task(task.id, title="New title")

        assert updated.title == "New title"
        assert updated.description == "Description"

    def test_update_task_description_only(self) -> None:
        """Test updating only the description."""
        service = TaskService()
        task = service.add_task("Title", "Old description")

        updated = service.update_task(task.id, description="New description")

        assert updated.title == "Title"
        assert updated.description == "New description"

    def test_update_task_both_fields(self) -> None:
        """Test updating both title and description."""
        service = TaskService()
        task = service.add_task("Old title", "Old description")

        updated = service.update_task(
            task.id, title="New title", description="New description"
        )

        assert updated.title == "New title"
        assert updated.description == "New description"

    def test_update_task_nonexistent_id_raises_error(self) -> None:
        """Test that updating non-existent task raises TaskNotFoundError."""
        service = TaskService()

        with pytest.raises(TaskNotFoundError):
            service.update_task(99, title="New title")

    def test_update_task_with_empty_title_raises_validation_error(self) -> None:
        """Test that empty title raises ValidationError."""
        service = TaskService()
        task = service.add_task("Original title")

        with pytest.raises(ValidationError) as exc_info:
            service.update_task(task.id, title="")

        assert "Title cannot be empty" in str(exc_info.value)


class TestDeleteTask:
    """Test cases for TaskService.delete_task method."""

    def test_delete_task_success(self) -> None:
        """Test successfully deleting a task."""
        service = TaskService()
        task = service.add_task("Task to delete")

        service.delete_task(task.id)

        assert len(service.get_all_tasks()) == 0

    def test_delete_task_nonexistent_id_raises_error(self) -> None:
        """Test that deleting non-existent task raises TaskNotFoundError."""
        service = TaskService()

        with pytest.raises(TaskNotFoundError):
            service.delete_task(99)

    def test_delete_then_reaccess_raises_error(self) -> None:
        """Test that accessing deleted task raises TaskNotFoundError."""
        service = TaskService()
        task = service.add_task("Task to delete")
        service.delete_task(task.id)

        with pytest.raises(TaskNotFoundError):
            service.get_task(task.id)
