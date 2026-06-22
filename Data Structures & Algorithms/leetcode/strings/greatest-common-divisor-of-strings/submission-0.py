class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        l1, l2 = len(str1), len(str2)
        x,y = min(l1, l2), max(l1, l2)

        while x != 0:
            temp = y % x
            y = x
            x = temp
        
        div = [1]

        for i in range(2, y+1):
            if y%i == 0:
                div.append(i)
        
        l = len(div)

        for i in range(l-1, -1, -1):
            w = str1[:div[i]]
            valid = True

            for j in range(1, l1//div[i]):
                if str1[j*div[i]:(j+1)*div[i]] != w:
                    valid = False
                    break
            
            for j in range(l2//div[i]):
                if str2[j*div[i]:(j+1)*div[i]] != w:
                    valid = False
                    break
            
            if valid:
                return w
        
        return ''