N, D = map(int,input().split())
Sl = [input() for _ in range(N)]

c = 0
r = [0]

for i in range(D):
  l = list(map(lambda x: x[i], Sl))
  s = set(l)
  if len(s) == 1 and "o" in s:
    c += 1
  else:
    r.append(c)
    c = 0
else:
  r.append(c)

print(max(r))