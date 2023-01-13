class Solution:
    def longestPath(self, parent, s):
        """
        RUNTIME: 1742 ms (88.67%)
        MEMORY: 151 MB (62.15%)
        """
        children = [[] for i in range(len(s))]
        for i in range(len(parent)):
            if parent[i] >= 0:
                children[parent[i]].append(i)

        self.longest = 0
        def dfs(node):
            cands = [0, 0]
            for child in children[node]:
                depth = dfs(child)
                if s[child] != s[node]:
                    cands.append(depth)
                    cands.sort()
                    cands = cands[-2:]
            self.longest = max(self.longest, cands[0] + cands[1] + 1)
            return cands[1] + 1
        dfs(0)
        return self.longest
