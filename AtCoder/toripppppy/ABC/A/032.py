import math

a, b, n = [int(input()) for _ in range(3)]

l = math.lcm(a, b)

r = 0

while True:
    r += l
    if r >= n:
        print(r)
        break