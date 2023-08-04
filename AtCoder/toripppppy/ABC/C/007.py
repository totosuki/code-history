from collections import deque

R, C = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())

y, x = 1, 1

cnt = 1

c = []
for _ in range(R):
    c.append(input())

d = deque()

print(c)

def put_next():
    s = list()

    if x > 0:
        s.append([y,x-1])
    if y > 0:
        s.append([y-1,x])

    s.append([y,x+1])
    s.append([y+1,x])

    [d.append([p, cnt]) for p in s if c[p[0]][p[1]] == "."]
    

for _ in range(10):
    put_next()
    print(d)
    while True:
        p = d.popleft()
        if p[1] == cnt:
            y, x = p[0]
            break

    cnt += 1