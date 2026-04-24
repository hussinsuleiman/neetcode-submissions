class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        cur, i, j, l, out = 0, 0, 0, len(words), []

        while j < l:
            while j < l and cur + len(words[j]) <= maxWidth:
                cur += len(words[j]) + 1
                j += 1
        
            word = []

            if j == i+1:
                word.append(words[i])
                word.append(' ' * (maxWidth-len(words[i])))
            
            elif j == l:
                for k in range(i, l-1):
                    word.append(words[k])
                    word.append(' ')
                
                word.append(words[l-1])
                word.append(' ' * (maxWidth-cur+1))
            
            else:
                q, r = (maxWidth-cur+j-i) // (j-i-1), (maxWidth-cur+j-i) % (j-i-1)

                for k in range(r):
                    word.append(words[i+k])
                    word.append(' ' * (q+1))
                
                word.append(words[i+r])

                for k in range(r+1, j-i):
                    word.append(' ' * q)
                    word.append(words[i+k])
            
            out.append(''.join(word))
            i = j
            cur = 0
        
        return out