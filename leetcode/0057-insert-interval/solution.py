class BetterSolution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        RUNTIME: 84 ms (81.92%)
        MEMORY: 17.3 MB (91.18%)
        """
        answer = []
        for i in intervals:
            if i[1] < newInterval[0]:
                answer.append(i)
            elif newInterval[1] < i[0]:
                answer.append(newInterval)
                newInterval = i
            else:
                newInterval[0] = min(newInterval[0], i[0])
                newInterval[1] = max(newInterval[1], i[1])
        answer.append(newInterval)
        return answer


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        RUNTIME: 95 ms (51.61%)
        MEMORY: 17.6 MB (6.88%)
        """
        answer = []
        while len(intervals) > 0 and intervals[0][1] < newInterval[0]:
            answer.append(intervals.pop(0))
        while len(intervals) > 0 and intervals[0][0] <= newInterval[1]:
            tmp = intervals.pop(0)
            newInterval[0] = min(newInterval[0], tmp[0])
            newInterval[1] = max(newInterval[1], tmp[1])
        return answer + [newInterval] + intervals
