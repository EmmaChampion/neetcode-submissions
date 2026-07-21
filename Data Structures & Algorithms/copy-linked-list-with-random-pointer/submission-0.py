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
        table = {}
        newList = self.copyList(head, table)
        curr = head
        while curr:
            if not curr.random:
                table[curr].random = None
            else:
                table[curr].random = table[curr.random]
            curr = curr.next
        return newList
    
    def copyList(self, head, table):
        if not head:
            return None
        newHead = Node(head.val, self.copyList(head.next, table), None)
        table[head] = newHead
        return newHead





