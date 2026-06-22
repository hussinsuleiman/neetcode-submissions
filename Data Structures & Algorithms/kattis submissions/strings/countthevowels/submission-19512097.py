s = input().lower()
vowels = {'a', 'e', 'i', 'o', 'u'}
cnt = 0

for c in s:
    if c in vowels:
        cnt += 1

print(cnt)