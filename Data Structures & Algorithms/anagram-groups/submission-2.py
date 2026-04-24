class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def anagrams(a, b):
            count = [0]*26

            for letter in a:
                count[ord(letter)-ord('a')] += 1
            for letter in b:
                count[ord(letter)-ord('a')] -= 1
            
            for i in range(26):
                if count[i] != 0:
                    return False
            return True
        
        output = []
        inGroup = [False] * len(strs)

        for i in range(len(strs)):
            if not inGroup[i]:
                newList = [strs[i]]
                inGroup[i] = True

                for j in range(i+1, len(strs)):
                    if anagrams(strs[i], strs[j]):
                        newList.append(strs[j])
                        inGroup[j] = True
                
                output.append(newList)
        
        return output