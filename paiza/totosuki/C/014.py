N, R = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]
rslt = []
for i,l in enumerate(data):
  if l[0] >= R*2 and l[1] >= R*2 and l[2] >= R*2:
    rslt.append(i + 1)
[print(r) for r in rslt]