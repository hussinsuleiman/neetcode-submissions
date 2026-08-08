# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        new = head
        carry = 0

        while l1 and l2:
            new.val = (carry + l1.val + l2.val) % 10
            carry = (carry + l1.val + l2.val) // 10
            l1 = l1.next
            l2 = l2.next

            if l1 and l2:
                new.next = ListNode()
                new = new.next
            
        while l1:
            new.next = ListNode()
            new = new.next
            new.val = (carry + l1.val) % 10
            carry = (carry + l1.val) // 10
            l1 = l1.next

        while l2: 
            new.next = ListNode()
            new = new.next
            new.val = (carry + l2.val) % 10
            carry = (carry + l2.val) // 10
            l2 = l2.next
                
        if carry == 1:
            new.next = ListNode(1)

        return head