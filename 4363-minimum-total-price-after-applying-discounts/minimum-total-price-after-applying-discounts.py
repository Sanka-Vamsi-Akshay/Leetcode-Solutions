class Solution:
    def minPrice(self, prices: list[int], discounts: list[int]) -> float:
        prices.sort(reverse = True)
        discounts.sort(reverse = True)
        res = l = 0
        for i, j in zip(prices, discounts):
            res += (i * (100 - j) / 100)
            l += 1
        for i in range(l, len(prices)):
            res += prices[i]
        return res