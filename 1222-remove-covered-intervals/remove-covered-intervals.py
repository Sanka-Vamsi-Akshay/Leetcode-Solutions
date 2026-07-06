class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x : (x[0], -x[1]))
        cnt = 1
        s = [intervals[0]]
        l = 1
        for i in range(1, len(intervals)):
            if not((s[-1][0] <= intervals[i][0]) and (s[-1][1] >= intervals[i][1])):
                s.append(intervals[i])
                l += 1
        return l