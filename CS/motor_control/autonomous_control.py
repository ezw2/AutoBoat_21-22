"""
This file determines the exact autonomous execution sequence.
"""

from modes.tasks_enum import Task
import SFR
import control_tasks.mandatory_nav_channel as mandatory_nav_channel
import control_tasks.determine_task as determine_task


def execute():
    if SFR.task == Task.DETERMINE_TASK:
        determine_task.execute()
    if SFR.task == Task.MANDATORY_NAV_CHANNEL:
        mandatory_nav_channel.execute()
