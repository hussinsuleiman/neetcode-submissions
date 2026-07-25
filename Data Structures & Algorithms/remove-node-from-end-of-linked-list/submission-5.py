# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node1, node2 = head, head

        for i in range(n):
            node2 = node2.next
        
        if not node2:
            return head.next
        
        while node2.next:
            node2 = node2.next
            node1 = node1.next
        
        node1.next = node1.next.next
        return head