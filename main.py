from maze import Maze
from window import Window

win = Window(1000, 800)
maze = Maze(
    x1=20,
    y1=20,
    num_rows=30,
    num_cols=30,
    cell_size_x=20,
    cell_size_y=20,
    win=win
)

win.wait_for_close()

