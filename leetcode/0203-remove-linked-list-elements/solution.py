# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        """
        RUNTIME: 66 ms (96.74%)
        MEMORY: 17.8 MB (83.99%)
        """
        while head and head.val == val:
            tmp = head.next
            head = tmp
        if not head: return
        current = head
        while current.next:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next
        return head
