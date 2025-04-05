from window import Window, Point, Line

win = Window(800, 600)

pA1 = Point(400, 0)
pA2 = Point(400, 600)
pB1 = Point(0, 300)
pB2 = Point(800, 300)

l1 = Line(pA1, pA2)
l2 = Line(pB1, pB2)

win.draw_line(l1, 'black')
win.draw_line(l2, 'black')

win.wait_for_close()