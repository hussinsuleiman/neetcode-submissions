class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        l = len(hand)

        if l % groupSize != 0:
            return False
        
        if groupSize == 1:
            return True

        hand.sort()
        valid = [True] * l

        for t in range(1, l // groupSize+1):
            a = 0
            while not valid[a]:
                a += 1
            
            cur = hand[a]
            x = 1
            valid[a] = False
            done = False

            for i in range(a+1, l):
                if not valid[i]:
                    continue

                if cur == hand[i]-1:
                    cur = hand[i]
                    valid[i] = False
                    x += 1

                    if x == groupSize:
                        done = True
                        break
            
            if not done:
                return False
        
        return True