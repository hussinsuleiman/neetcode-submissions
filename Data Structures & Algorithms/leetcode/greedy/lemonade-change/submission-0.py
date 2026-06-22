class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        nbFives, nbTens = 0, 0

        for i in range(len(bills)):
            if bills[i] == 5:
                nbFives += 1
            
            elif bills[i] == 10:
                if nbFives > 0:
                    nbFives -= 1
                    nbTens += 1
                else:
                    return False
            
            else:
                if nbTens > 0:
                    if nbFives > 0:
                        nbFives -= 1
                        nbTens -= 1
                    else:
                        return False
                
                elif nbFives > 2:
                    nbFives -= 3
                
                else:
                    return False
        
        return True
                