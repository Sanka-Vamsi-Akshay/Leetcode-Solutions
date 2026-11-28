class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        f1 = {'1' : 0, '2' : 0, '3' : 0, '4' : 0, '5' : 0, '6' : 0, '7' : 0, '8' : 0, '9' : 0, '0' : 0}
        f2 = {'1' : 0, '2' : 0, '3' : 0, '4' : 0, '5' : 0, '6' : 0, '7' : 0, '8' : 0, '9' : 0, '0' : 0}
        bulls = 0
        for i, j in zip(secret, guess):
            if i == j:
                bulls += 1
            else:
                f1[i] += 1
                f2[j] += 1
        cows = 0
        for i in range(10):
            cows += min(f1[str(i)], f2[str(i)])
        return f"{bulls}A{cows}B"