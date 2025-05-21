from figures import Line, Point
from window import Window

win = Window(1000, 800)
new_line = Line(Point(30, 50), Point(100, 50))
win.draw_line(new_line, "black")
new_line2 = Line(Point(30, 50), Point(1000, 70))
win.draw_line(new_line2, "black")
win.wait_for_close()

