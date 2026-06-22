import sys
input = sys.stdin.readline

n, m = map(int, input().split())
leftSum = sum(list(map(int, input().split())))
rightSum = sum(list(map(int, input().split())))

if leftSum == rightSum:
    print("either")
elif leftSum < rightSum:
    print("left")
else:
    print("right")