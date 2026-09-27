class Solution:
    def reverseString(self, s):
        l = 0
        r = len(s) - 1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
    def reverseParentheses(self, s: str) -> str:
        s = list(s)
        stack = []
        tmp = []
        for i in s:
            if i == '(':
                if tmp:
                    stack.append(''.join(tmp))
                    tmp = []
                else:
                    stack.append('')
            elif i == ')':
                self.reverseString(tmp)
                if stack:
                    tmp = list(stack.pop()) + tmp
            else:
                tmp.append(i)
        stack.append(''.join(tmp))
        return ''.join(stack)