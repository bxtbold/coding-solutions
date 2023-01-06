class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        """
        RUNTIME: 855 ms (88.48%)
        MEMORY: 28 MB (61.26%)
        """
        if sum(costs) < coins: return len(costs)
        costs.sort()
        answer = 0
        for i in costs:
            if coins < i:
                break
            coins -= i
            answer += 1
        return answer
