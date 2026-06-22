S = input()
output = []
vowels = {'a', 'e', 'i', 'o', 'u', 'y'}

for letter in S:
    if letter.lower() in vowels:
        output.append(letter)

print(''.join(output))
