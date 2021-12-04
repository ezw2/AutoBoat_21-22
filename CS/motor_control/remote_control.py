"""Handles the remote control aspect of the boat's movement."""

from enum import Enum

FORWARD_MAX = 1938.0
BACKWARD_MAX = 1257.0
VERTICAL_MIDDLE = (FORWARD_MAX + BACKWARD_MAX) / 2
RIGHT_MAX = 1863.0
LEFT_MAX = 1036.0
HORIZONTAL_MIDDLE = (RIGHT_MAX + LEFT_MAX) / 2
STOP_RADIUS = 50.0

channel_5_reading = VERTICAL_MIDDLE
channel_6_reading = HORIZONTAL_MIDDLE
stick_dist = 0.0  # the control stick's distance from the center
sector = 0


class Sector(Enum):
    CENTER = 0
    TOP_RIGHT = 1
    TOP_LEFT = 2
    BOTTOM_LEFT = 3
    BOTTOM_RIGHT = 4


def read_channels():
    channel_5_reading = read_channel_5()  # placeholder function
    channel_6_reading = read_channel_6()  # placeholder function


def calculate_stick_dist():
    stick_dist = pow(pow(channel_5_reading - VERTICAL_MIDDLE, 2) +
                     pow(channel_6_reading - HORIZONTAL_MIDDLE, 2), 0.5)


def determine_sector():
    if stick_dist < STOP_RADIUS:
        sector = Sector.CENTER
    elif channel_5_reading > VERTICAL_MIDDLE and channel_6_reading > HORIZONTAL_MIDDLE:
        sector = Sector.TOP_RIGHT
    elif channel_5_reading > VERTICAL_MIDDLE and channel_6_reading < HORIZONTAL_MIDDLE:
        sector = Sector.TOP_LEFT
    elif channel_5_reading < VERTICAL_MIDDLE and channel_6_reading < HORIZONTAL_MIDDLE:
        sector = Sector.BOTTOM_LEFT
    elif channel_5_reading < VERTICAL_MIDDLE and channel_6_reading > HORIZONTAL_MIDDLE:
        sector = Sector.BOTTOM_RIGHT


def fire_motors():
    # fire motors based on which sector the control stick is in
    # stabilization from gyroscope
    pass


def execute():
    read_channels()
    calculate_stick_dist()
    determine_sector()
    fire_motors()
