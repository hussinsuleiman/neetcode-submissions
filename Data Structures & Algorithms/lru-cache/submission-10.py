class ListNode:
    def __init__(self, val, key):
        self.val = val
        self.key = key
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.dico = dict()
        self.head = None
        self.tail = None 
        self.left = capacity

    def get(self, key: int) -> int:
        if key in self.dico:
            if self.tail != self.dico[key]:
                if self.dico[key].prev:
                    self.dico[key].prev.next = self.dico[key].next
                    self.dico[key].next.prev = self.dico[key].prev
                else:
                    self.head = self.dico[key].next
                    self.head.prev = None

                self.dico[key].prev = self.tail
                self.tail.next = self.dico[key]
                self.dico[key].next = None
                self.tail = self.dico[key]

        return self.dico[key].val if key in self.dico else -1 

    def put(self, key: int, value: int) -> None:
        if key in self.dico:
            if self.dico[key].next:
                self.dico[key].next.prev = self.dico[key].prev  
    
            if self.dico[key] != self.tail:
                if self.dico[key] != self.head:
                    self.dico[key].prev.next = self.dico[key].next
                else:
                    self.head = self.head.next

                self.dico[key].prev = self.tail
                self.tail.next = self.dico[key]
                self.dico[key].next = None
                self.tail = self.dico[key]

            self.dico[key].val = value   

        else:
            self.dico[key] = ListNode(value, key)

            if not self.head:
                self.head = self.dico[key]
            else: 
                self.tail.next = self.dico[key]
                self.dico[key].prev = self.tail
            
            self.tail = self.dico[key]

            if self.left == 0:
                temp = self.head.key

                if self.head.next:
                    self.head = self.head.next
                    self.head.prev = None
                    
                del self.dico[temp]

            else:
                self.left -= 1