"""
This file contains the software for completing the Return Home Task
"""
from modes.tasks_enum import Task
import SFR

def execute():
    # Determine launch point position
    # Outline path to take, make sure it avoids all obstacles
    # Follow path using PID control
    if isComplete():
        SFR.RETURN_HOME = True
        SFR.task = Task.DETERMINE_TASK

def isComplete():
    #returns a boolean indicating whether the return home task is complete
    pass