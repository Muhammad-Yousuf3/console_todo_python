"""Unit tests for Task dataclass."""

import pytest

from src.models import Task, TaskStatus


class TestTask:
    """Test cases for Task dataclass creation."""

    def test_create_task_with_all_fields(self) -> None:
        """Test creating a task with all fields specified."""
        task = Task(
            id=1,
            title="Buy groceries",
            description="Milk, eggs, bread",
            status=TaskStatus.INCOMPLETE,
        )

        assert task.id == 1
        assert task.title == "Buy groceries"
        assert task.description == "Milk, eggs, bread"
        assert task.status == TaskStatus.INCOMPLETE

    def test_create_task_with_minimal_fields(self) -> None:
        """Test creating a task with only required fields."""
        task = Task(id=2, title="Call mom")

        assert task.id == 2
        assert task.title == "Call mom"
        assert task.description == ""
        assert task.status == TaskStatus.INCOMPLETE

    def test_task_default_status_is_incomplete(self) -> None:
        """Test that default status is INCOMPLETE."""
        task = Task(id=3, title="Test task")

        assert task.status == TaskStatus.INCOMPLETE

    def test_task_default_description_is_empty(self) -> None:
        """Test that default description is empty string."""
        task = Task(id=4, title="Test task")

        assert task.description == ""

    def test_create_complete_task(self) -> None:
        """Test creating a task with COMPLETE status."""
        task = Task(
            id=5,
            title="Finished task",
            status=TaskStatus.COMPLETE,
        )

        assert task.status == TaskStatus.COMPLETE


class TestTaskStatus:
    """Test cases for TaskStatus enum."""

    def test_incomplete_value(self) -> None:
        """Test INCOMPLETE enum value."""
        assert TaskStatus.INCOMPLETE.value == "incomplete"

    def test_complete_value(self) -> None:
        """Test COMPLETE enum value."""
        assert TaskStatus.COMPLETE.value == "complete"

    def test_enum_members(self) -> None:
        """Test that TaskStatus has exactly two members."""
        members = list(TaskStatus)
        assert len(members) == 2
        assert TaskStatus.INCOMPLETE in members
        assert TaskStatus.COMPLETE in members
