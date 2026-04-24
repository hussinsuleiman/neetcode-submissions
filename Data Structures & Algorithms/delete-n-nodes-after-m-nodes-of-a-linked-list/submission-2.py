# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteNodes(self, head: Optional[ListNode], m: int, n: int) -> Optional[ListNode]:
        node = head

        while node:
            for i in range(m-1):
                if node:
                    node = node.next
            
            for i in range(n):
                if node and node.next:
                    node.next = node.next.next
            
            if node:
                node = node.next
        
        return head