"""
This file contains the software for completing the Avoid The Crowd Task
"""
from modes.tasks_enum import Task
import SFR

def execute():
    # The boat will find/outline a path through the obstacle red, yellow, and green buoy
    # The boat will alway stay in between the green and red buoy
    # The yellow buoy will always be between a red and green buoy
    # The boat will choose the closest, easiest path to pass through two different colored buoy
    # Follow path using PID control

    if isComplete():
        SFR.AVOID_THE_CROWD = True
        SFR.task = Task.DETERMINE_TASK


def isComplete():
    #returns a boolean indicating whether the avoid the crowds task is complete
    pass
