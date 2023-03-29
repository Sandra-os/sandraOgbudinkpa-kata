"""
This module contains tests for the MazeSolver class in maze_solver.py and its functions.
"""
from maze_solver import MazeSolver, find_maze_path


# Test cases
# Walls are represented with 1 and empty spaces with 0 using n*m matrices.
# 2 represents a start position
# and 3 an end position.


# Empty space in a single row, user story 1
def empty_space():
    """
    This function finds the empty spaces in the maze.
    """
    maze = [1, 1, 1, 1, 2, 0, 3, 1]  # empty space = row 4
    solver = MazeSolver(maze)
    assert solver.start == (0, 4)
    assert solver.end == (0, 6)
    assert find_maze_path(maze) == [(0, 4), (0, 5), (0, 6)]


# through hallway, user story 2
def hallway():  # Function to test hallway maze
    """
    This function tests the hallway maze.
    """
    maze = [
        [1, 2, 1, 1, 1, 1],
        [1, 0, 1, 1, 1, 1],
        [1, 0, 1, 1, 1, 1],
        [1, 0, 1, 1, 1, 1],
        [1, 0, 1, 1, 1, 1],
        [1, 3, 1, 1, 1, 1]
    ]
    solver = MazeSolver(maze)
    # list of coordinate tuples (row, column), count starts at 0
    assert solver.start == (0, 4)
    assert solver.end == (5, 1)
    assert find_maze_path(maze) == [(0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1)]


# finding a way in and out of a room, user story 3
def through_room():
    """
    This function finds a way in and out of a room.
    """
    maze = [
        [1, 2, 1, 1, 1, 1, 1, 1],
        [1, 0, 1, 1, 1, 1, 1, 1],
        [1, 0, 1, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 1, 0, 1],
        [1, 1, 1, 1, 0, 1, 0, 1],
        [1, 1, 1, 1, 0, 1, 0, 1],
        [1, 1, 1, 1, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 3, 1]
    ]
    solver = MazeSolver(maze)
    assert solver.start == (0, 1)
    assert solver.end == (7, 6)
    assert find_maze_path(maze) == [(0, 1), (1, 1), (2, 1),
     (3, 1), (3, 2), (3, 3), (3, 4), (4, 4), (5, 4), (6, 4),
     (6, 5), (6, 6), (7, 6)]


# test to follow winding path, user story 4
def winding_path():
    """
    This is the function to follow a winding path.
    """
    maze = [
        [1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 1]
    ]
    solver = MazeSolver(maze)
    assert solver.start == (0, 1)
    assert solver.end == (8, 10)
    assert find_maze_path(maze) == [
        (0, 1), (1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 4), (3, 5), (4, 5),
        (5, 5), (5, 6), (5, 7), (6, 7), (7, 7), (7, 8), (7, 9), (7, 10), (8, 10)
    ]


# test to reach the end of a maze, even if there are dead ends, user story 5
def dead_end():
    """
    This is the function to force reach the end of the maze.
    """
    maze = [
        [1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1],
        [1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
        [1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1],
        [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1],
        [1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 1]
    ]
    solver = MazeSolver(maze)
    assert solver.start == (0, 1)
    assert solver.end == (8, 10)
    assert find_maze_path(maze) == [
        (0, 1), (1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 4), (3, 5),
        (3, 6), (3, 7), (2, 7), (1, 7), (1, 8), (1, 9), (2, 9), (3, 9),
        (4, 9), (5, 9), (5, 8), (5, 7), (5, 6), (6, 6), (7, 6), (7, 7),
        (7, 8), (7, 9), (7, 10), (8, 10)
    ]
