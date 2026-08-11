class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        s = 0

        for op in operations:
            if op == '+':
                record.append(record[-1] + record[-2])
                s += record[-1]

            elif op == 'D':
                record.append(record[-1] * 2)
                s += record[-1]

            elif op == 'C':
                s -= record[-1]
                record.pop()
            
            else:
                record.append(int(op))
                s += record[-1]
        
        return s