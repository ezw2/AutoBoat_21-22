OPTIMAL_POSITION=0
CURRENT_POSITION=0
ROOM_FOR_ERROR=0
TIME=0
# Calculate the optimal position/direction to move towards (gives the horizontal component relative to a buoy)
def calculate_goal_pos():
    # Sees buoy: try to make a formula that sees the first 2 sets of buoys and create optimal positioning
    # Else if there is only 2 buoys then new formula
    # No buoys should prepare for transition phase or turning
    pass

# Calculate the current position of the boat (x, y, z) relative to a buoy (returns vector)
def calculate_curr_pos():
    pass

# Moves towards the destination
def move(distance, angle, speed):
    # How would be fire the motors if we knew the angle and distance? 
    pass

# Determines if the boat should readjust position
def ShouldAdjust():
    curr_pos = calculate_curr_pos()
    #Should only call this method when the boat is off track or if it has been a long time since this method was last called 
    if (abs(OPTIMAL_POSITION-curr_pos)>ROOM_FOR_ERROR ):
        move()
        TIME=0


def ():
#knowing the optimal position, it should call should adjust 
#