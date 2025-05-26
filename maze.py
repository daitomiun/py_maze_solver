from figures import Cell
import time


class Maze():
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win,
    ):
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cells = []
        self.__cells_size_x = cell_size_x
        self.__cells_size_y = cell_size_y
        self.__win = win 
        self.__create_cells()

    def __create_cells(self):
        for i in range(self.__num_cols):
            self.__cells.append([])
            for j in range(self.__num_rows):
                self.__cells[i].append(Cell(self.__win))
                self.__draw_cell(i, j)

    def __draw_cell(self, i, j):
        self.__cells[i][j].draw(
            self.__x1 * i, 
            self.__y1 * j, 
            self.__x1 + (self.__cells_size_x * i), 
            self.__y1 + (self.__cells_size_y * j)
        )
        self.__animate()

    def __animate(self):
        if self.__win is None:
            return
        self.__win.redraw()
        time.sleep(0.005)

