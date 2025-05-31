
class Point():
    def __init__(self, x, y) -> None:
        self.x = x 
        self.y = y 

class Line():
    def __init__(self, p1, p2) -> None:
        self.p1 = p1
        self.p2 = p2

    def draw(self, canvas, fill_color):
        canvas.create_line(self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2)

class Cell():
    def __init__(self, window=None) -> None:
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = -1
        self.__x2 = -1
        self.__y1 = -1
        self.__y2 = -1
        self.__win = window
        self.visited = False

    def draw(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2  
        self.__y2 = y2
        if self.__win is None:
            return
        wall_color = "black"
        wall_broken_color = "#d9d9d9"
        left_wall_color = wall_color if self.has_left_wall else wall_broken_color
        left_wall = Line(Point(self.__x1, self.__y1), Point(self.__x1, self.__y2))
        right_wall_color = wall_color if self.has_right_wall else wall_broken_color
        right_wall = Line(Point(self.__x2, self.__y1), Point(self.__x2, self.__y2))
        top_wall_color = wall_color if self.has_top_wall else wall_broken_color
        bottom_wall_color = wall_color if self.has_bottom_wall else wall_broken_color

        top_wall = Line(Point(self.__x1, self.__y1), Point(self.__x2, self.__y1))
        bottom_wall = Line(Point(self.__x1, self.__y2), Point(self.__x2, self.__y2))

        self.__win.draw_line(left_wall, left_wall_color)
        self.__win.draw_line(right_wall, right_wall_color)
        self.__win.draw_line(top_wall, top_wall_color)
        self.__win.draw_line(bottom_wall, bottom_wall_color)

    def draw_move(self, to_cell, undo=False):
        color = "gray" if undo else "red"

        self_half_length = abs(self.__x2 - self.__x1) // 2
        self_x_center = self.__x1 + self_half_length
        self_y_center = self.__y1 + self_half_length

        to_cell_half_length = abs(to_cell.__x2 - to_cell.__x1) // 2
        to_cell_x_center = to_cell.__x1 + to_cell_half_length
        to_cell_y_center = to_cell.__y1 + to_cell_half_length

        if self.__win is None:
            return

        self.__win.draw_line(
            Line(
                Point(self_x_center, self_y_center), 
                Point(to_cell_x_center, to_cell_y_center)
            ),
            color
        )

