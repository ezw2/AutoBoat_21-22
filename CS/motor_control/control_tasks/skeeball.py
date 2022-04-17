"""
This file contains the software for completing the Skeeball Task
"""
from modes.tasks_enum import Task
import SFR
def execute():
    # The boat must deploy and shoot balls through the frame and onto the skeeball table, in any of the three holes
    
    if isComplete():
        SFR.SKEEBALL = True
        SFR.task = Task.DETERMINE_TASK

def isComplete():
    #returns a boolean indicating whether the skeeball task is complete
    pass
