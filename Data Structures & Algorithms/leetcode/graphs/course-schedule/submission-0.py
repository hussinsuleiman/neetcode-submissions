class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq = {c : [] for c in range(numCourses)}

        for crs, pre in prerequisites:
            prereq[crs].append(pre)

        cycle = set()
        visit = set()

        def dfs(crs):
            if crs in cycle:
                return False
            
            cycle.add(crs)
            
            for pre in prereq[crs]:
                if not dfs(pre):
                    return False

            visit.add(crs)
            cycle.remove(crs)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True     