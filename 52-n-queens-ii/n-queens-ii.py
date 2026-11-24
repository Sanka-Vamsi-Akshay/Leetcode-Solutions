class Solution:
    def check(self, row: int, column: int) -> bool:
        for i in range(row):
            if self.board[i][column] == 1:
                return False
        r, c = row - 1, column - 1
        while r >= 0 and c >= 0:
            if self.board[r][c] == 1:
                return False
            r -= 1
            c -= 1
        r, c = row - 1, column + 1
        while r >= 0 and c < self.n:
            if self.board[r][c] == 1:
                return False
            r -= 1
            c += 1
        return True
    def find(self, row: int, column: int) -> None:
        if row == self.n:
            self.cnt += 1
            return
        while column < self.n:
            if self.check(row, column):
                self.board[row][column] = 1
                self.find(row + 1, 0)
                self.board[row][column] = 0
            column += 1
    def totalNQueens(self, n: int) -> int:
        self.n = n
        self.cnt = 0
        self.board = [[0] * n for _ in range(n)]
        row = column = 0
        self.find(row, column)
        return self.cnt