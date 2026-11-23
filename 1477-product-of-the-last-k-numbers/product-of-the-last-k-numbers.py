class ProductOfNumbers:

    def __init__(self):
        self.n = 0
        self.nums = []
        self.lastZero = None
        self.prod = 0

    def add(self, num: int) -> None:
        if self.prod == 0:
            self.prod = num
        else:
            self.prod *= num
        self.nums.append(self.prod)
        if num == 0:
            self.lastZero = 1
        elif self.lastZero:
            self.lastZero += 1
        self.n += 1
    def getProduct(self, k: int) -> int:
        if self.lastZero and self.lastZero <= k:
            return 0
        elif self.n == k or self.nums[-k - 1] == 0:
            return self.prod
        return self.prod // self.nums[-k - 1]

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)