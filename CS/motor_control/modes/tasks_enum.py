"""
Enumerates the different tasks for the boat.
"""
from enum import Enum

class Task(Enum):
    DETERMINE_TASK = 0

    # Objectives
    MANDATORY_NAV_CHANNEL = 1
    
    # Transitions
    TRANSITION_TO_MNC = 10