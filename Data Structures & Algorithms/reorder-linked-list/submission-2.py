# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #Find middle and end
        if not head or not head.next:
            return
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            if fast.next.next:
                fast = fast.next.next
            else:
                fast = fast.next
        curr = slow.next
        slow.next = None

        #Reverse the second half
        prev = None
        
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        #Merge the two halves
        forward = head
        reverse = prev

        while reverse:
            tempF = forward.next
            tempR = reverse.next
            forward.next = reverse
            reverse.next = tempF
            forward = tempF
            reverse = tempR