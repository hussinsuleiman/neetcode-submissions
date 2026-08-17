class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        graph = defaultdict(list)
        mailToName = dict()
        seen = set()

        for a in accounts:
            mailToName[a[1]] = a[0]
            
            for i in range(1, len(a)-1):
                graph[a[i]].append(a[i+1])
                graph[a[i+1]].append(a[i])
        
        res = []

        for mail in mailToName:
            if mail in seen:
                continue

            new = [mailToName[mail]]
            stack = [mail]
            seen.add(mail)

            while stack:
                top = stack.pop()
                new.append(top)
                
                for nei in graph[top]:
                    if nei not in seen:
                        seen.add(nei)
                        stack.append(nei)
            
            res.append(new)
        
        return res