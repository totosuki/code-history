from fractions import Fraction

N = int(input())

l = []
for i in range(N):
    A, B = map(int,input().split())
    l.append([i+1, Fraction(A)/(Fraction(A+B))])

print(*list(map(lambda a: a[0], sorted(l, key=lambda x: x[1], reverse=True))))