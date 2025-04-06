

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2
    
    def draw(self, canvas, fill_color):
        canvas.create_line(self.point1.x, self.point1.y, self.point2.x, self.point2.y, fill=fill_color, width=2)

class Cell:
    def __init__(self, window, x1, x2, y1, y2):
        self.window = window
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
    
    def draw(self, x1, x2, y1, y2):
        if self.has_left_wall:
            left_line = Line(Point(x1, y1), Point(x1, y2))
            self.window.draw_line(left_line, 'black')
        if self.has_top_wall:
            top_line = Line(Point(x1, y1), Point(x2, y1))
            self.window.draw_line(top_line, 'black')
        if self.has_right_wall:
            right_line = Line(Point(x2, y1), Point(x2, y2))
            self.window.draw_line(right_line, 'black')
        if self.has_bottom_wall:
            bottom_line = Line(Point(x2, y2), Point(x1, y2))
            self.window.draw_line(bottom_line, 'black')
        
    def draw_move(self, to_cell, undo=False):
        color = 'red'
        if undo == True: color = 'gray'

        path_x1 = (self.x2 - self.x1) // 2 + self.x1
        path_y1 = (self.y2 - self.y1) // 2 + self.y1
        path_x2 = (to_cell.x2 - to_cell.x1) // 2 + to_cell.x1
        path_y2 = (to_cell.y2 - to_cell.y1) // 2 + to_cell.y1

        path = Line(Point(path_x1, path_y1), Point(path_x2, path_y2))
        self.window.draw_line(path, color)