class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        arr = list(range(1, n + 1))
        st = 0
        k -= 1
        while n > 1:
            st = (st + k) % n
            arr.pop(st)
            n -= 1
        return arr[0]