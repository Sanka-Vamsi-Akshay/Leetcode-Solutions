class Solution:
    def check(self, row, col):
        for i in range(row):
            if self.board[i][col] == 'Q':
                return False
        r, c = row - 1, col - 1
        while r >= 0 and c >= 0:
            if self.board[r][c] == 'Q':
                return False
            r -= 1
            c -= 1
        r, c = row - 1, col + 1
        while r >= 0 and c < self.n:
            if self.board[r][c] == 'Q':
                return False
            r -= 1
            c += 1
        return True
    def solve(self, row):
        if row == self.n:
            self.res.append([''.join(r) for r in self.board])
            return
        for col in range(self.n):
            if self.check(row, col):
                self.board[row][col] = 'Q'
                self.solve(row + 1)
                self.board[row][col] = '.'
    def solveNQueens(self, n: int) -> list[list[str]]:
        self.board = [['.'] * n for _ in range(n)]
        self.res = []
        self.n = n
        self.solve(0)
        return self.res
        