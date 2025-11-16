# Maze Solver

A small Python project that generates and visually solves mazes using Tkinter.

<div style="max-width: 100%; height: auto;">
  <video style="width: 100%; height: auto;" controls>
    <source src="assets/maze_solver.mp4" type="video/mp4">
    Your browser does not support the video tag.
  </video>
</div>


## What this project does

- Generates a random maze and draws it using Tkinter.
- Provides a visual maze solver (animated) that walks through the maze to find the exit.

Note: The current solver implementation in `maze.py` uses a recursive depth-first search (DFS) backtracking approach to find a path from the entrance (top-left) to the exit (bottom-right). The repository is structured so additional algorithms (BFS, A*, Dijkstra) can be added and compared in the future.

## Files of interest

- `main.py` — launcher that creates a `Window` and a `Maze`, then runs the solver.
- `maze.py` — maze generation and solving logic.
- `cell.py` — visual cell representation and drawing helpers.
- `graphics.py` — thin Tkinter wrapper (Window, Point, Line) used for drawing.
- `tests.py` — basic unit tests for maze creation/structure.
- `assets/maze_solver.mp4` — demo video of the maze being solved.

## Requirements

- Python 3.10+
- Tkinter

## How to run

1. Make sure you have Python and Tkinter available.
2. From the project root run:

```bash
python3 main.py
```

This opens a window showing the maze being generated and then solved. The current animation speed is controlled inside `maze.py` by `time.sleep(0.05)` in the animation loop.

## Running tests

Run the bundled unit tests with:

```bash
python3 tests.py
```

The tests cover basic maze creation and that the entrance/exit walls are opened and the reset of visited flags.

## Current algorithm

- Maze generation: randomized recursive backtracker (a depth-first method that knocks down walls between cells).
- Maze solving: recursive DFS implemented in `Maze._solve_r`.


## Future plans

Planned improvements and experiments:

- Implement a BFS-based solver and make it selectable at runtime so we can compare path lengths and animation behavior.
- Add A* and Dijkstra implementations.
- Add a command-line interface to choose algorithm, maze size, seed, and animation speed.

## Notes / Tips

- To speed up animation for demonstrations, reduce or remove the `time.sleep(...)` calls in `maze.py`.


