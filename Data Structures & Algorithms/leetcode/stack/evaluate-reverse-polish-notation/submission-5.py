class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nbs = []

        for t in tokens:
            if t == "+":
                nbs.append(nbs.pop() + nbs.pop())
            elif t == "-":
                nbs.append((-1) * nbs.pop() + nbs.pop())
            elif t == "*":
                nbs.append(nbs.pop() * nbs.pop())
            elif t == "/":
                d = nbs.pop()
                r = nbs[-1] % d
                nbs.append(nbs.pop() // d)
                if nbs[-1] < 0 and r != 0:
                    nbs[-1] += 1
            else: 
                nbs.append(int(t))
        
        return nbs[0]