class Solution:
    def minOperations(self, logs: List[str]) -> int:
        count = 0

        for elt in logs:
            if elt == '../':
                count = max(0, count-1)
            
            elif elt != './':
                count += 1
        
        return count