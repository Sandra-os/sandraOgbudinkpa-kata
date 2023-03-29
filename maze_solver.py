class maze_solver:
    def __init__(self, maze):
        # store maze as an attribute, then find and store the starting and end position and explored positions
        self.maze = maze                    
        self.start = self.find_start()
        self.end = self.find_end()
        self.explored = set()

    # User Story 1: Find the empty space in a single-row input
    def find_start(self):
        # Iterate through the rows and columns in the maze and the elements in the row and column to find starting position
        for row_pos, row in enumerate(self.maze):
            for column_pos, value in enumerate(row):
                # starting position of 2
                if value == 2:
                    return (row_pos, column_pos)
    def find_end(self):
        # Iterate through the rows and columns in the maze and the elements in the row and column to find ending position
        for row_pos, row in enumerate(self.maze):
            for column_pos, value in enumerate(row):
                # If value is 3, return its position. End position
                if value == 3:
                    return (row_pos, column_pos)

    def get_solution(self):
        # solve method is called, to get path followed from start to end position
        path_followed = self.solve(self.start[0], self.start[1])
        return path_followed

    # User Story 2: Walk through a hallway
    def solve(self, row, column):
        # Check for walls and boundries for current position in maze
        if (
            row < 0
            or column < 0
            or row >= len(self.maze)
            or column >= len(self.maze[row])
            or self.maze[row][column] == 1
        ):
            return None

        # need to know if a position has been explored, this also solves user story 5 specifically.
        if (row, column) in self.explored:
            return None
        self.explored.add((row, column)) # to keep track of the explored position
        
        # position at maze end?
        if (row, column) == self.end:
            return [(row, column)]

