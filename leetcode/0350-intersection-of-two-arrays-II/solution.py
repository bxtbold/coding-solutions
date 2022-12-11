class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        RUNTIME: 52 ms (90.62%)
        MEMORY: 14 MB (52.91%)
        """
        num_dict1, num_dict2 = {}, {}

        if len(num_dict1) > len(num_dict2):
            num_dict1, num_dict2 = num_dict2, num_dict1

        for i in nums1:
            if i in num_dict1:
                num_dict1[i] += 1
            else:
                num_dict1[i] = 1
        for i in nums2:
            if i in num_dict1:
                if i in num_dict2:
                    num_dict2[i] += 1
                else:
                    num_dict2[i] = 1

        intersected = []
        for each in num_dict2:
            intersected += [each] * min(num_dict1[each], num_dict2[each])
        return intersected
