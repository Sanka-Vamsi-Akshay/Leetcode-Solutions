class Solution:
    arr = [0, 0]
    def factors(self, num: int) -> bool:
        for i in range(2, int(num ** 0.5) + 1):
            if(num % i == 0):
                if Solution.arr[num - i] == 0 or Solution.arr[num - (num // i)] == 0:
                    return True
        return False
    def divisorGame(self, n: int) -> bool:
        tmp = len(Solution.arr)
        if tmp - 1 < n:
            Solution.arr.extend([0] * (n - tmp + 1))
            for i in range(tmp, n + 1):
                if Solution.arr[i - 1] == 0:
                    Solution.arr[i] = 1
                else:
                    self.factors(i)
        return bool(Solution.arr[n])