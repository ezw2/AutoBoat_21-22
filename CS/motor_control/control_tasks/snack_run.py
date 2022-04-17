"""
This file contains the software for completing the Snack Run Task
"""
from modes.tasks_enum import Task
import SFR

def execute():
    # Locates the blue buoy 
    # Outline path to take to the blue buoy circle around it and the return back to it's starting position
    # Follow path using PID control

    if isComplete():
        SFR.SNACK_RUN = True
        SFR.task = Task.DETERMINE_TASK

def isComplete():
    #returns a boolean indicating whether the snack run task is complete
    pass