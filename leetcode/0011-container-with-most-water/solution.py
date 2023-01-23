class FirstSolution:
    def maxArea(self, height: List[int]) -> int:
        """
        RUNTIME: 2260 ms (8.11%)
        MEMORY: 27.6MB (11.6%)
        """
        left, right = 0, len(height) - 1
        max_area = 0
        while left < right:
            max_area = max(max_area, (right - left) * min(height[left], height[right]))
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return max_area
