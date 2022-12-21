# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        RUNTIME: 46 ms (88.93%)
        MEMORY: 17.1 MB (7.51%)
        """
        if not head: return None
        if not head.next or not head.next.next: return head
        result = ListNode()
        res_copy = result
        current = head
        while True:
            res_copy.val = current.val
            res_copy.next = ListNode()
            if not current.next or not current.next.next: break
            current = current.next.next
            res_copy = res_copy.next
        current = head.next
        while True:
            res_copy.next = ListNode(current.val)
            if not current.next or not current.next.next: break
            current = current.next.next
            res_copy = res_copy.next
        return result
