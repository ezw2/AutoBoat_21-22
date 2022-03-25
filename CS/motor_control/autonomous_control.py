import mandatory_nav_channel as mnc
from enum import Enum

class Task(Enum):
    MANDATORY_NAV_CHANNEL = 1

def execute():
    mnc.execute()
