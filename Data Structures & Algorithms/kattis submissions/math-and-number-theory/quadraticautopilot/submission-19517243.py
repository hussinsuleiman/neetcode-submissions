t1,e1 = map(int, input().split())
t2,e2 = map(int, input().split())
t3,e3 = map(int, input().split())

A = [[1, t1, t1**2], [0, t2-t1, t2**2-t1**2], [0, 0, (t3-t1)*(t3-t2)]]
e = [e1, e2-e1, e3-e1 - (e2-e1)*(t3-t1)//(t2-t1)]

a = e[2] // A[2][2]
b = (e[1] - a*A[1][2]) // A[1][1]
c = (e[0] - a*A[0][2] - b*A[0][1]) // A[0][0]

print(str(a) + ' ' + str(b) + ' ' + str(c))