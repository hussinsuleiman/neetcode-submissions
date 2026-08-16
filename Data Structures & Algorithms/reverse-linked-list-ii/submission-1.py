# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        i = 1
        prev = None
        node = head

        while i < left:
            i += 1
            prev = node
            node = node.next
        
        p = prev

        for t in range(right - left + 1):
            nxt = node.next
            node.next = prev
            prev = node
            node = nxt
        
        if p:
            p.next.next = nxt
            p.next = prev
            return head
        
        head.next = node
        
        return prev