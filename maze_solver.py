class maze_solver:
    def __init__(self, maze):
        # store maze as an attribute, then find and store the starting and end position and explored positions
        self.maze = maze                    
        self.start = self.find_start()
        self.end = self.find_end()
        self.explored = set()

