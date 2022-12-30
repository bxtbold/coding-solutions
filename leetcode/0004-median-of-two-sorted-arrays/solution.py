class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        RUNTIME: 102 ms (78.88%)
        MEMORY: 14.2 MB (66.38%)
        """
        nums1[:] = nums1 + nums2
        nums1.sort()
        if len(nums1) % 2 == 0:
            median_index = len(nums1) // 2 - 1
            median = (nums1[median_index] + nums1[median_index+1]) / 2
        else:
            median_index = len(nums1) // 2
            median = nums1[median_index]
        return median
