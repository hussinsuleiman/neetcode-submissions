class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = ['']
        files = path.split('/')
        
        for f in files:
            if not f or f == '.':
                continue
            
            if f == '..':
                if len(stack) > 1:
                    stack.pop()
                continue
            
            stack.append(f)

        return '/'.join(stack) if len(stack) > 1 else '/'