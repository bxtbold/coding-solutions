"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """
        RUNTIME: 35 ms (93.75%)
        MEMORY: 14.9 MB (27.36%)
        """
        curr = head
        while curr is not None:
            if curr.child is not None:
                self.get_child(curr, curr.child, curr.next)
                curr.child = None
            curr = curr.next
        return head

    def get_child(self, before, child, after):
        # bind prev to child
        before.next = child
        # bind child to prev
        child.prev = before
        # bind child's last_node to after
        last_node = child
        while child is not None:
            if child.child is not None:
                self.get_child(child, child.child, child.next)
                child.child = None
            last_node = child
            child = child.next
        last_node.next = after
        # bind after to child's last_node
        if after is not None:
            after.prev = last_node
