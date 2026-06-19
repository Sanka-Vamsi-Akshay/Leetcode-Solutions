class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        tot = 0
        for i, j in zip(seats, students):
            tot += abs(i - j)
        return tot