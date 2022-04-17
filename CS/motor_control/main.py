import autonomous_control
import remote_control
import SFR
from modes.movement_modes_enum import Mode

def read_movement_mode():
    pass
    # controller_output = read_controller_output()
    # SFR.mode = controller_output

def main_control_loop():
    # Read movement mode from remote controller

    # If mode is remote control, call remote_control execute
    if SFR.mode == Mode.REMOTE_CONTROL:
        remote_control.execute()

    # If mode autonomous, call autonomous execute
    if SFR.mode == Mode.AUTONOMOUS:
        autonomous_control.execute()
    pass


if __name__ == "__main__":
    while True:
        main_control_loop()
