from enum import IntEnum


class TaskStatus(IntEnum):
    CREATED = 0
    TODO = 1
    IN_PROGRESS = 2
    COMPLETED = 3
