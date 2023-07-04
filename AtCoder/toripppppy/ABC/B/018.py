S = input()
N = int(input())

def r(s: int, e: int):
    s1 = S[:s-1]
    s2 = S[s-1:e][::-1]
    s3 = S[e:]
    return s1 + s2 + s3

for _ in range(N):
    S = r(*map(int,input().split()))

print(S)
S = input()
N = int(input())

def r(s: int, e: int):
    s1 = S[:s-1]
    s2 = S[s-1:e][::-1]
    s3 = S[e:]
    return s1 + s2 + s3

for _ in range(N):
    S = r(*map(int,input().split()))

print(S)
