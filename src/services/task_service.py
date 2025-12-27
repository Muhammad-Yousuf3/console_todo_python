"""Task service for managing todo tasks with in-memory storage."""

from src.models import Task, TaskNotFoundError, TaskStatus, ValidationError


class TaskService:
    """Business logic layer for task management.

    Provides CRUD operations and status toggling for tasks.
    All tasks are stored in memory and lost when the application exits.
    """

    def __init__(self) -> None:
        """Initialize TaskService with empty storage."""
        self._tasks: dict[int, Task] = {}
        self._next_id: int = 1

    def add_task(self, title: str, description: str = "") -> Task:
        """Add a new task with the given title and optional description.

        Args:
            title: Required task title (1-200 characters, non-whitespace-only).
            description: Optional task description (defaults to empty string).

        Returns:
            The created Task with assigned ID.

        Raises:
            ValidationError: If title is empty or whitespace-only.
        """
        if not title or not title.strip():
            raise ValidationError("Title cannot be empty")

        task = Task(
            id=self._next_id,
            title=title.strip(),
            description=description.strip() if description else "",
            status=TaskStatus.INCOMPLETE,
        )
        self._tasks[self._next_id] = task
        self._next_id += 1
        return task

    def get_all_tasks(self) -> list[Task]:
        """Get all tasks.

        Returns:
            List of all tasks (empty list if none exist).
        """
        return list(self._tasks.values())

    def get_task(self, task_id: int) -> Task:
        """Get a task by ID.

        Args:
            task_id: The ID of the task to retrieve.

        Returns:
            The Task with the specified ID.

        Raises:
            TaskNotFoundError: If no task exists with the given ID.
        """
        if task_id not in self._tasks:
            raise TaskNotFoundError(task_id)
        return self._tasks[task_id]

    def update_task(
        self,
        task_id: int,
        title: str | None = None,
        description: str | None = None,
    ) -> Task:
        """Update a task's title and/or description.

        Args:
            task_id: The ID of the task to update.
            title: New title (None to keep current).
            description: New description (None to keep current).

        Returns:
            The updated Task.

        Raises:
            TaskNotFoundError: If no task exists with the given ID.
            ValidationError: If new title is empty or whitespace-only.
        """
        task = self.get_task(task_id)

        if title is not None:
            if not title or not title.strip():
                raise ValidationError("Title cannot be empty")
            task.title = title.strip()

        if description is not None:
            task.description = description.strip()

        return task

    def delete_task(self, task_id: int) -> None:
        """Delete a task by ID.

        Args:
            task_id: The ID of the task to delete.

        Raises:
            TaskNotFoundError: If no task exists with the given ID.
        """
        if task_id not in self._tasks:
            raise TaskNotFoundError(task_id)
        del self._tasks[task_id]

    def mark_complete(self, task_id: int) -> Task:
        """Mark a task as complete.

        Args:
            task_id: The ID of the task to mark complete.

        Returns:
            The updated Task with status=COMPLETE.

        Raises:
            TaskNotFoundError: If no task exists with the given ID.
        """
        task = self.get_task(task_id)
        task.status = TaskStatus.COMPLETE
        return task

    def mark_incomplete(self, task_id: int) -> Task:
        """Mark a task as incomplete.

        Args:
            task_id: The ID of the task to mark incomplete.

        Returns:
            The updated Task with status=INCOMPLETE.

        Raises:
            TaskNotFoundError: If no task exists with the given ID.
        """
        task = self.get_task(task_id)
        task.status = TaskStatus.INCOMPLETE
        return task
