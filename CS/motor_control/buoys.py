class Buoy:
    """
    Class for buoy objects.
    """
    color = ""
    shape = ""
    position = [0, 0, 0] # indicates the x, y, and z vector values from the ZED camera (we may be able to reduce this to just x, z)

    def __init__(self, color, shape, position):
        self.color = color
        self.shape = shape
        self.position = position

