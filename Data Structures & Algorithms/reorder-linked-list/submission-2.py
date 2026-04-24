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

    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        node1 = head    
        node2 = self.reverseList(slow.next)
        slow.next = None

        while node2:
            temp1 = node1.next
            temp2 = node2.next
            node1.next = node2
            node2.next = temp1
            node1 = temp1
            node2 = temp2
