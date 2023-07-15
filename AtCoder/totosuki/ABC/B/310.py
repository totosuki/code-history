N, M = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]
answer = "No"

for i in range(N):
  for j in range(N):
    if i == j: continue
    Pi = data[i][0]
    Pj = data[j][0]
    Fi = data[i][2:]
    Fj = data[j][2:]

    cnt = 0

    if Pi >= Pj:
      cnt += 1

    se = set(Fi) & set(Fj)
    if len(se) == len(Fi):
      cnt += 1
    
    if (Pi > Pj) or (len(Fi) < len(Fj)):
      cnt += 1

    if cnt == 3:
      answer = "Yes"

print(answer)