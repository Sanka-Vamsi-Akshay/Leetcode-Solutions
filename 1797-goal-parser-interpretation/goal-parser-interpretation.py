class Solution:
    def interpret(self, command: str) -> str:
        s = []
        tmp = False
        for i in command:
            if i == "G":
                s.append(i)
            elif i == "(":
                tmp = True
            elif i == ")":
                if tmp:
                    tmp = False
                    s.append('o')
            elif i == 'a':
                tmp = False
                s.append('al')
        return ''.join(s)