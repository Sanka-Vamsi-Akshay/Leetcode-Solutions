class Solution(object):
    def findSmallestSetOfVertices(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        indegree = [0] * n
        for _, i in edges:
            indegree[i] = 1
        return [i for i, j in enumerate(indegree) if j == 0]