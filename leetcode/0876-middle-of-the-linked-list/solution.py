class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        RUNTIME: 63 ms (24.23%)
        MEMORY: 13.9 MB (56.16%)
        """
        p1 = p2 = head

        while p2 != None and p2.next != None:
            p1 = p1.next
            p2 = p2.next.next

        return p1

sol = Solution()
sol.middleNode([1,2,3,4,5])
