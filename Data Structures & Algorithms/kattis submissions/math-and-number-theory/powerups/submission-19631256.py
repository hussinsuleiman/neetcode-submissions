n,k = map(int, input().split())
facts = [1]

for i in range(1, n+k):
    facts.append(facts[-1] * i)

print(facts[n+k-1] // facts[n-1] // facts[k])