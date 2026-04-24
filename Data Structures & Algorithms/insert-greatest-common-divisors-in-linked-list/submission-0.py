# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def gcd(self, a, b):
        while b != 0:
            temp = a%b
            a = b
            b = temp
        
        return a

    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head

        while node.next:
            a,b = node.val, node.next.val
            g = self.gcd(a,b)
            new = ListNode(g)
            new.next = node.next
            node.next = new
            node = node.next.next

        return head