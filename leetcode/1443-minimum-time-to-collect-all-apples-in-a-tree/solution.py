import collections
class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        """
        RUNTIME: 665 ms (96.18%)
        MEMORY: 50.7 MB (80.25%)
        """
        if sum(hasApple) == 0: return 0
        # dfs
        def dfs(current: int, parent: int) -> bool:
            for child in graph[current]:
                if child == parent:
                    continue
                if dfs(child, current):
                    hasApple[current] = True
            return hasApple[current]
        # graph
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        dfs(0, -1)
        return (sum(hasApple) - 1) * 2
