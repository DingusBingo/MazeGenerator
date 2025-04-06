from window import Window
from cell import Point, Line, Cell

win = Window(800, 600)

cell1 = Cell(win, 400, 420, 300, 320)
cell1.has_right_wall = False
cell1.draw(400, 420, 300, 320)
cell2 = Cell(win, 420, 440, 300, 320)
cell2.has_left_wall = False
cell2.has_right_wall = False
cell2.draw(420, 440, 300, 320)
cell3 = Cell(win, 440, 460, 300, 320)
cell3.has_left_wall = False
cell3.has_bottom_wall = False
cell3.draw(440, 460, 300, 320)
cell4 = Cell(win, 440, 460, 320, 340)
cell4.has_top_wall = False
cell4.has_bottom_wall = False
cell4.draw(440, 460, 320, 340)
cell5 = Cell(win, 440, 460, 340, 360)
cell5.has_top_wall = False
cell5.has_right_wall = False
cell5.draw(440, 460, 340, 360)
cell6 = Cell(win, 460, 480, 340, 360)
cell6.has_left_wall = False
cell6.draw(460, 480, 340, 360)

cell1.draw_move(cell2)
cell2.draw_move(cell3)
cell3.draw_move(cell4)
cell4.draw_move(cell5)
cell5.draw_move(cell6)

win.wait_for_close()