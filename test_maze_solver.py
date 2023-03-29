from maze_solver import maze_solver, find_maze_path
# Test cases 
# Walls are represented with 1 and empty spaces with 0 using n*m matrices. 2 represents a start position
# and 3 an end position.

# Empty space in a single row, user story 1
def empty_space():
    maze = [1, 1, 1, 1, 0, 1, 1, 1]         # empty space = row 4



# through hallway, user story 2
def hallway():                              # Function to test hallway maze
    maze = [
        [1, 2, 1, 1, 1, 1],
        [1, 0, 1, 1, 1, 1],
        [1, 0, 1, 1, 1, 1],
        [1, 0, 1, 1, 1, 1],
        [1, 0, 1, 1, 1, 1],
        [1, 3, 1, 1, 1, 1]
    ]
    # list of coordinate tuples (row, column), count starts at 0
    path_followed = [(0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1)]


# finding a way in and out of a room, user story 3
def through_room():
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
    path_followed = [(0, 1), (1, 1), (2, 1), (3, 1), (4, 4), (5, 4), (6, 4), (6, 5), (6, 6), (7, 6)]


# test to follow winding path, user story 4
def winding_path():
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
    path_followed = [(0, 1), (1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 2), (3, 1), (4, 1), (5, 1), (5, 2), (5, 3), (6, 3), (7, 3), (7, 4), (7, 5), (7, 6), (7, 7), (8, 7), (9, 7)]


# test to reach the end of a maze, even if there are dead ends, user story 5
def dead_end():
    [
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
    path_followed = [(0, 1), (1, 1), (2, 1), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (4, 5), (5, 5), (5, 6), (5, 7), (5, 8), (6, 8), (7, 8), (7, 9), (8, 9), (9, 9)]
