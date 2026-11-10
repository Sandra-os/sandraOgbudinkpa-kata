"""
The class MazeSolver solves
mazes using a depth-first search algorithm.
"""
class MazeSolver:
    """Find routes through a grid using depth-first search."""
    def __init__(self, maze):
        # find and store the
        # starting and end position and explored positions
        self.maze = maze
        self.start = self.find_start()
        self.end = self.find_end()
        self.explored = set()

    # User Story 1: Find the empty space in a single-row input
    def find_start(self):
        # Iterate through the rows and columns in the maze and
        # the elements in the row and column to find starting position
        """Return the coordinates of the first start marker (2)."""
        for row_pos, row in enumerate(self.maze):
            for column_pos, value in enumerate(row):
                # starting position of 2
                if value == 2:
                    return (row_pos, column_pos)

    def find_end(self):
        # the elements in the row and column to find ending position
        """Return the coordinates of the first end marker (3)."""
        for row_pos, row in enumerate(self.maze):
            for column_pos, value in enumerate(row):
                # If value is 3, return its position. End position
                if value == 3:
                    return (row_pos, column_pos)

    def get_solution(self):
        """Return the first route from the stored start to the end."""
        path_followed = self.solve(self.start[0], self.start[1])
        return path_followed

    # User Story 2: Walk through a hallway using depth-first search algorithm
    def solve(self, row, column):
        """Explore an unvisited cell, returning a route or None."""
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
        self.explored.add((row, column))  # to keep track of the explored position

        # position at maze end?
        if (row, column) == self.end:
            return [(row, column)]

        # to move in all four directions
        for path_dir in [(1, 0), (-1, 0), (0, 1), (0, -1)]:  # down, up, right, left
            new_row, new_column = row + path_dir[0], column + path_dir[1]
            path_followed = self.solve(new_row, new_column)
            # If a path is found, return the current position and then continue path
            if path_followed is not None:
                return [(row, column)] + path_followed

        # return None if no path is found, path must have no walls ahead
        return None


def find_maze_path(maze):
    """Create a solver and return its first route through the grid."""
    solver = MazeSolver(maze)
    # find path with the get_solution function call
    return solver.get_solution()
