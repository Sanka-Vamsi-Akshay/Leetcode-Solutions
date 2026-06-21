class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        l = 0
        rcnt = 0
        rtot = 0
        for idx, i in enumerate(boxes):
            if i == "1":
                rcnt += 1
                rtot += idx
            l += 1
        lcnt = 0
        ltot = 0
        res = []
        for idx, i in enumerate(boxes):
            res.append((rtot - (idx * rcnt)) + (idx * lcnt) - ltot)
            if i == "1":
                rcnt -= 1
                rtot -= idx
                lcnt += 1
                ltot += idx
        return res