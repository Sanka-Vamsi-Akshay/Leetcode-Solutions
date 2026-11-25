class Solution:
    def check(self, row, col, num):
        if (num in self.rows[row]) or (num in self.cols[col]) or (num in self.boxes[((row // 3) * 3) + (col // 3)]):
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
                b = ((row // 3) * 3) + (col // 3)
                self.boxes[b].add(str(num))
                if col == 8:
                    if self.find(row + 1, 0):
                        return True
                else:
                    if self.find(row, col + 1):
                        return True
                self.board[row][col] = '.'
                self.rows[row].remove(str(num))
                self.cols[col].remove(str(num))
                self.boxes[b].remove(str(num))

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
                    self.boxes[((i // 3) * 3) + (j // 3)].add(board[i][j])
        self.find(0, 0)
        return self.board
        