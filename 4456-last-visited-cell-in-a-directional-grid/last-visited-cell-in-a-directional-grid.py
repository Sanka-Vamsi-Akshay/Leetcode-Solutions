class Solution:
    def lastVisitedCell(self, grid: list[list[str]]) -> list[int]:
        v = set()
        m = len(grid)
        n = len(grid[0])
        r = 0
        c = 0
        while r >= 0 and r < m and c >= 0 and c < n and (r, c) not in v:
            tmp = (r, c)
            v.add(tmp)
            match grid[r][c]:
                case 'R':
                    c += 1
                case 'L':
                    c -= 1
                case 'U':
                    r -= 1
                case 'D':
                    r += 1
        return list(tmp)