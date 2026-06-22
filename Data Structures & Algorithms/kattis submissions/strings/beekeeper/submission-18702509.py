import sys
input = sys.stdin.readline

N = int(input())
vowels = {'a', 'e', 'i', 'o', 'u', 'y'}

while N != 0:
    result = ''
    maxRes = -1
    
    for i in range(N):
        word = input().strip()
        res = 0
        
        for j in range(len(word)-1):
            if word[j] in vowels and word[j+1] == word[j]:
                res += 1
        
        if res > maxRes:
            maxRes = res
            result = word
    
    print(result)
    N = int(input())
    