N, M = map(int, input().split())
data = [list(input().split()) for _ in range(M)]
rslt = []
for i in range(N):
  number = i + 1
  output = []
  for j in range(M):
    if number % int(data[j][0]) == 0:
      output.append(data[j][1])
  if not output:
    output = [number]
  rslt.append(output)
[print(*r) for r in rslt]