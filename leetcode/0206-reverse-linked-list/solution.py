# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        RUNTIME: 39 ms (88.78%)
        MEMORY: 15.4 MB (94.38%)
        """
        reversed_list = None
        while head:
            tmp = head.next
            head.next = reversed_list
            reversed_list = head
            head = tmp
        return reversed_list
