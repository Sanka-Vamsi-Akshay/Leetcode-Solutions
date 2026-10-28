class Solution:
    def maxPrimes(self, n: int, s: int) -> list[int]:
        tot = 0
        ans = []
        def isPrime(n : int) -> bool:
            if n == 2:
                return True
            if n % 2 == 0:
                return False
            tmp = n ** 0.5
            for i in ans:
                if i > tmp:
                    break
                if n % i == 0:
                    return False
            return True
        for i in range(2, n + 1):
            if tot + i > s:
                break
            if isPrime(i):
                ans.append(i)
                tot += i
        return ans