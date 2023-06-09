N = int(input())
G = input()
S = [input() for _ in range(N)]
rslt = []
for s in S:
  if G in s:
    rslt.append(s)
if not rslt:
  print("None")
  exit()
[print(r) for r in rslt]