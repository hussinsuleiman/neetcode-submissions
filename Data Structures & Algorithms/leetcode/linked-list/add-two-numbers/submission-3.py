# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        headNew = ListNode()
        nodeNew = headNew
        carry = 0
        node1 = l1
        node2 = l2

        while node1 and node2:
            nodeNew.val = (node1.val + node2.val + carry) % 10

            if (node1.val + node2.val + carry) >= 10:
                carry = 1
            else:
                carry = 0
            
            node1 = node1.next
            node2 = node2.next
            
            if node1 or node2:
                temp = ListNode()
                nodeNew.next = temp
                nodeNew = temp
            
        if not node2:
            while node1:
                nodeNew.val = (node1.val + carry) % 10

                if (node1.val + carry) >= 10:
                    carry = 1
                else:
                    carry = 0
                
                node1 = node1.next
                
                if node1:
                    temp = ListNode()
                    nodeNew.next = temp
                    nodeNew = temp
                
        
        elif not node1:
            while node2:
                nodeNew.val = (node2.val + carry) % 10

                if (node2.val + carry) >= 10:
                    carry = 1
                else:
                    carry = 0
                
                node2 = node2.next
                
                if node2:
                    temp = ListNode()
                    nodeNew.next = temp
                    nodeNew = temp
            
        if carry == 1:
            nodeNew.next = ListNode(1, None)
        
        return headNew

