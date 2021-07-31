import queue
import random

from solver import Puzzle, PuzzleSolver, Strategy, BreadthFirst, AStar

class Board:
    def __init__(self):
        self.board = [list(range(1, 5)), list(range(5, 9)), list(range(9, 13)), list(range(13, 16)) + ['*']]
        self.goal = []
        for i in self.board:
            self.goal.append(tuple(i))
        self.goal = tuple(self.goal)
        self.empty = [3, 3]

    def __repr__(self):
        string = ''
        for row in self.board:
            for num in row:
                if len(str(num)) == 1:
                    string += '   ' + str(num)
                elif len(str(num)) > 1:
                    string += '  ' + str(num)
            string += '\n'
        return string

    # def convert_to_tuple(self, ar):
    #     result = []
    #     for i in ar:
    #         result.append(tuple(i))
    #     return tuple(result)

    def convert_to_list(self, tup):
        result = []
        for i in tup:
            result.append(list(i))
        return result

    def match(self, copy):
        a = Board()
        a.board = copy
        for row in range(0, 4):
            for col in range(0, 4):
                if a.board[row][col] == '*':
                    a.empty = [row, col]
        result = []
        for i in a.board:
            result.append(list(i))
        a.board = result
        return a

    def move_up(self): # move empty block up
        try:
            if self.empty[0] != 0:
                tmp = self.board[self.empty[0]-1][self.empty[1]]
                self.board[self.empty[0]-1][self.empty[1]] = '*'
                self.board[self.empty[0]][self.empty[1]] = tmp
                self.empty = [self.empty[0]-1, self.empty[1]]
        except IndexError:
            pass

    def move_down(self): # move empty block down
        try:
            tmp = self.board[self.empty[0]+1][self.empty[1]]
            self.board[self.empty[0]+1][self.empty[1]] = '*'
            self.board[self.empty[0]][self.empty[1]] = tmp
            self.empty = [self.empty[0]+1, self.empty[1]]
        except IndexError:
            pass

    def move_right(self): # move empty block right
        try:
            tmp = self.board[self.empty[0]][self.empty[1]+1]
            self.board[self.empty[0]][self.empty[1]+1] = '*'
            self.board[self.empty[0]][self.empty[1]] = tmp
            self.empty = [self.empty[0], self.empty[1]+1]
        except IndexError:
            pass

    def move_left(self): # move empty block left
        try:
            if self.empty[1] != 0:
                tmp = self.board[self.empty[0]][self.empty[1]-1]
                self.board[self.empty[0]][self.empty[1]-1] = '*'
                self.board[self.empty[0]][self.empty[1]] = tmp
                self.empty = [self.empty[0], self.empty[1]-1]
        except IndexError:
            pass

    def shuffle(self, steps):
        for i in range(0, steps):
            direction = random.randrange(1, 5)
            if direction == 1:
                self.move_up()
            elif direction == 2:
                self.move_right()
            elif direction == 3:
                self.move_left()
            elif direction == 4:
                self.move_down()

    def solve(self):
        start = self.convert_to_list(self.board)
        puzzle = Puzzle(start)
        p = PuzzleSolver(AStar(puzzle))
        p.run()
        p.print_performance()
        p.print_solution()
