from enum import Enum

class States(Enum):
    IDLE = 1
    RUNNING = 2
    PAUSED = 3
    COMPLETED = 4