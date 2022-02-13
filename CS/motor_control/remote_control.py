"""Handles the remote control aspect of the boat's movement."""
import navio.rcinput
import navio.util
navio.util.check_apm()
rcin = navio.rcinput.RCInput()
from enum import Enum

# Channel 5 boundary values (indicates vertical position of control stick)
FORWARD_MAX = 1938.0
BACKWARD_MAX = 1257.0
VERTICAL_MIDDLE = (FORWARD_MAX + BACKWARD_MAX) / 2

# Channel 6 boundary values (indicates horizontal position of control stick)
RIGHT_MAX = 1863.0
LEFT_MAX = 1036.0
HORIZONTAL_MIDDLE = (RIGHT_MAX + LEFT_MAX) / 2

# No movement square boundary in the center of the stick's range of motion
STOP_BOUNDARY = 50.0

# This value is subjected to change depending on the electrical team 
MOTOR_FORWARDMAX=1.900
MOTOR_STOP=1.500
MOTOR_BACKWARDMAX=1.100
MOTOR_FORWARDTURN=(MOTOR_FORWARDMAX+MOTOR_STOP)/2
MOTOR_BACKWARDTURN=(MOTOR_STOP+MOTOR_BACKWARDMAX)/2

# Right is 1, Left is 2
pwm1 = navio.pwm.PWM(0)
pwm2 = navio.pwm.PWM(1)
pwm1.set_period(50)
pwm2.set_period(50)
pwm1.enable()
pwm2.enable()


channel_5_reading = VERTICAL_MIDDLE
channel_6_reading = HORIZONTAL_MIDDLE
# stick_dist = 0.0  # the control stick's distance from the center
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
    channel_5_reading = rcin.read(5) # placeholder function, x
    channel_6_reading = rcin.read(6)  # placeholder function, y


# def calculate_stick_dist():
#     stick_dist = pow(pow(channel_5_reading - VERTICAL_MIDDLE, 2) +
#                      pow(channel_6_reading - HORIZONTAL_MIDDLE, 2), 0.5)


def determine_sector():
    y = channel_6_reading
    x = channel_5_reading

    #if stick_dist < STOP_BOUNDARY:
    #    sector = Sector.CENTER

    if y >= VERTICAL_MIDDLE + STOP_BOUNDARY:
        sector = Sector.TOP
        percent_power = (y - VERTICAL_MIDDLE)/(FORWARD_MAX - VERTICAL_MIDDLE)

    elif y <= VERTICAL_MIDDLE - STOP_BOUNDARY:
        sector = Sector.BOTTOM
        percent_power = (y - VERTICAL_MIDDLE)/(BACKWARD_MAX - VERTICAL_MIDDLE)

    elif x >= HORIZONTAL_MIDDLE + STOP_BOUNDARY:
        sector = Sector.RIGHT
        percent_power = (x - HORIZONTAL_MIDDLE)/(RIGHT_MAX - HORIZONTAL_MIDDLE)

    elif x <= HORIZONTAL_MIDDLE - STOP_BOUNDARY:
        sector = Sector.LEFT
        percent_power = (x - HORIZONTAL_MIDDLE)/(LEFT_MAX - HORIZONTAL_MIDDLE)

    else:
        sector = Sector.CENTER
        percent_power = 0
    
    # if stick_dist < STOP_BOUNDARY:
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

    power=MOTOR_STOP+((MOTOR_FORWARDMAX-MOTOR_STOP)*percent_power)
    rpower=MOTOR_STOP-((MOTOR_STOP-MOTOR_FORWARDMAX)*percent_power)
   
    if sector == Sector.TOP:
        #both motors are power
        pwm1.set_duty_cycle(power)
        pwm2.set_duty_cycle(power)
    elif sector == Sector.BOTTOM:
        #both motors are rpower
        pwm1.set_duty_cycle(rpower)
        pwm2.set_duty_cycle(rpower)
    elif sector == Sector.LEFT:
        #left motor is rpower, right is power
        pwm1.set_duty_cycle(MOTOR_FORWARDTURN)
        pwm2.set_duty_cycle(MOTOR_BACKWARDTURN)
    elif sector == Sector.RIGHT:
        #left motor is power, right is rpower
        pwm1.set_duty_cycle(MOTOR_BACKWARDTURN)
        pwm2.set_duty_cycle(MOTOR_FORWARDTURN)
    else:
        #both motors are stationary
        pwm1.set_duty_cycle(MOTOR_STOP)
        pwm2.set_duty_cycle(MOTOR_STOP)
    



def execute():
    read_channels()
    # calculate_stick_dist()
    determine_sector()
    fire_motors()


with navio.pwm.PWM(PWM_OUTPUT), navio.pwm.PWM(PWM_OUTPUT2) as pwm, pwm2:
    pwm.set_period(50)
    pwm2.set_period(50)
    pwm.enable()

    while (True):
        pwm.set_duty_cycle(SERVO_MIN)
        time.sleep(1)
        pwm.set_duty_cycle(SERVO_MAX)
        time.sleep(1)
