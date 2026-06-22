class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        dico = dict()

        for ID, score in items:
            if ID in dico:
                heapq.heappush(dico[ID], -score)
            else:
                dico[ID] = [-score]
                heapq.heapify(dico[ID])
        
        res = []

        for ID in dico:
            s = 0

            for i in range(5):
                s -= heapq.heappop(dico[ID])
            
            res.append([ID, s // 5])
        
        res.sort()
        return res