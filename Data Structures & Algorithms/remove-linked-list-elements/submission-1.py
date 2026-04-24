# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        while head and head.val == val:
            head = head.next
        
        if not head:
            return None

        newHead = head
        node = newHead
        after = node.next

        while after:
            while after and after.val == val:
                after = after.next
            
            node.next = after
            node = after

            if node:
                after = node.next
        
        return newHead