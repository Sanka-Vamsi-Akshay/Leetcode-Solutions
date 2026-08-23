class Solution(object):
    def findSmallestSetOfVertices(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        res = set(range(n))
        for i, j in edges:
            if j in res:
                res.remove(j)
        return list(res)