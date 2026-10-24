class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        m1, d1 = map(int, arriveAlice.split('-'))
        m2, d2 = map(int, leaveAlice.split('-'))
        m3, d3 = map(int, arriveBob.split('-'))
        m4, d4 = map(int, leaveBob.split('-'))
        if m2 < m3 or (m2 == m3 and d2 < d3) or m4 < m1 or (m4 == m1 and d4 < d1):
            return 0
        if m1 < m3:
            m1, d1 = m3, d3
        elif m1 == m3 and d1 < d3:
            d1 = d3
        if m2 > m4:
            m2, d2 = m4, d4
        elif m2 == m4 and d2 > d4:
            d2 = d4
        if m1 == m2:
            return d2 - d1 + 1
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        res = days[m1 - 1] - d1 + 1 + d2
        for i in range(m1, m2 - 1):
            res += days[i]
        return res