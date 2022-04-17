"""
This file contains the software for completing the Mandatory Navigation Channel Task.
"""
from modes.tasks_enum import Task
import SFR

def execute():
    # Determine goal position
    # Outline path to take
    # Follow path using PID control
    if isComplete():
        SFR.MNC = True
        SFR.task = Task.DETERMINE_TASK

def isComplete():
    #returns a boolean indicating whether the mandatory navigation channel task is complete
    pass