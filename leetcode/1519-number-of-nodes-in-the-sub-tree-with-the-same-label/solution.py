import collections
class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        """
        RUNTIME: 2088 ms (94.23%)
        MEMORY: 193 MB (50%)
        """
        # dfs
        def dfs(current: int, parent: int) -> List[int]:
            node_counts = [0] * 26
            node_counts[ord(labels[current]) - 97] = 1
            for child in graph[current]:
                if child == parent:
                    continue
                child_counts = dfs(child, current)
                for i in range(26):
                    node_counts[i] += child_counts[i]
            answer[current] = node_counts[ord(labels[current]) - 97]
            return node_counts
        # graph
        graph = collections.defaultdict(list)
        answer = [0] * n
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)
        dfs(0, -1)
        return answer
