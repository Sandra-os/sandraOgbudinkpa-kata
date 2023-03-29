# sandraOgbudinkpa-kata

Analysis of Story 1: 
The maze solver is implemented for general purposes and it struggles to solve mazes with loops or a lot of paths. The depth-first search (DFS) algorithm used here may take a lot of unneeded detours before coming up with a solution. Additionally, DFS will still investigate every route if the maze has no solution, which can take some time.