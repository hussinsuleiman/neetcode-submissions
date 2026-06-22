F = input()
H = input()
i,j = 0,0
Lf, Lh = len(F), len(H)

while i < Lf and j < Lh:
    if F[i] == H[j]:
        i += 1
    j += 1

if i == Lf:
    print("Ja")
else:
    print("Nej")