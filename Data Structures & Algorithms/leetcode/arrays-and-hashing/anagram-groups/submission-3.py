class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dico = defaultdict(list)

        for word in strs:
            count = [0]*26
            for letter in word:
                count[ord(letter)-ord('a')] += 1
            dico[tuple(count)].append(word)
        
        output = []

        for k in dico.values():
            output.append(k)

        return output

        