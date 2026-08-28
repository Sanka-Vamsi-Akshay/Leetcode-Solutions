from collections import deque
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        v = set()
        q = deque([0])
        while q:
            n = q.popleft()
            v.add(n)
            for i in rooms[n]:
                if i not in v:
                    q.append(i)
        return len(v) == len(rooms)