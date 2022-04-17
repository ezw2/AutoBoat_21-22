"""
Enumerates the different tasks for the boat.
"""
from enum import Enum

class Task(Enum):
    DETERMINE_TASK = 0

    # Objectives
    MANDATORY_NAV_CHANNEL = 1
    AVOID_THE_CROWDS = 2
    FIND_SEAT = 3
    SNACK_RUN = 4
    SKEEBALL = 5
    WATER_BLAST = 6
    RETURN_HOME = 7

    
    # Transitions
    TRANSITION_TO_MNC = 8
    TRANSITION_TO_AVOID = 9
    TRASITION_TO_SEAT = 10
    TRANSITION_TO_SNACK = 11
    TRANSITION_TO_SKEEBALL = 12
    TRANSITION_TO_WATER_BLAST = 13
    TRANSITION_TO_HOME = 14