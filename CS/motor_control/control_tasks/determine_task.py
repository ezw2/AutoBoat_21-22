from modes.tasks_enum import Task
import SFR
"""
This file contains the software for completing the determining the next task to execute.
"""
def all_tasks_complete():
    return SFR.AVOID_THE_CROWD and SFR.FIND_A_SEAT and SFR.SKEEBALL and SFR.SNACK_RUN and SFR.WATER_BLAST

def execute():
    # Find closest task that is incomplete
    # Update the SFR so that the next loop calls the appropriate transition function

    # if all tasks are complete (set to True), return home
    if all_tasks_complete():
        SFR.task = Task.RETURN_HOME
    pass