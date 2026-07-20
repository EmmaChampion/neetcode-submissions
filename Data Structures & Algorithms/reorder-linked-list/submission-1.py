# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head and head.next:
            self.reorder(head, head.next)
    
    def reorder(self, root, curr):
        if not curr:
            return root
        root = self.reorder(root, curr.next)
        if not root:
            return None
        if root == curr or root.next == curr:
            curr.next = None
            temp = None
        else:
            temp = root.next
            root.next = curr
            curr.next = temp
        return temp