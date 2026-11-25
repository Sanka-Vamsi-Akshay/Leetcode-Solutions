class Solution:
    def findBox(self, row: int, col: int) -> int:
        if row < 3:
            if col < 3: return 0
            elif col < 6: return 1
            else: return 2
        elif row < 6:
            if col < 3: return 3
            elif col < 6: return 4
            else: return 5
        else:
            if col < 3: return 6
            elif col < 6: return 7
            else: return 8
    def check(self, row, col, num):
        if (num in self.rows[row]) or (num in self.cols[col]) or (num in self.boxes[self.findBox(row, col)]):
            return False
        return True
    def find(self, row, col):
        if row == 9:
            return True
        if col == 9:
            return
        if self.board[row][col] != '.':
            if col == 8:
                if self.find(row + 1, 0):
                    return True
            if self.find(row, col + 1):
                return True
            return
        for num in range(1, 10):
            if self.check(row, col, str(num)):
                self.board[row][col] = str(num)
                self.rows[row].add(str(num))
                self.cols[col].add(str(num))
                self.boxes[self.findBox(row, col)].add(str(num))
                if col == 8:
                    if self.find(row + 1, 0):
                        return True
                else:
                    if self.find(row, col + 1):
                        return True
                self.board[row][col] = '.'
                self.rows[row].remove(str(num))
                self.cols[col].remove(str(num))
                self.boxes[self.findBox(row, col)].remove(str(num))

    def solveSudoku(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.board = board
        self.rows = [set() for _ in range(9)]
        self.cols = [set() for _ in range(9)]
        self.boxes = [set() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    self.rows[i].add(board[i][j])
                    self.cols[j].add(board[i][j])
                    self.boxes[self.findBox(i, j)].add(board[i][j])
        self.find(0, 0)
        return self.board
        