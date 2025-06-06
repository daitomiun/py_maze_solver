from figures import Cell
import time
import random

class Maze():
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
        seed=None,
        maze_gen_speed=0.005
    ):
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cells = []
        self.__cells_size_x = cell_size_x
        self.__cells_size_y = cell_size_y
        self.__win = win 
        self.__maze_gen_speed=maze_gen_speed
        if seed:
            random.seed(seed)
        self.__create_cells()
        self.__break_entrance_and_exit()
        self.__break_walls_r(0, 0)
        self.__reset_cells_visited()

    def __create_cells(self):
        for i in range(self.__num_cols):
            self.__cells.append([])
            for j in range(self.__num_rows):
                self.__cells[i].append(Cell(self.__win))
        if self.__win is None:
            return

        for i in range(self.__num_cols):
            for j in range(self.__num_rows):
                self.__draw_cell(i, j)

    def __draw_cell(self, i, j):
        if self.__win is None:
            return
        x1= self.__x1 + i * self.__cells_size_x
        y1= self.__y1 + j * self.__cells_size_y
        x2= x1 + self.__cells_size_x
        y2= y1 + self.__cells_size_y

        self.__cells[i][j].draw(x1, y1, x2, y2)
        self.__animate()

    def __animate(self):
        if self.__win is None:
            return
        self.__win.redraw()
        time.sleep(self.__maze_gen_speed)

    def __break_entrance_and_exit(self):
        last_col = self.__num_cols - 1
        last_row = self.__num_rows - 1
        self.__cells[0][0].has_top_wall = False
        self.__draw_cell(0, 0)
        self.__cells[last_col][last_row].has_bottom_wall = False
        self.__draw_cell(last_col, last_row)

    def __break_walls_r(self, i, j):
        self.__cells[i][j].visited = True
        while True:
            right = [i+1, j]
            left = [i-1, j]
            top = [i, j-1]
            bottom = [i, j+1]
            directions = [right, left, top, bottom]

            if len(self.__possible_directions(directions)) == 0:
                self.__draw_cell(i, j)
                return

            possible_directions = self.__possible_directions(directions)
            rand_sel = random.choice(possible_directions)
            chosen_dir_x, chosen_dir_y = directions[rand_sel][0], directions[rand_sel][1]
            if right == directions[rand_sel]:
                self.__cells[i][j].has_right_wall = False
                self.__cells[chosen_dir_x][chosen_dir_y].has_left_wall = False
            elif left == directions[rand_sel]:
                self.__cells[i][j].has_left_wall = False
                self.__cells[chosen_dir_x][chosen_dir_y].has_right_wall = False

            elif top == directions[rand_sel]:
                self.__cells[i][j].has_top_wall = False
                self.__cells[chosen_dir_x][chosen_dir_y].has_bottom_wall = False

            elif bottom == directions[rand_sel]:
                self.__cells[i][j].has_bottom_wall = False
                self.__cells[chosen_dir_x][chosen_dir_y].has_top_wall = False

            self.__draw_cell(i, j)
            self.__draw_cell(chosen_dir_x, chosen_dir_y)
            self.__break_walls_r(chosen_dir_x, chosen_dir_y)

    def __possible_directions(self, directions):
        possible_directions = []
        for i, d in enumerate(directions):
            out_bounds = (d[0] < 0 or d[0] >= self.__num_cols) or (d[1] < 0 or d[1] >= self.__num_rows) 
            if out_bounds:
                continue
            if not self.__cells[d[0]][d[1]].visited:
                possible_directions.append(i)
        return possible_directions

    def __reset_cells_visited(self):
        for i in range(self.__num_cols):
            for j in range(self.__num_rows):
                self.__cells[i][j].visited = False
        print("Cells reset!")

    def solve(self):
        print("solve maze")
        return self._solve_r(0, 0)
 
    def _solve_r(self, i, j):
        self.__animate()
        self.__cells[i][j].visited = True
        if i == self.__num_cols - 1 and j == self.__num_rows - 1: 
            return True

        right = i+1
        left = i-1
        top = j-1
        bottom = j+1

        open_right_path = i < self.__num_cols - 1 and not self.__cells[i][j].has_right_wall and not self.__cells[right][j].visited
        open_left_path = i > 0 and not self.__cells[i][j].has_left_wall and not self.__cells[left][j].visited
        open_top_path = j > 0 and not self.__cells[i][j].has_top_wall and not self.__cells[i][top].visited
        open_bottom_path = j < self.__num_rows - 1 and not self.__cells[i][j].has_bottom_wall and not self.__cells[i][bottom].visited

        if open_right_path: 
           self.__cells[i][j].draw_move(self.__cells[right][j])
           if self._solve_r(right, j):
                return True
           else:
                self.__cells[i][j].draw_move(self.__cells[right][j], True)
        if open_left_path: 
           self.__cells[i][j].draw_move(self.__cells[left][j])
           if self._solve_r(left, j):
                return True
           else:
               self.__cells[i][j].draw_move(self.__cells[left][j], True)
        if open_top_path:  
           self.__cells[i][j].draw_move(self.__cells[i][top])
           if self._solve_r(i, top):
                return True
           else:
               self.__cells[i][j].draw_move(self.__cells[i][top], True)
        if open_bottom_path:  
           self.__cells[i][j].draw_move(self.__cells[i][bottom])
           if self._solve_r(i, bottom):
                return True
           else:
               self.__cells[i][j].draw_move(self.__cells[i][bottom], True)
        return False

