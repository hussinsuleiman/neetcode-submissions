class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)

        if n % groupSize != 0:
            return False
        
        if groupSize == 1:
            return True

        hand.sort()
        straights = [([hand[0]], 1)]

        for i in range(1,n):
            found = False

            for straight, size in straights:
                if hand[i] - straight[-1] == 1:
                    straights.remove((straight, size))

                    if size + 1 < groupSize:
                        straight.append(hand[i])
                        size += 1
                        straights.append((straight, size))
                    
                    found = True
                    break
            
            if not found:
                straights.append(([hand[i]], 1))

        return not straights