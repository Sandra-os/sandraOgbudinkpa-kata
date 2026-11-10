# Python maze solver

A recursive depth-first search exercise. `MazeSolver` finds the first route from the start to the end of a grid; it does not guarantee the shortest route.

## Input and result

Pass a list of rows. Cells use `1` for walls, `0` for open space, `2` for the start, and `3` for the end. The current implementation expects valid start and end markers; it does not validate missing or duplicate markers.

```python
from maze_solver import find_maze_path

maze = [[2, 0, 3]]
print(find_maze_path(maze))
# [(0, 0), (0, 1), (0, 2)]
```

The result is a list of `(row, column)` coordinates including both endpoints, or `None` when no route is found. Create a new solver for a new search: the explored-cell set belongs to the solver instance.

## Search behavior

The solver checks adjacent cells in this order: down, up, right, left. It records visited cells to avoid revisiting loops, follows each valid route recursively, and backtracks at dead ends. Hallways, rooms, winding paths, and dead ends use the same traversal.

Each cell is visited at most once, but recursion depth and repeated copying of path lists can make large mazes expensive. Python's recursion limit also bounds practical input size. Breadth-first search would be an alternative when the requirement is a shortest route in an unweighted grid; it is not implemented here.

## Run and validation

Use Python 3 and import `find_maze_path` from `maze_solver.py`, as in the example above. The solver has no external runtime dependencies.

`test_maze_solver.py` contains example assertions for the five original stories. Its functions currently lack pytest's `test_` prefix, so a normal `python3 -m pytest test_maze_solver.py` invocation does not collect them as tests. The single-row example also uses a flat list rather than a list of rows, and the hallway example's expected start coordinate differs from its grid. These limitations must be resolved before treating that file as a passing automated suite.

## Proposed extension

The original larger-ship scenario would require a search state containing position and orientation, collision checks for the full footprint, and explicit movement and rotation rules. That extension and alternative search algorithms remain design ideas; the current implementation searches for a single-cell route.
