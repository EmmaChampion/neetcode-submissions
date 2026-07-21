# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = l1
        curr2 = l2
        while curr1.next and curr2.next:
            curr1.val = curr1.val + curr2.val
            if curr1.val >= 10:
                carry = curr1.val // 10
                curr1.val %= 10
                curr1.next.val += carry
            curr1 = curr1.next
            curr2 = curr2.next

        curr1.val = curr1.val + curr2.val
        if curr1.val < 10:
            if not curr2.next:
                return l1
            else:
                curr1.next = curr2.next
                return l1

        if curr1.next is None and curr2.next is not None:
            curr1.next = curr2.next
        while curr1.next:
            if curr1.val >= 10:
                carry = curr1.val // 10
                curr1.next.val += carry
                curr1.val %= 10
            else:
                return l1
            curr1 = curr1.next
        
        if curr1.val < 10:
            return l1
        else:
            curr1.next = ListNode(curr1.val // 10)
            curr1.val %= 10
            return l1





