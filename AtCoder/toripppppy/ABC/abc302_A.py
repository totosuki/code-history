A, B = map(int, input().split(" "))
c = 0

while A > 0:
    A -= B
    c += 1

print(c)