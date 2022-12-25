"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """
        RUNTIME: 36 ms (92.80%)
        MEMORY: 14.8 MB (98.97%)
        """
        if head is None: return None
        # add a copy of node after the node (A->A'->B->B')
        cur = head
        while cur is not None:
            new = Node(cur.val)
            new.next = cur.next
            new.random = cur.random
            cur.next = new
            cur = cur.next.next

        # move random pointers of copied to its corresponding copied
        cur = head
        cur = cur.next
        while True:
            random_pointer = cur.random
            if random_pointer is not None:
                cur.random = random_pointer.next
            if cur.next is None:
                break
            cur = cur.next.next

        # get copied linked list only (A'->B')
        copy = head.next
        cur = copy
        while True:
            if cur.next is None:
                break
            cur.next = cur.next.next
            cur = cur.next
        return copy
