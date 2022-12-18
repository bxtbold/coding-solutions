# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        RUNTIME: 52 ms (93.93%)
        MEMORY: 17.9 MB (23.21%)
        """
        if not head or not head.next or not head.next.next: return None
        slow_traversed = {}
        slow_traversed[head] = 0
        slow, fast = head.next, head.next.next
        while slow != fast:
            slow_traversed[slow] = 0
            if not fast.next or not fast.next.next: return None
            if fast in slow_traversed:
                return fast
            elif fast.next in slow_traversed:
                return fast.next
            elif fast.next.next in slow_traversed:
                return fast.next.next
            slow = slow.next
            fast = fast.next.next
        return fast
