class Solution:
    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        paths = []
        target = len(graph) - 1
        def check(path):
            node = path[-1]
            if node == target:
                paths.append(path)
                return
            for n in graph[node]:
                check(path + [n])
        check([0])
        return paths