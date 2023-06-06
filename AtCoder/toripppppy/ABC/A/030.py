A, B, C, D = map(int, input().split())

a = B/A
t = D/C

if a == t:
    print("DRAW")
elif a > t:
    print("TAKAHASHI")
else:
    print("AOKI")