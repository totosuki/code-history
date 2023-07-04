A, B, C = map(int, input().split())

l = []

if A + B == C:
    l.append("+")

if A - B == C:
    l.append("-")

if len(l) == 1:
    print(l[0])

elif len(l) == 2:
    print("?")

else:
    print("!")