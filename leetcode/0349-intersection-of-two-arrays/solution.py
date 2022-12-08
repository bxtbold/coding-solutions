class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        RUNTIME: 95 ms (52.23%)
        MEMORY: 14 MB (92.6%)
        """
        hashset1 = {}
        hashset2 = {}
        for i in nums1:
            hashset1[i] = 1
        for j in nums2:
            hashset2[j] = 1
        unique = []
        for k in hashset1.keys():
            if k in hashset2.keys():
                unique.append(k)
        return unique
