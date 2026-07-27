class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        children = defaultdict(set)
        parents = defaultdict(list)

        for a,b in prerequisites:
            children[a].add(b)
            parents[b].append(a)
        
        seen = set()
        done = False

        while not done:
            done = True

            for i in range(numCourses):
                if i not in children and i not in seen:
                    done = False
                    seen.add(i)

                    for p in parents[i]:
                        children[p].remove(i)

                        if not children[p]:
                            del children[p]
                    
        return len(seen) == numCourses