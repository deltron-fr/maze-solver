
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, point1, point2):
        self.x1 = point1.x
        self.y1 = point1.y 
        self.x2 = point2.x
        self.y2 = point2.y

    def draw(self, canvas, fill_color="black"):
        canvas.create_line(
            self.x1, self.y1, self.x2, self.y2, fill=fill_color, width=2 
        )

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
        
        if self.has_right_wall:
            l = Line(Point(self.__x2, self.__y1), Point(self.__x2, self.__y2))
            self.__win.draw_line(l, "black")

        if self.has_top_wall:
            l = Line(Point(self.__x1, self.__y1), Point(self.__x2, self.__y1))
            self.__win.draw_line(l, "black")

        if self.has_bottom_wall:
            l =Line(Point(self.__x1, self.__y2), Point(self.__x2, self.__y2))
            self.__win.draw_line(l,"black")

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
