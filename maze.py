from cell import Cell
import time, random

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
            seed=None
        ):
        if seed:
            random.seed(seed)

        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win
        self.__cells = []

        self.__create_cells()
        self.__break_entrance_and_exit()
        self.__break_walls_r(0, 0)
        self.__reset_cells_visited(self.__num_cols, self.__num_rows)


    def __create_cells(self):
        for i in range(self.__num_cols):
            temp_list = []
            for j in range(self.__num_rows):
                temp_list.append(Cell(self.__win))
                
            self.__cells.append(temp_list)
                
        for i in range(self.__num_cols):
            for j in range(self.__num_rows):
                self.__draw_cell(i, j)

    def __draw_cell(self, i, j):
        if self.__win is None:
            return

        x_left = self.__x1 + i * self.__cell_size_x
        y_top = self.__y1 + j * self.__cell_size_y

        x_right = x_left + self.__cell_size_x
        y_bottom = y_top + self.__cell_size_y

        self.__cells[i][j].draw(x_left, y_top, x_right, y_bottom)

        self.__animate()

    def __animate(self):
        if self.__win is None:
            return
        self.__win.redraw()
        time.sleep(0.05)

    def __break_entrance_and_exit(self):
        self.__cells[0][0].has_top_wall = False
        self.__draw_cell(0, 0)
        self.__cells[self.__num_cols-1][self.__num_rows-1].has_bottom_wall = False
        self.__draw_cell(self.__num_cols-1, self.__num_rows-1)

    
    def __break_walls_r(self, i, j):
        self.__cells[i][j].visited = True

        while True:
            temp_list = []

            if i > 0:
                if self.__cells[i - 1][j].visited  == False:
                    temp_list.append([i - 1,j])

            if j > 0:
                if self.__cells[i][j - 1].visited  == False:
                    temp_list.append([i,j - 1])

            if i < (self.__num_cols - 1):
                 if self.__cells[i + 1][j].visited  == False:
                    temp_list.append([i + 1,j])

            if j < (self.__num_rows - 1):
                if self.__cells[i][j + 1].visited  == False:
                    temp_list.append([i,j + 1])

            if not temp_list:
                self.__draw_cell(i, j)
                return
            
            else:
                random_value = random.choice(temp_list)
            
            chosen_i = random_value[0]
            chosen_j = random_value[1]

            if i < chosen_i:
                self.__cells[i][j].has_right_wall = False
                self.__cells[chosen_i][chosen_j].has_left_wall = False

            if j < chosen_j:
                self.__cells[i][j].has_bottom_wall = False
                self.__cells[chosen_i][chosen_j].has_top_wall = False

            if i > chosen_i:
                self.__cells[i][j].has_left_wall = False
                self.__cells[chosen_i][chosen_j].has_right_wall = False

            if j > chosen_j:
                self.__cells[i][j].has_top_wall = False
                self.__cells[chosen_i][chosen_j].has_bottom_wall = False

            self.__break_walls_r(chosen_i, chosen_j)

    def __reset_cells_visited(self, col, row):
        for i in range(col):
            for j in range(row):
                self.__cells[i][j].visited = False

    def solve(self):

        if self._solve_r(0, 0):
            return True
        return False

    def _solve_r(self, i, j):
        self.__animate()

        self.__cells[i][j].visited = True

        if self.__num_cols - 1 == i and self.__num_rows - 1 == j:
            return True
        
        if j > 0:
            if self.__cells[i][j].has_top_wall == False:
                if self.__cells[i][j - 1].visited == False:
                    self.__cells[i][j].draw_move(self.__cells[i][j - 1])
                    new_cell = self._solve_r(i, j - 1)
                    if new_cell:
                        return True
                    self.__cells[i][j - 1].draw_move(self.__cells[i][j], undo=True)

        if j < (self.__num_rows - 1):
            if self.__cells[i][j].has_bottom_wall == False:
                if self.__cells[i][j + 1].visited == False:
                    self.__cells[i][j].draw_move(self.__cells[i][j + 1])
                    new_cell = self._solve_r(i, j + 1)
                    if new_cell:
                        return True
                    self.__cells[i][j + 1].draw_move(self.__cells[i][j], undo=True)

        if i < (self.__num_cols - 1):
            if self.__cells[i][j].has_right_wall == False:
                if self.__cells[i + 1][j].visited == False:
                    self.__cells[i][j].draw_move(self.__cells[i + 1][j])
                    new_cell = self._solve_r(i + 1, j)
                    if new_cell:
                        return True
                    self.__cells[i + 1][j].draw_move(self.__cells[i][j], undo=True)


        if i > 0:
            if self.__cells[i][j].has_left_wall == False:
                if self.__cells[i - 1][j].visited == False:
                    self.__cells[i][j].draw_move(self.__cells[i - 1][j])
                    new_cell = self._solve_r(i - 1, j)
                    if new_cell:
                        return True
                    self.__cells[i - 1][j].draw_move(self.__cells[i][j], undo=True)
        

        return False





                

                