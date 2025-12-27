"""Custom exceptions for Todo Console Application."""


class TaskNotFoundError(Exception):
    """Raised when a task with the specified ID is not found.

    Attributes:
        task_id: The ID that was not found.
        message: Human-readable error message.
    """

    def __init__(self, task_id: int) -> None:
        """Initialize TaskNotFoundError.

        Args:
            task_id: The ID of the task that was not found.
        """
        self.task_id = task_id
        self.message = f"Task with ID {task_id} not found"
        super().__init__(self.message)


class ValidationError(Exception):
    """Raised when input validation fails.

    Attributes:
        message: Human-readable error message describing the validation failure.
    """

    def __init__(self, message: str) -> None:
        """Initialize ValidationError.

        Args:
            message: Description of the validation failure.
        """
        self.message = message
        super().__init__(self.message)
