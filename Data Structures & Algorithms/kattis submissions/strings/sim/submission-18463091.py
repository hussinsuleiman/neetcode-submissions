import sys
from collections import deque

input = sys.stdin.readline
T = int(input())

for _ in range(T):
    text = input().rstrip('\n')
    currWord = []
    output = deque()
    right = True

    for char in text:
        if char == '<':
            if currWord:
                currWord.pop()
            elif right:
                if output:
                    s = output.pop()
                    s = s[:-1]
                    if s:
                        output.append(s)

        elif char == '[':
            if right:
                if currWord:
                    output.append(''.join(currWord))
            else:
                if currWord:
                    output.appendleft(''.join(currWord))
            currWord = []
            right = False

        elif char == ']':
            if not right:
                if currWord:
                    output.appendleft(''.join(currWord))
                currWord = []
                right = True

        else:
            currWord.append(char)

    if currWord:
        if right:
            output.append(''.join(currWord))
        else:
            output.appendleft(''.join(currWord))

    print(''.join(output))