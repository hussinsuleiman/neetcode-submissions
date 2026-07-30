# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge(list1, list2):
            new = list1
            node1, node2 = list1.next, list2

            if list2.val < list1.val:
                new = list2
                node1, node2 = list1, list2.next
            
            node = new

            while node1 and node2:
                if node1.val < node2.val:
                    node.next = node1
                    node1 = node1.next
                else:
                    node.next = node2
                    node2 = node2.next
                
                node = node.next
            
            if not node2:
                node.next = node1
            else:
                node.next = node2
            
            return new
        
        n = len(lists)

        if n == 0:
            return None

        if n == 1:
            return lists[0]

        nxt = []

        for i in range(n//2):
            nxt.append(merge(lists[2*i], lists[2*i+1]))

        if n%2 == 1:
            nxt.append(lists[-1])

        return self.mergeKLists(nxt) 