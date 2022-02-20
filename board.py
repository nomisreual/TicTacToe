class Field:
    def __init__(self):
        self.__value = None
    
    @property
    def value(self):
        """
        Field holds either 1 or -1 as value.
        """
        return self.__value
    
    @value.setter
    def value(self, playerID):
        self.__value = playerID


class Board:
    def __init__(self):
        self.__board = [[Field(), Field(), Field()] for _ in range(3)]
    
    @property
    def board(self):
        """
        3 x 3 tic-tac-toe board is represented by an list of lists.
        """
        return self.__board
    
    def set_field(self, row, col, playerID):
        self.board[row][col].value = playerID
    
    def display(self):
        print("\n")
        print("{}  | 1 | 2 | 3 |".format(20 * " "))
        print("{}---------------".format(20 * " "))
        rowLabels = ("A", "B", "C")
        count     = 0
        for row in self.board:
            col = [col.value for col in row]
            col = ["o" if k == 1 else ("x" if k == -1 else " ") for k in col]
            print("{}{} | {} | {} | {} |".format(20 * " ",rowLabels[count] ,*col))
            print("{}---------------".format(20 * " "))
            count += 1
        print("\n")

    def hasWon(self, row, col):
        current_row = self.board[row]
        current_col = []
        for i in range(3):
            current_col.append(self.board[i][col])

        diagonal_one = []
        for i in range(3):
            diagonal_one.append(self.board[i][i].value)
        diagonal_two = []
        for i in range(3):
            diagonal_two.append(self.board[i][2 - i].value)

        current_row = [entry.value for entry in current_row]
        current_col = [entry.value for entry in current_col]

        row_sum = 0
        col_sum = 0
        diag_one_sum = 0
        diag_two_sum = 0

        for entry in current_row:
            if entry is not None:
                row_sum += entry
        for entry in current_col:
            if entry is not None:
                col_sum += entry
        for entry in diagonal_one:
            if entry is not None:
                diag_one_sum += entry
        for entry in diagonal_two:
            if entry is not None:
                diag_two_sum += entry

        row_sum = abs(row_sum)
        col_sum = abs(col_sum)
        diag_one_sum = abs(diag_one_sum)
        diag_two_sum = abs(diag_two_sum)

        if row_sum == 3 or col_sum == 3 or diag_one_sum == 3 or diag_two_sum == 3:
            return True
        else:
            return False
