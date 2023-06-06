N, S, T = map(int, input().split())

w = 0
count = 0

for _ in range(N):
    w += int(input())
    if S <= w <= T: count += 1

print(count)