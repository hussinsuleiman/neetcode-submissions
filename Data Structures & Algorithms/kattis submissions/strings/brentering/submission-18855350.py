s = input()
i = len(s)-1
vowels = {'a', 'e', 'i', 'o', 'u'}

while s[i] not in vowels:
    i -= 1

print(s[:i+1] + "ntry")
