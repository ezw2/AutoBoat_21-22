"""
This file determines the exact autonomous execution sequence.
"""

from modes.tasks_enum import Task
import SFR
import control_tasks.mandatory_nav_channel as mandatory_nav_channel
import control_tasks.determine_task as determine_task
import control_tasks.avoid_the_crowds as avoid_the_crowds
import control_tasks.find_a_seat as find_seat
import control_tasks.snack_run as snack_run
import control_tasks.skeeball as skeeball
import control_tasks.water_blast as water_blast
import control_tasks.return_home as return_home
import control_tasks.transitions as transitions


def execute():
    if SFR.task == Task.DETERMINE_TASK:
        determine_task.execute()
    elif SFR.task == Task.MANDATORY_NAV_CHANNEL:
        mandatory_nav_channel.execute()
    elif SFR.task == Task.AVOID_THE_CROWDS:
        avoid_the_crowds.execute()
    elif SFR.task == Task.FIND_SEAT:
        find_seat.execute()
    elif SFR.task == Task.SNACK_RUN:
        snack_run.execute()
    elif SFR.task == Task.SKEEBALL:
        skeeball.execute()
    elif SFR.task == Task.WATER_BLAST:
        water_blast.execute()
    elif SFR.task == Task.RETURN_HOME:
        return_home.execute()
    elif SFR.task == Task.TRASITION_TO_MNC:
        transitions.executeMNC()
    elif SFR.task == Task.TRANSITION_TO_AVOID:
        transitions.executeAVOID()
    elif SFR.task == Task.TRASITION_TO_SEAT:
        transitions.executeSEAT()
    elif SFR.task == Task.TRASITION_TO_SNACK:
        transitions.executeSNACK()
    elif SFR.task == Task.TRASITION_TO_SKEEBALL:
        transitions.executeSKEEBALL()
    elif SFR.task == Task.TRANSITION_TO_WATER_BLAST:
        transitions.executeWATER_BLAST()
    elif SFR.task == Task.TRASITION_TO_HOME:
        transitions.executeHOME()

    



