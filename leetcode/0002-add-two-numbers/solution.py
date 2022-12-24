# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        RUNTIME: 79 ms (76.99%)
        MEMORY: 13.9MB (86.47%)
        """
        result = hold = ListNode()
        prev = 0
        while l1 != None or l2 != None:
            if l1 != None and l2 != None:
                prev = l1.val + l2.val + prev
            elif l1 != None and l2 == None:
                prev = l1.val + prev
            elif l1 == None and l2 != None:
                prev = l2.val + prev
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            hold.next = ListNode(prev%10)
            hold = hold.next
            prev //=  10
        if prev != 0:
            hold.next = ListNode(prev)
            hold = hold.next
        return result.next
