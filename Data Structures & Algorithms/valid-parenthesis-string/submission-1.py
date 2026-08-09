class Solution:
    def checkValidString(self, s: str) -> bool:
        d = set([0])

        for c in s:
            new = set()

            if c == '(':
                for diff in d:
                    new.add(diff+1)

            elif c == ')':
                for diff in d:
                    if diff > 0:
                        new.add(diff-1)
            
            else:
                for diff in d:
                    new.add(diff)
                    new.add(diff+1)
                    
                    if diff > 0:
                        new.add(diff-1)
            
            d = new
        
        return 0 in d