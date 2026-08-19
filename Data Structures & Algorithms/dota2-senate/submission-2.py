class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        nextId = len(senate)
        radiant = deque()
        dire = deque()

        for i,s in enumerate(senate):
            if s == 'R':
                radiant.append(i)
            else:
                dire.append(i)
        
        while dire and radiant:
            r,d = radiant.popleft(), dire.popleft()

            if d < r:
                dire.append(nextId)
            else:
                radiant.append(nextId)

            nextId += 1    
        
        if radiant:
            return 'Radiant'
        return 'Dire'