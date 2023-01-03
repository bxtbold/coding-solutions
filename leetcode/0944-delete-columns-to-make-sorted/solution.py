class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        """
        RUNTIME: 89 ms (96.84%)
        MEMORY: 14.7 MB (25.26%)
        """
        answer = 0
        for each in zip(*strs):
            if list(each) != sorted(each):
                answer += 1
        return answer
