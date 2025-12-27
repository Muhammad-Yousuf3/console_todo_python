"""Output formatting helpers for Todo Console Application."""

from src.models import Task


def display_success(message: str) -> None:
    """Display a success message to the user.

    Args:
        message: The success message to display.
    """
    print(f"✓ {message}")


def display_error(message: str) -> None:
    """Display an error message to the user.

    Args:
        message: The error message to display.
    """
    print(f"✗ {message}")


def truncate(text: str, max_length: int = 30) -> str:
    """Truncate text to max_length, adding ellipsis if needed.

    Args:
        text: The text to truncate.
        max_length: Maximum length (default 30).

    Returns:
        Truncated text with ellipsis if it exceeded max_length.
    """
    if len(text) <= max_length:
        return text
    return text[: max_length - 3] + "..."


def format_task_list(tasks: list[Task]) -> str:
    """Format a list of tasks for display.

    Args:
        tasks: List of tasks to format.

    Returns:
        Formatted string representation of the task list.
    """
    if not tasks:
        return "No tasks found."

    lines = []
    header = f"{'ID':<4}| {'Title':<32}| {'Description':<32}| {'Status':<12}"
    separator = "-" * 4 + "|" + "-" * 33 + "|" + "-" * 33 + "|" + "-" * 12
    lines.append(header)
    lines.append(separator)

    for task in tasks:
        title = truncate(task.title, 30)
        description = truncate(task.description, 30) if task.description else ""
        status = task.status.value
        line = f"{task.id:<4}| {title:<32}| {description:<32}| {status:<12}"
        lines.append(line)

    return "\n".join(lines)
