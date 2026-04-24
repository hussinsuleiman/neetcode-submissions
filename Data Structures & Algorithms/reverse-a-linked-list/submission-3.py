# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:    
        node1, node2 = None, head

        while node2:
            node3 = node2.next
            node2.next = node1
            node1 = node2
            node2 = node3
        
        return node1

        