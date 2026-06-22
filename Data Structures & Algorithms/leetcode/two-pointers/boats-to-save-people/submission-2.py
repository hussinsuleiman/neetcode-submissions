class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        n = len(people)
        i,j = 0, n-1
        cur = people[-1]
        t = 1

        while i < j:
            if cur + people[i] <= limit:
                cur += people[i]
                i += 1
            
            if i == j:
                break

            t += 1
            j -= 1
            cur = people[j]
        
        return t

        