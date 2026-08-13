class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        nbs = [0,0]

        for b in bills:
            if b == 5:
                nbs[0] += 1
            
            elif b == 10:
                if nbs[0] == 0:
                    return False
                
                nbs[0] -= 1
                nbs[1] += 1
            
            else:
                if nbs[0] == 0:
                    return False

                elif nbs[1] > 0:
                    nbs[1] -= 1
                    nbs[0] -= 1

                elif nbs[0] < 3:
                    return False

                else:
                    nbs[0] -= 3
        
        return True