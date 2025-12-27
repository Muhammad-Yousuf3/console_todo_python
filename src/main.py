"""Main entry point for Todo Console Application."""

from src.cli import (
    get_user_choice,
    prompt_add_task,
    prompt_delete_task,
    prompt_mark_complete,
    prompt_mark_incomplete,
    prompt_update_task,
    prompt_view_tasks,
    show_menu,
)
from src.cli.formatters import display_error
from src.services import TaskService


def main() -> None:
    """Run the Todo Console Application main loop."""
    service = TaskService()

    print("Welcome to Todo Console Application!")

    while True:
        show_menu()
        choice = get_user_choice()

        if choice == "1":
            prompt_add_task(service)
        elif choice == "2":
            prompt_view_tasks(service)
        elif choice == "3":
            prompt_update_task(service)
        elif choice == "4":
            prompt_delete_task(service)
        elif choice == "5":
            prompt_mark_complete(service)
        elif choice == "6":
            prompt_mark_incomplete(service)
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            display_error("Invalid choice. Please enter 1-7.")


if __name__ == "__main__":
    main()
