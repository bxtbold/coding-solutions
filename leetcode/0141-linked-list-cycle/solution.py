# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        RUNTIME: 66 ms (80.52%)
        MEMORY: 17.6 MB (68.37%)
        """
        if not head or not head.next or not head.next.next: return False
        slow, fast = head.next, head.next.next
        while slow != fast:
            if not fast.next or not fast.next.next:
                return False
            slow = slow.next
            fast = fast.next.next
        return True
