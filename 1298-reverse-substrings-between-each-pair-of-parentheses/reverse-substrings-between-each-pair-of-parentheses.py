class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = [""]
        for ch in s:
            match ch:
                case "(":
                    stack.append("")
                case ")":
                    tmp = stack.pop()
                    stack[-1] += tmp[::-1]
                case _:
                    stack[-1] += ch
        return stack[0]