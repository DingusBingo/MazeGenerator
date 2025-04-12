from graphics import Window
from maze import Maze


def main():
    num_rows = 12
    num_cols = 16
    margin = 50
    screen_x = 800
    screen_y = 600
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows
    win = Window(screen_x, screen_y)

    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win,)

    win.wait_for_close()


main()

#cell1 = Cell(win, 400, 420, 300, 320)
#cell1.has_right_wall = False
#cell1.draw(400, 420, 300, 320)
#cell2 = Cell(win, 420, 440, 300, 320)
#cell2.has_left_wall = False
#cell2.has_right_wall = False
#cell2.draw(420, 440, 300, 320)
#cell3 = Cell(win, 440, 460, 300, 320)
#cell3.has_left_wall = False
#cell3.has_bottom_wall = False
#cell3.draw(440, 460, 300, 320)
#cell4 = Cell(win, 440, 460, 320, 340)
#cell4.has_top_wall = False
#cell4.has_bottom_wall = False
#cell4.draw(440, 460, 320, 340)
#cell5 = Cell(win, 440, 460, 340, 360)
#cell5.has_top_wall = False
#cell5.has_right_wall = False
#cell5.draw(440, 460, 340, 360)
#cell6 = Cell(win, 460, 480, 340, 360)
#cell6.has_left_wall = False
#cell6.draw(460, 480, 340, 360)

#cell1.draw_move(cell2)
#cell2.draw_move(cell3)
#cell3.draw_move(cell4)
#cell4.draw_move(cell5)
#cell5.draw_move(cell6)