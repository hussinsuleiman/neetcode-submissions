from collections import deque

N = int(input())

for _ in range(N):
    L, n_op, n_w = map(int, input().split())
    ops = []
    res = []
    
    full = (1 << L) - 1

    for i in range(n_op):
        op, c = input().split()
        c = int(c)

        flip = 0
        set1 = 0
        clear = 0

        for j in range(L):
            bit = 1 << (L - 1 - j)

            if op[j] == 'F':
                flip |= bit
            elif op[j] == 'S':
                set1 |= bit
            elif op[j] == 'C':
                clear |= bit

        keep = full ^ clear
        ops.append((flip, set1, keep, c))

    for t in range(n_w):
        st, tar = input().split()

        st = int(st, 2)
        tar = int(tar, 2)

        nodes = {st: 0}
        queue = deque([st])

        while queue:
            node = queue.popleft()

            for flip, set1, keep, c in ops:
                new = node ^ flip
                new |= set1
                new &= keep

                if new not in nodes or nodes[new] > nodes[node] + c:
                    nodes[new] = nodes[node] + c
                    queue.append(new)

        if tar in nodes:
            res.append(str(nodes[tar]))
        else:
            res.append('NP')

    print(' '.join(res))