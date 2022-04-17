"""
A file of global variables to be referenced and read in other files.
"""

from modes.movement_modes_enum import Mode
from modes.tasks_enum import Task

# Boat state variables
mode = Mode.REMOTE_CONTROL
task = Task.DETERMINE_TASK

# Task tracking
is_mnc_complete = False
