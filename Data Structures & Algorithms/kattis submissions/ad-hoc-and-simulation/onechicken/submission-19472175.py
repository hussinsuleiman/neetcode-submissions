N,M = map(int, input().split())

if N > M:
    if N-M == 1:
        print("Dr. Chaz needs 1 more piece of chicken!")
    else:
        print("Dr. Chaz needs " + str(N-M) + " more pieces of chicken!")
    
else:
    if M-N == 1:
        print("Dr. Chaz will have 1 piece of chicken left over!")
    else:
        print("Dr. Chaz will have " + str(M-N) + " pieces of chicken left over!")