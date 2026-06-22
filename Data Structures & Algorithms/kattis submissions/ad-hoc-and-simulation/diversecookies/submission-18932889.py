N, A, B, C = map(int, input().split())
a, b, c = sorted([A, B, C], reverse=True)
answer = min(a + b + c, 2 * (b + c) + N)
print(answer)