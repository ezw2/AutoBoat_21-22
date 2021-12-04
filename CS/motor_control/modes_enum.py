"""Enumerates the movement modes for the boat."""
from enum import Enum


class Mode(Enum):
    REMOTE_CONTROL = 1
    MANDATORY_NAV_CHANNEL = 2
    WINDING_NAV_CHANNEL = 3
    CIRCUMNAVIGATION = 4
    SPEED_GATE = 5
    ACOUSTIC_DOCKING = 6
    RETURN_TO_START = 7
