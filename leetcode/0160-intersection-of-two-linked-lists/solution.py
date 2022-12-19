# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        """
        RUNTIME: 443 ms (12.93%)
        MEMORY: 30.5 MB (5.1%)
        """
        copyA, copyB = headA, headB
        passed = {}
        while True:
            if copyA.val not in passed:
                passed[copyA.val] = [copyA]
            elif copyA.val in passed and copyA not in passed[copyA.val]:
                passed[copyA.val].append(copyA)
            if not copyA.next: break
            copyA = copyA.next
        while True:
            if copyB.val in passed and copyB in passed[copyB.val]:
                break
            if not copyB.next: return None
            copyB = copyB.next
        return copyB
