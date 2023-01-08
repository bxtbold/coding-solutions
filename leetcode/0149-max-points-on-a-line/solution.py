class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        """
        RUNTIME: 66 ms (97.37%)
        MEMORY: 13.9 MB (75.79%)
        """
        ans = 0
        for i in range(len(points)):
            hashmap = {}
            for j in range(i):
                slope = self.getSlope(points[i], points[j])
                hashmap[slope] = 1 + hashmap.get(slope,0)
            if hashmap.values():
                ans = max(ans, max(hashmap.values()))
        return ans + 1

    def getSlope(self, p1, p2):
        if p1[0] - p2[0] == 0:
            return 'inf'
        return (p1[1] - p2[1]) / (p1[0] - p2[0])
