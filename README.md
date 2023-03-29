# sandraOgbudinkpa-kata
***Part 1***
**Algorithm Approach**
The given MazeSolver implementation uses a depth-first search (DFS) algorithm as its algorithmic approach. The DFS algorithm works by investigating a path in a maze as thoroughly as possible before retreating to explore different paths. 

1. Begin at the specified starting point. 
2. Return the path to the current location if the current position is the end point. 
3. Make a note of the present location as explored. 
4. Do the following steps for each possible direction (up, down, left, right): 
    a. Move in that direction to the next cell. 
    b. Recursively apply the DFS method if the new point is valid (not a wall, within the maze bounds, and not yet explored).
    c. If the recursive call returns a non-empty path, the current position is appended to the path and returned. 
5. If no valid path is found, go back and return to an empty path.
This method is simple to implement and can solve many maze problems. although, it may not be the most efficient solution, as many unnecessary paths are explored before finding a solution. Alternative algorithms such as fBidirectional Search and A* search would be more efficient.

*User Stories*
The solve method in the MazeSolver class incorporates User Stories 2 through 5 using a depth-first search algorithm. This algorithm visits each cell recursively and backtracks when it encounters a dead end. Here's how each user story is addressed:

User Story 2 (Walk through a "hallway" maze):
The depth-first search algorithm naturally handles hallway mazes. When it encounters a hallway, it simply follows the empty path until it reaches the end or another branching point.
User Story 3 (Find a way into and out of rooms):
The algorithm explores all possible paths, including those leading into and out of rooms. If it encounters a room with an exit, it will continue exploring the path beyond the exit. If the room is a dead end, the algorithm backtracks and tries other paths.
User Story 4 (Follow winding paths):
The depth-first search algorithm is designed to handle winding paths. It will follow a winding path until it reaches a dead end or the end of the maze. If the path leads to a dead end, the algorithm will backtrack and explore other possibilities. If the path leads to the end of the maze, the algorithm will return the successful path.
User Story 5 (Reach the end of the maze, even if there are dead ends):
The algorithm can find a path to the end of the maze, even if there are dead ends along the way. When it encounters a dead end, it backtracks to the last branching point and continues exploring other paths. This ensures that it will explore all possible paths and eventually find the correct one that leads to the end of the maze.
In summary, the solve method uses a depth-first search algorithm to explore the maze recursively, following hallways, entering and exiting rooms, and navigating winding paths. It handles dead ends by backtracking and trying other paths, ensuring that it will find the correct path to the end of the maze.





***Part 2***

**Analysis of Story 1:** 
The maze solver is implemented for general purposes and it struggles to solve mazes with loops or a lot of paths. The depth-first search (DFS) algorithm used here may take a lot of unneeded detours before coming up with a solution. Additionally, DFS will still investigate every route if the maze has no solution, which can take some time.


**Analysis of Story 2:**
The time complexity of the current implementation is O(4(n*m)), where n and m are the dimensions of the maze. This is because in the worst case it does a depth-first search and checks every path making the optimization slower. We may also use other methods such as: 

A* Search Algorithm: The A* algorithm explores the maze more efficiently and eliminates implausible solution paths by using a heuristic method that estimates the remaining distance to the goal. It finds the optimal path between two nodes in a graph.

Bidirectional Search: Performs two searches simultaneously, one from the head, one from the tail, and stopping when they cross each other hence finding the shortest path. As a result, the search space can be significantly reduced.


**Analysis of Story 3:**
Possible way to approach this problem will be a step-by-step story, to be able to build and test each story: 

Story 1:
The ship and the maze are described to be of the same size and position. It will be best implemented with a tuple.

Story 2:
The algorithm should also be used to check for a path that fits the description of the maze. It will need to determine if the ship can navigate through the passages and if there is enough room to rotate as needed.

Story 3:
since the ship has to be able to move around a 3*3 space, the ship must be capable of rotating at any given time, this will involve the ship mechanics.

Story 4:
Then a different algorithm will be used like A* Search Algorithm and Bidirectional Search as discussed in analysis 2.

Story 5:
The algorithm must be optimized for efficiency and adapt to changes.

**How to run the program**

To run the maze_solver and maze_solver_test program, follow these steps:

1. Have Python installed device. If not on device, have it installed, you can download it from https://www.python.org/downloads/.
2. Install the pytest testing framework, which will be used to run the tests. install pip and pytest
3. Open IDE and create two files in your project folder:
4. Download maze_solver.py file and test_maze_solver.py from the github repository
5. Open terminal and type pytest test_maze_solver.py
If everything is set up correctly, you should see the test results in the terminal, indicating whether the tests passed or failed.
6. Other test files can be used to test the maze_solver.py program. "from maze_solver import MazeSolver, find_maze_path" should be added to the first line of the test program.
