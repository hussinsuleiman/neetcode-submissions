# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverseList(curHead, end):
            if not curHead or not curHead.next:
                return curHead

            cur = curHead
            node = curHead.next

            while node != end:
                after = None

                if node.next:
                    after = node.next

                node.next = cur
                cur = node
                node = after
            
            return cur, curHead
        
        nbNodes = 0
        node = head

        while node:
            node = node.next
            nbNodes += 1
        
        if nbNodes < k or k == 1:
            return head

        node = head
        HeadsTails = []

        for i in range(nbNodes//k):
            curHead = node

            for j in range(k):
                node = node.next

            newHead, newTail = reverseList(curHead, node)
            HeadsTails.append((newHead, newTail))
        
        for i in range(nbNodes//k - 1):
            HeadsTails[i][1].next = HeadsTails[i+1][0]
        
        HeadsTails[-1][1].next = node
        return HeadsTails[0][0]