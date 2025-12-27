"""Menu display and input handling for Todo Console Application."""

from src.cli.formatters import display_error, display_success, format_task_list
from src.models import TaskNotFoundError, ValidationError
from src.services import TaskService


def show_menu() -> None:
    """Display the main menu options."""
    print("\n=== Todo Application ===\n")
    print("1. Add task")
    print("2. View all tasks")
    print("3. Update task")
    print("4. Delete task")
    print("5. Mark complete")
    print("6. Mark incomplete")
    print("7. Quit")
    print()


def get_user_choice() -> str:
    """Get and validate user menu choice.

    Returns:
        The user's choice as a string (1-7).
    """
    return input("Enter choice (1-7): ").strip()


def get_task_id() -> int | None:
    """Prompt for and validate a task ID.

    Returns:
        The task ID as an integer, or None if invalid.
    """
    try:
        id_str = input("Enter task ID: ").strip()
        return int(id_str)
    except ValueError:
        display_error("Invalid task ID")
        return None


def prompt_add_task(service: TaskService) -> None:
    """Prompt user to add a new task.

    Args:
        service: The TaskService instance to use.
    """
    title = input("Enter task title: ")
    description = input("Enter description (optional): ")

    try:
        task = service.add_task(title, description)
        display_success(f"Task created with ID {task.id}")
    except ValidationError as e:
        display_error(e.message)


def prompt_view_tasks(service: TaskService) -> None:
    """Display all tasks.

    Args:
        service: The TaskService instance to use.
    """
    tasks = service.get_all_tasks()
    print()
    print(format_task_list(tasks))


def prompt_update_task(service: TaskService) -> None:
    """Prompt user to update a task.

    Args:
        service: The TaskService instance to use.
    """
    task_id = get_task_id()
    if task_id is None:
        return

    try:
        task = service.get_task(task_id)
        print(f"Current title: {task.title}")
        new_title = input("Enter new title (or Enter to keep): ").strip()
        print(f"Current description: {task.description}")
        new_description = input("Enter new description (or Enter to keep): ")

        service.update_task(
            task_id,
            title=new_title if new_title else None,
            description=new_description if new_description else None,
        )
        display_success(f"Task {task_id} updated")
    except TaskNotFoundError:
        display_error("Task not found")
    except ValidationError as e:
        display_error(e.message)


def prompt_delete_task(service: TaskService) -> None:
    """Prompt user to delete a task.

    Args:
        service: The TaskService instance to use.
    """
    task_id = get_task_id()
    if task_id is None:
        return

    try:
        service.delete_task(task_id)
        display_success(f"Task {task_id} deleted")
    except TaskNotFoundError:
        display_error("Task not found")


def prompt_mark_complete(service: TaskService) -> None:
    """Prompt user to mark a task as complete.

    Args:
        service: The TaskService instance to use.
    """
    task_id = get_task_id()
    if task_id is None:
        return

    try:
        service.mark_complete(task_id)
        display_success(f"Task {task_id} marked as complete")
    except TaskNotFoundError:
        display_error("Task not found")


def prompt_mark_incomplete(service: TaskService) -> None:
    """Prompt user to mark a task as incomplete.

    Args:
        service: The TaskService instance to use.
    """
    task_id = get_task_id()
    if task_id is None:
        return

    try:
        service.mark_incomplete(task_id)
        display_success(f"Task {task_id} marked as incomplete")
    except TaskNotFoundError:
        display_error("Task not found")
