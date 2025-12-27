"""Task model and status enum for Todo Console Application."""

from dataclasses import dataclass, field
from enum import Enum


class TaskStatus(Enum):
    """Enumeration representing the completion status of a task."""

    INCOMPLETE = "incomplete"
    COMPLETE = "complete"


@dataclass
class Task:
    """A single todo item.

    Attributes:
        id: Unique integer identifier (auto-assigned, sequential, never reused).
        title: Required text (1-200 characters).
        description: Optional text (0-1000 characters, empty string if not provided).
        status: Completion status, defaults to INCOMPLETE.
    """

    id: int
    title: str
    description: str = ""
    status: TaskStatus = field(default=TaskStatus.INCOMPLETE)
