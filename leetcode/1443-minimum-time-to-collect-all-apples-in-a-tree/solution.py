import collections
class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        """
        RUNTIME: 656 ms (96.79%)
        MEMORY: 50.9 MB (64.10%)
        """
        if sum(hasApple) == 0: return 0
        # dfs
        def dfs(node: int, prev: int) -> bool:
            for neighbor in graph[node]:
                if neighbor != prev and dfs(neighbor, node):
                    hasApple[node] = True
            return hasApple[node]
        # graph
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        dfs(0, -1)
        return (sum(hasApple) - 1) * 2
