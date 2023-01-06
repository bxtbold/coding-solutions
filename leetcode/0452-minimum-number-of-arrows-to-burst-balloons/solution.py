class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        """
        RUNTIME: 1349 ms (84.14%)
        MEMORY: 60 MB (14.41%)
        """
        points.sort(key = lambda x : x[1])
        answer, arrow = 0, float('-inf')
        for point in points:
            if point[0] > arrow:
                answer += 1
                arrow = point[1]
        return answer
