import sys
input = sys.stdin.readline

def gcd(a,b):
    while a != b:
        if a < b:
            a,b = b,a
        
        a -= b
    
    return a

n, a, b = map(int, input().split())
nbFizzBuzz = n // (a*b // gcd(a,b))
nbFizz = n // a - nbFizzBuzz
nbBuzz = n // b - nbFizzBuzz

print(str(nbFizz) + " " + str(nbBuzz) + " " + str(nbFizzBuzz))
 
