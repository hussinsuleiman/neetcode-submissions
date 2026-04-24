class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        dico = dict()

        for s in strings:
            isNew = True

            for k in dico.keys():
                valid = (len(s) == len(k))

                if valid:
                    o = (ord(s[0]) - ord(k[0]))%26

                    for i in range(1, len(s)):
                        if (ord(s[i]) - ord(k[i]))%26 != o:
                            valid = False
                            break
                    
                if valid:
                    dico[k].append(s)
                    isNew = False

            if isNew:
                dico[s] = [s]
        
        output = []

        for elt in dico.keys():
            output.append(dico[elt])
        
        return output
            
            