import sys

def bwt(s):
    n = len(s)

    if n == 0:
        return ""

    rank = [ord(c) for c in s]
    sa = list(range(n))

    k = 1

    while k < n:
        sa.sort(key=lambda i: (rank[i], rank[(i + k) % n]))

        new_rank = [0] * n

        for j in range(1, n):
            prev = sa[j - 1]
            curr = sa[j]

            prev_key = (rank[prev], rank[(prev + k) % n])
            curr_key = (rank[curr], rank[(curr + k) % n])

            new_rank[curr] = new_rank[prev] + (curr_key != prev_key)

        rank = new_rank

        if rank[sa[-1]] == n - 1:
            break

        k *= 2

    return ''.join(s[(i - 1) % n] for i in sa)


for line in sys.stdin:
    s = line.rstrip('\n')
    print(bwt(s))