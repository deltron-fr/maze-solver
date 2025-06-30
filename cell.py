from graphics import Line, Point

class Cell:
    def __init__(self, window=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True

        self.__x1 = -1
        self.__x2 = -1
        self.__y1 = -1
        self.__y2 = -1

        self.visited = False
        self.__win = window

    def draw(self, x1, y1, x2, y2):
        if self.__win is None:
            return
        
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2

        if self.has_left_wall:
            l = Line(Point(self.__x1, self.__y1), Point(self.__x1, self.__y2))
            self.__win.draw_line(l, "black")

        else:
            l = Line(Point(self.__x1, self.__y1), Point(self.__x1, self.__y2))
            self.__win.draw_line(l, "white")
        
        if self.has_right_wall:
            l = Line(Point(self.__x2, self.__y1), Point(self.__x2, self.__y2))
            self.__win.draw_line(l, "black")

        else:
            l = Line(Point(self.__x2, self.__y1), Point(self.__x2, self.__y2))
            self.__win.draw_line(l, "white")

        if self.has_top_wall:
            l = Line(Point(self.__x1, self.__y1), Point(self.__x2, self.__y1))
            self.__win.draw_line(l, "black")

        else:
            l = Line(Point(self.__x1, self.__y1), Point(self.__x2, self.__y1))
            self.__win.draw_line(l, "white")

        if self.has_bottom_wall:
            l = Line(Point(self.__x1, self.__y2), Point(self.__x2, self.__y2))
            self.__win.draw_line(l,"black")

        else:
            l = Line(Point(self.__x1, self.__y2), Point(self.__x2, self.__y2))
            self.__win.draw_line(l,"white")

    def draw_move(self, to_cell, undo=False):
        if self.__win is None:
            return
        
        if not undo:
            l = Line(
                Point((self.__x1 + self.__x2) // 2, (self.__y1 + self.__y2) // 2
                ), Point((to_cell.__x1 + to_cell.__x2) // 2, (to_cell.__y1 + to_cell.__y2) // 2)
            )
            self.__win.draw_line(l, "red")

        else:
            l = Line(
                Point((self.__x1 + self.__x2) // 2, (self.__y1 + self.__y2) // 2
                ), Point((to_cell.__x1 + to_cell.__x2) // 2, (to_cell.__y1 + to_cell.__y2) //2)
            )
            self.__win.draw_line(l, "gray")
