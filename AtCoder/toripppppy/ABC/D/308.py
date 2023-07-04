from collections import deque

R, C = map(int,input().split())
# start
sy, sx = map(int,input().split())
# goal
gy, gx = map(int,input().split())

maze = [input() for _ in range(R)]


q = deque()

for i in maze:
    q.append(i)

q.popleft()
print(q)