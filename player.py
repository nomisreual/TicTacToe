class Player:
    def __init__(self, name = "", id = 1):
        self.__name = name
        if id in (1, -1):
            self.__id   = id
        else:
            raise ValueError

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, id):
        if id in (1, -1):
            self.__id = id
        else:
            raise ValueError

    def makeMove(self):
        while True:
            try:
                move = input()
                if move[0] in ("A", "B", "C") and move[1] in ("1", "2", "3"):
                    row = {"A": 0, "B": 1, "C": 2}.get(move[0])
                    col = {1: 0, 2: 1, 3: 2}.get(int(move[1]))
                    return row, col, self.id
                else:
                    print("Not a valid move. Try again.")
            except IndexError:
                continue