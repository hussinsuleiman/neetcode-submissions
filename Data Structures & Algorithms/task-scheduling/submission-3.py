class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        occ = defaultdict(int)
        nbTasks = len(tasks)
        idle = []
        times = []
        output = 0

        for task in tasks:
            occ[task] += 1
        
        while nbTasks > 0:
            for i in range(len(times)):
                times[i] -= 1
            
            keyMax = None

            for key in occ.keys():
                if key not in idle:
                    keyMax = key
                    break

            if keyMax:
                for key in occ.keys():
                    if key not in idle and occ[key] > occ[keyMax]:
                        keyMax = key
                
                if occ[keyMax] > 0:
                    occ[keyMax] -= 1
                    nbTasks -= 1
                    idle.append(keyMax)
                    times.append(n)
                
            if times != [] and times[0] == 0:
                idle.pop(0)
                times.pop(0)
                       
            output += 1
        
        return output

