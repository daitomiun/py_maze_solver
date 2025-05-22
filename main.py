from figures import Cell
from window import Window

win = Window(1000, 800)
new_cell = Cell(win)
new_cell.draw(40, 40, 60, 60)
new_cell_2 = Cell(win)
new_cell_2.draw(60, 40, 80, 60)
new_cell_3 = Cell(win)
new_cell_3.draw(80, 40, 100, 60)
new_cell_3.draw_move(new_cell)
win.wait_for_close()

