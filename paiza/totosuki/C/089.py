H, W = map(int, input().split())
S = [input() for _ in range(H)]
P = [list(map(int, input().split())) for _ in range(H)]
rslt = 0
for i in range(len(S)):
  for j, s in enumerate(S[i]):
    if s == "o":
      rslt += P[i][j]
print(rslt)