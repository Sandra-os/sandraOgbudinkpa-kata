# sandraOgbudinkpa-kata

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

Story 2
The algorithm should also be used to check for a path that fits the description of the maze. It will need to determine if the ship can navigate through the passages and if there is enough room to rotate as needed.

Story 3
since the ship has to be able to move around a 3*3 space, the ship must be capable of rotating at any given time, this will involve the ship mechanics.

Story 4
Then a different algorithm will be used like A* Search Algorithm and Bidirectional Search as discussed in analysis 2.

Story 5
The algorithm must be optimized for efficiency and adapt to changes.
