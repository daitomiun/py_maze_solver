from maze import Maze
from window import Window
import sys

def main():
    num_rows = 14
    num_cols = 20
    margin = 50
    screen_x = 800
    screen_y = 600
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows
    sys.setrecursionlimit(10000)
    win = Window(screen_x, screen_y)
    maze = Maze(
        x1=margin,
        y1=margin,
        num_rows=num_rows,
        num_cols=num_cols,
        cell_size_x=cell_size_x,
        cell_size_y=cell_size_y,
        win=win,
        maze_gen_speed=0.005
    )
    is_solvable = maze.solve()
    if not is_solvable:
        print("ERROR: maze not solvable")
    else:
        print("WIN!!!: maze is solvable")
    win.wait_for_close()

main()
