# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def mergeLists(node1, node2):
            headNew = node1

            if node1.val > node2.val:
                headNew = node2
                node2 = node2.next
            else:
                node1 = node1.next

            node = headNew
            
            while node1 and node2:
                if node1.val > node2.val:
                    node.next = node2
                    node = node2
                    node2 = node2.next
                else:
                    node.next = node1
                    node = node1
                    node1 = node1.next
            
            if not node1:
                node.next = node2
            else:
                node.next = node1
            
            return headNew
        
        
        nbLists = len(lists)

        if nbLists == 0:
            return None

        while nbLists > 1:
            for i in range(nbLists // 2):
                lists[i] = mergeLists(lists[i], lists[nbLists-1-i])
            
            r = nbLists % 2
            nbLists //= 2
            
            if r == 1:
                nbLists += 1
        
        return lists[0]