import SFR
from modes.tasks_enum import Task

"""
This file contains the software for transitioning 
General idea:
- Identify next task and location
- Outline path to the next task
- Calculate optimal orientation for the next task
- Follow path using PID control
- Check if transition has been completed
- Update the SFR to the task transitioned to
"""
def MNCcomplete():
    pass

def executeMNC():
    if MNCcomplete:
      SFR.task = Task.MANDATORY_NAV_CHANNEL
    pass

def AVOIDcomplete():
    pass

def executeAVOID():
    # If camera sees at least one red, yellow, and green buoy Task 1 (Avoid the Crowd)
    if AVOIDcomplete():
      SFR.task = Task.AVOID_THE_CROWDS
    pass

def SEATcomplete():
    pass

def executeSEAT():
    # If camera sees colored shapes Task 2 (Find a seat)
    if SEATcomplete():
      SFR.task = Task.FIND_SEAT
    pass

def SNACKcomplete():
    pass

def executeSNACK():
    # If camera sees only 1 red and green buoy and and a blue buoy farther away Task 3 (Snack run)
    if SNACKcomplete():
      SFR.task = Task.SNACK_RUN
    pass

def SKEEBALLcomplete():
    pass

def executeSKEEBALL():
    # If camera sees purple frame Task 4 (Skeeball)
    if SEATcomplete():
      SFR.task = Task.SKEEBALL
    pass

def WATERBLASTcomplete():
    pass

def executeWATER_BLAST():
    # If camera sees a target face Task 5 (Water Blast)
    if WATERBLASTcomplete():
      SFR.task = Task.WATER_BLAST
    pass

def HOMEcomplete():
    pass

def executeHOME():
    # If completed all task 1-5 complete Task 6 (Return Home)
    if HOMEcomplete():
      SFR.task = Task.HOME
    pass


def execute():
    # general transition? or transition if it shuts off and has to restart?

    # If camera sees at least one red, yellow, and green buoy Task 1 (Avoid the Crowd)
    # If camera sees colored shapes Task 2 (Find a seat)
    # If camera sees only 1 red and green buoy and and a blue buoy father away Task 3 (Snack run)
    # If camera sees purple frame Task 4 (Skeeball)
    # If camera sees a target face Task 5 (Water Blast)
    # If completed all task 1-5 complete Task 6 (Return Home)
    pass