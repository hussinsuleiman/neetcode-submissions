# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(x,y):
            while y != 0:
                x,y = y,x%y
            return x

        node = head
        nxt = node.next

        while nxt:
            g = gcd(node.val, nxt.val)
            new = ListNode(g)
            node.next = new
            new.next = nxt
            node = nxt
            nxt = node.next
        
        return head