N = int(input())

l = list(map(int, input().split()))

for i in range(1, N+1):
  l.remove(i)

a = []

for s in l:
    if len(a) == N: break
    if s not in a:
        a.append(s)

print(*a)
