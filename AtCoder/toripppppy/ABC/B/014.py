n, X = map(int, input().split())
al = list(map(int, input().split()))
r = int()

for a, x in zip(al,reversed(bin(X)[2:].zfill(n))):
    if x == "1":
        r += a

print(r)