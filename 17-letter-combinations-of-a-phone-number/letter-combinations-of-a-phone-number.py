class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        vals = {'2' : ['a', 'b', 'c'], '3' : ['d', 'e', 'f'], '4' : ['g', 'h', 'i'], '5' : ['j', 'k', 'l'], '6' : ['m', 'n', 'o'], '7' : ['p', 'q', 'r', 's'], '8' : ['t', 'u', 'v'], '9' : ['w', 'x', 'y', 'z']}
        n = len(digits)
        res = []
        def find(s, l):
            if l == n:
                res.append(s)
                return
            for i in vals[digits[l]]:
                find(s + i, l + 1)
        find('', 0)
        return res