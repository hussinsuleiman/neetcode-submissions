# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node0, node1, node2 = None, head, head

        for i in range(n):
            node2 = node2.next

        if not node2:
            node1 = head.next
            head.next = None
            return node1
        
        while node2:
            node1 = node1.next
            node2 = node2.next

            if not node0:
                node0 = head
            else:
                node0 = node0.next
        
        node0.next = node1.next
        node1.next = None

        return head