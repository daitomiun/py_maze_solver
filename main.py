from maze import Maze
from window import Window

def main():
    num_rows = 12
    num_cols = 16
    margin = 50
    screen_x = 800
    screen_y = 600
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows
    win = Window(screen_x, screen_y)
    maze = Maze(
        x1=margin,
        y1=margin,
        num_rows=num_rows,
        num_cols=num_cols,
        cell_size_x=cell_size_x,
        cell_size_y=cell_size_y,
        win=win,
        seed=1
    )

    win.wait_for_close()

main()
