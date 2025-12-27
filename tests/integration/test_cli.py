"""Integration tests for CLI flows."""

import pytest

from src.models import TaskNotFoundError, TaskStatus, ValidationError
from src.services import TaskService


class TestAddViewFlow:
    """Integration tests for Add → View flow."""

    def test_add_then_view_shows_task(self) -> None:
        """Test that added task appears in view."""
        service = TaskService()

        task = service.add_task("Test task", "Test description")

        tasks = service.get_all_tasks()
        assert len(tasks) == 1
        assert tasks[0].id == task.id
        assert tasks[0].title == "Test task"
        assert tasks[0].description == "Test description"

    def test_add_multiple_then_view_all(self) -> None:
        """Test that multiple added tasks all appear in view."""
        service = TaskService()

        service.add_task("Task 1")
        service.add_task("Task 2")
        service.add_task("Task 3")

        tasks = service.get_all_tasks()
        assert len(tasks) == 3
        titles = [t.title for t in tasks]
        assert "Task 1" in titles
        assert "Task 2" in titles
        assert "Task 3" in titles


class TestAddUpdateViewFlow:
    """Integration tests for Add → Update → View flow."""

    def test_add_update_then_view_shows_changes(self) -> None:
        """Test that updated task reflects changes in view."""
        service = TaskService()

        task = service.add_task("Original title", "Original description")
        service.update_task(task.id, title="Updated title", description="Updated description")

        tasks = service.get_all_tasks()
        assert len(tasks) == 1
        assert tasks[0].title == "Updated title"
        assert tasks[0].description == "Updated description"

    def test_update_preserves_status(self) -> None:
        """Test that updating task preserves its status."""
        service = TaskService()

        task = service.add_task("Task")
        service.mark_complete(task.id)
        service.update_task(task.id, title="Updated task")

        updated = service.get_task(task.id)
        assert updated.title == "Updated task"
        assert updated.status == TaskStatus.COMPLETE


class TestAddDeleteViewFlow:
    """Integration tests for Add → Delete → View flow."""

    def test_add_delete_then_view_empty(self) -> None:
        """Test that deleted task no longer appears in view."""
        service = TaskService()

        task = service.add_task("Task to delete")
        assert len(service.get_all_tasks()) == 1

        service.delete_task(task.id)

        tasks = service.get_all_tasks()
        assert len(tasks) == 0

    def test_delete_one_preserves_others(self) -> None:
        """Test that deleting one task preserves other tasks."""
        service = TaskService()

        task1 = service.add_task("Task 1")
        task2 = service.add_task("Task 2")
        task3 = service.add_task("Task 3")

        service.delete_task(task2.id)

        tasks = service.get_all_tasks()
        assert len(tasks) == 2
        ids = [t.id for t in tasks]
        assert task1.id in ids
        assert task2.id not in ids
        assert task3.id in ids


class TestAddToggleViewFlow:
    """Integration tests for Add → Toggle → View flow."""

    def test_add_complete_then_view_shows_complete(self) -> None:
        """Test that completed task shows correct status in view."""
        service = TaskService()

        task = service.add_task("Task")
        assert task.status == TaskStatus.INCOMPLETE

        service.mark_complete(task.id)

        tasks = service.get_all_tasks()
        assert tasks[0].status == TaskStatus.COMPLETE

    def test_toggle_complete_then_incomplete(self) -> None:
        """Test toggling task status back and forth."""
        service = TaskService()

        task = service.add_task("Task")
        service.mark_complete(task.id)
        service.mark_incomplete(task.id)

        updated = service.get_task(task.id)
        assert updated.status == TaskStatus.INCOMPLETE


class TestErrorHandling:
    """Integration tests for error handling scenarios."""

    def test_update_nonexistent_task_raises_error(self) -> None:
        """Test that updating non-existent task raises error."""
        service = TaskService()

        with pytest.raises(TaskNotFoundError):
            service.update_task(999, title="New title")

    def test_delete_nonexistent_task_raises_error(self) -> None:
        """Test that deleting non-existent task raises error."""
        service = TaskService()

        with pytest.raises(TaskNotFoundError):
            service.delete_task(999)

    def test_mark_complete_nonexistent_task_raises_error(self) -> None:
        """Test that marking non-existent task raises error."""
        service = TaskService()

        with pytest.raises(TaskNotFoundError):
            service.mark_complete(999)

    def test_add_empty_title_raises_validation_error(self) -> None:
        """Test that adding task with empty title raises error."""
        service = TaskService()

        with pytest.raises(ValidationError):
            service.add_task("")

    def test_ids_not_reused_after_delete(self) -> None:
        """Test that IDs are not reused after deletion."""
        service = TaskService()

        task1 = service.add_task("Task 1")
        task2 = service.add_task("Task 2")
        service.delete_task(task1.id)
        task3 = service.add_task("Task 3")

        assert task1.id == 1
        assert task2.id == 2
        assert task3.id == 3  # ID 1 is not reused
