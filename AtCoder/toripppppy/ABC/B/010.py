n = int(input())
r = int()
for f in map(int,input().split()):
    if f%6 in [2,4,5,0]:
        if f%6 == 2:
            r += 1
        else:
            r += abs((f%6) - 3)
print(r)