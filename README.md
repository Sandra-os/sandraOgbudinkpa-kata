# sandraOgbudinkpa-kata

Analysis of Story 1: 
The maze solver is implemented for general purposes and it struggles to solve mazes with loops or a lot of paths. The depth-first search (DFS) algorithm used here may take a lot of unneeded detours before coming up with a solution. Additionally, DFS will still investigate every route if the maze has no solution, which can take some time.


Analysis of Story 2: 
The time complexity of the current implementation is O(4(n*m)), where n and m are the dimensions of the maze. This is because in the worst case it does a depth-first search and checks every path making the optimization slower. We may also use other methods such as: 

A* Search Algorithm: The A* algorithm explores the maze more efficiently and eliminates implausible solution paths by using a heuristic method that estimates the remaining distance to the goal. It finds the optimal path between two nodes in a graph.

Bidirectional Search: Performs two searches simultaneously, one from the head, one from the tail, and stopping when they cross each other hence finding the shortest path. As a result, the search space can be significantly reduced.

