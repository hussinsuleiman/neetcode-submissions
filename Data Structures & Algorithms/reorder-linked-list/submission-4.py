# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head):
        if not head:
            return None
        
        if not head.next:
            return head
        
        new = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return new

    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        rev = self.reverseList(slow.next)
        node1, node2 = head, rev

        while node1:
            if node1.next and node1.next.next == node1:
                node1.next = None
                break

            temp = node1.next
            node1.next = node2

            if temp == node2:
                break

            temp2 = node2.next
            node2.next = temp
            node1, node2 = temp, temp2