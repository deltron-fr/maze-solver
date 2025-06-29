from cell import Cell
import time

class Maze:
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win=None,
        ):
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win
        self.__cells = []
        self.__create_cells()

    def __create_cells(self):
        if self.__win is None:
            return

        for i in range(self.__num_cols):
            temp_list = []
            for j in range(self.__num_rows):
                c = Cell(self.__win)
                self.__draw_cell(i, j)
                temp_list.append(c)

            self.__cells.append(temp_list)

    def __draw_cell(self, i, j):
        if self.__win is None:
            return

        x_left = self.__x1 + i * self.__cell_size_x
        y_top = self.__y1 + j * self.__cell_size_y

        x_right = x_left + self.__cell_size_x
        y_bottom = y_top + self.__cell_size_y

        c = Cell(self.__win)
        c.draw(x_left, y_top, x_right, y_bottom)

        self.__animate()

    def __animate(self):
        if self.__win is None:
            return
        self.__win.redraw()
        time.sleep(0.05)


