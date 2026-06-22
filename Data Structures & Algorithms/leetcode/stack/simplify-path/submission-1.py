class Solution:
    def simplifyPath(self, path: str) -> str:
        inp = path.split("/")
        output = [""]

        for elt in inp:
            if elt == '' or elt == '.':
                continue
            
            if elt == '..':
                if len(output) > 1:
                    output.pop()
            else:
                output.append(elt)
        
        if len(output) <= 1:
            return "/"

        return "/".join(output)