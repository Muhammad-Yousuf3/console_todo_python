"""CLI package for Todo Console Application."""

from src.cli.formatters import display_error, display_success, format_task_list
from src.cli.menu import (
    get_user_choice,
    prompt_add_task,
    prompt_delete_task,
    prompt_mark_complete,
    prompt_mark_incomplete,
    prompt_update_task,
    prompt_view_tasks,
    show_menu,
)

__all__ = [
    "display_error",
    "display_success",
    "format_task_list",
    "get_user_choice",
    "prompt_add_task",
    "prompt_delete_task",
    "prompt_mark_complete",
    "prompt_mark_incomplete",
    "prompt_update_task",
    "prompt_view_tasks",
    "show_menu",
]
