class Room:
    """ This is a class that defines Rooms."""
    def __init__(self):
        """ Set up Room attributes. """
        self.description = ""
        self.north = 0
        self.south = 0
        self.east = 0
        self.west = 0


def main():

    """Main program function."""
    my_list = []
    room = Room()