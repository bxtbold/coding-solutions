class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        """
        RUNTIME: 728 ms (93%)
        MEMORY: 19 MB (25.51%)
        """
        if n == 1: return 1
        get_trusted = {}
        for i in trust:
            if i[1] not in get_trusted:
                get_trusted[i[1]] = 0
            get_trusted[i[1]] += 1
        for i in trust:
            if i[0] in get_trusted:
                del get_trusted[i[0]]
        if len(get_trusted) == 0:
            return -1
        elif get_trusted[list(get_trusted)[0]] == n - 1:
            return list(get_trusted)[0]
        return -1
