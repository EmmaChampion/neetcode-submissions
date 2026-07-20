# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        back = 0 - n - 1
        while curr:
            curr = curr.next
            back += 1
            if back == 0:
                prev = head
            if back > 0:
                prev = prev.next
        if back < 0:
            return head.next
        else:
            prev.next = prev.next.next
            return head