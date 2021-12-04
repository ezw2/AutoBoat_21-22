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

max_power = 100
percent_power = 0


class Sector(Enum):
    CENTER = 0
    TOP = 1
    BOTTOM = 2
    LEFT = 3
    RIGHT = 4


def read_channels():
    channel_5_reading = read_channel_5()  # placeholder function, x
    channel_6_reading = read_channel_6()  # placeholder function, y


def calculate_stick_dist():
    stick_dist = pow(pow(channel_5_reading - VERTICAL_MIDDLE, 2) +
                     pow(channel_6_reading - HORIZONTAL_MIDDLE, 2), 0.5)


def determine_sector():
    y = channel_6_reading
    x = channel_5_reading

    #if stick_dist < STOP_RADIUS:
    #    sector = Sector.CENTER

    if y >= VERTICAL_MIDDLE + STOP_RADIUS:
        sector = Sector.TOP
        percent_power = (y - VERTICAL_MIDDLE)/(FORWARD_MAX - VERTICAL_MIDDLE)

    elif y <= VERTICAL_MIDDLE - STOP_RADIUS:
        sector = Sector.BOTTOM
        percent_power = (y - VERTICAL_MIDDLE)/(BACKWARD_MAX - VERTICAL_MIDDLE)

    elif x >= HORIZONTAL_MIDDLE + STOP_RADIUS:
        sector = Sector.RIGHT
        percent_power = (x - HORIZONTAL_MIDDLE)/(RIGHT_MAX - HORIZONTAL_MIDDLE)

    elif x <= HORIZONTAL_MIDDLE - STOP_RADIUS:
        sector = Sector.LEFT
        percent_power = (x - HORIZONTAL_MIDDLE)/(LEFT_MAX - HORIZONTAL_MIDDLE)

    else:
        sector = Sector.CENTER
        percent_power = 0
    
    # if stick_dist < STOP_RADIUS:
    #     sector = Sector.CENTER
    # elif channel_5_reading > VERTICAL_MIDDLE and channel_6_reading > HORIZONTAL_MIDDLE:
    #     sector = Sector.TOP_RIGHT
    # elif channel_5_reading > VERTICAL_MIDDLE and channel_6_reading < HORIZONTAL_MIDDLE:
    #     sector = Sector.TOP_LEFT
    # elif channel_5_reading < VERTICAL_MIDDLE and channel_6_reading < HORIZONTAL_MIDDLE:
    #     sector = Sector.BOTTOM_LEFT
    # elif channel_5_reading < VERTICAL_MIDDLE and channel_6_reading > HORIZONTAL_MIDDLE:
    #     sector = Sector.BOTTOM_RIGHT


def fire_motors():
    # fire motors based on which sector the control stick is in
    # stabilization from gyroscope
    cur_power = (max_power * percent_power)/2
    if sector == Sector.TOP:
        #both motors are cur_power
        pass
    elif sector == Sector.BOTTOM:
        #both motors are cur_power*-1
        pass
    elif sector == Sector.LEFT:
        #left motor is cur_power*-1, right is cur_power
        pass
    elif sector == Sector.RIGHT:
        #left motor is cur_power, right is cur_power*-1
        pass
    else:
        #both motors are 0
        pass
    


def execute():
    read_channels()
    calculate_stick_dist()
    determine_sector()
    fire_motors()
