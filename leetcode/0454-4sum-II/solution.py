class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        """
        RUNTIME: 878 ms (76.24%)
        MEMORY: 14.2 MB (71.89%)
        """
        sum1, sum2 = {}, {}
        total = 0
        for i in range(len(nums1)):
            for j in range(len(nums1)):
                tmp1 = nums1[i] + nums2[j]
                tmp2 = nums3[i] + nums4[j]
                if tmp1 not in sum1:
                    sum1[tmp1] = 1
                else:
                    sum1[tmp1] += 1
                if tmp2 not in sum2:
                    sum2[tmp2] = 1
                else:
                    sum2[tmp2] += 1

        if (len(sum1) > len(sum2)):
            sum1, sum2 = sum2, sum1

        for i in sum1:
            if -i in sum2:
                total += sum1[i] * sum2[-i]
        return total
