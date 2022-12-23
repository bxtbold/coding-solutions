# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        RUNTIME: 40 ms (88.7%)
        MEMORY: 13.8MB (80.18%)
        """
        handle1, handle2 = list1, list2
        merged = ListNode()
        merged_handle = merged
        while True:
            if handle1 is not None and handle2 is not None:
                merged_handle.next = ListNode()
                merged_handle = merged_handle.next
                if handle1.val < handle2.val:
                    merged_handle.val = handle1.val
                    handle1 = handle1.next
                elif handle2.val < handle1.val:
                    merged_handle.val = handle2.val
                    handle2 = handle2.next
                elif handle1.val == handle2.val:
                    merged_handle.val = handle1.val
                    merged_handle.next = ListNode(handle2.val)
                    merged_handle = merged_handle.next
                    handle1 = handle1.next
                    handle2 = handle2.next
            elif handle1 is None:
                merged_handle.next = handle2
                break
            elif handle2 is None:
                merged_handle.next = handle1
                break
        return merged.next
