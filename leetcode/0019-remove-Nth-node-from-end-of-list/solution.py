class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        RUNTIME: 36 ms (91.7%)
        MEMORY: 14MB (21.66%)
        """
        fast = slow = head
        for _ in range(n):
            fast = fast.next
        if not fast:
            return head.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next

        return head

sol = Solution()
sol.removeNthFromEnd([1,2,3,4,5], 2)
