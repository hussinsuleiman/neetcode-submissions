# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        
        if not list2:
            return list1
        
        head = list1
        node1 = head.next
        node2 = list2
        
        if list2.val < list1.val:
            head = list2
            node2 = head.next
            node1 = list1

        curNode = head
        
        while node1 and node2:
            if node1.val < node2.val:
                curNode.next = node1
                node1 = node1.next
            else:
                curNode.next = node2
                node2 = node2.next
            
            curNode = curNode.next
        
        if node1:
            curNode.next = node1
        else:
            curNode.next = node2
        
        return head