# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        prevTail = dummy

        kthNode = self.getKthNode(prevTail, k)
        while kthNode:
            nextHead = kthNode.next
            prev = kthNode.next
            curr = prevTail.next

            while curr != nextHead:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            temp = prevTail.next
            prevTail.next = kthNode
            prevTail = temp
            kthNode = self.getKthNode(prevTail, k)
        return dummy.next
        
    def getKthNode(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr