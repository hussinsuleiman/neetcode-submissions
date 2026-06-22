import sys

MOD = 10**9 + 7

def solve():
    input()
    tokens = sys.stdin.readline().split()

    stack = []
    depth = 0
    stack.append((0, 0))

    for t in tokens:
        if t == '(':
            depth += 1

            if depth % 2 == 0:
                stack.append((0, 0))      
            else:
                stack.append((1, 1))     

        elif t == ')':
            val, _ = stack.pop()
            depth -= 1

            cur_val, op = stack.pop()

            if op == 0:
                cur_val = (cur_val + val) % MOD
            else:
                cur_val = (cur_val * val) % MOD

            stack.append((cur_val, op))

        else:
            x = int(t)
            cur_val, op = stack.pop()

            if op == 0:
                cur_val = (cur_val + x) % MOD
            else:
                cur_val = (cur_val * x) % MOD

            stack.append((cur_val, op))

    print(stack[0][0] % MOD)


solve()