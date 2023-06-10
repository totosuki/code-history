N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]
s = data[0][0]
e = data[-1][1]
h_l = []
l_l = []
for d in data:
  h_l.append(d[2])
  l_l.append(d[3])
h = max(h_l)
l = min(l_l)
print(s, e, h, l)
