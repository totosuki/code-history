N = input()
M = int(input())
R = [input() for _ in range(M)]
rslt = []
for i in range(len(R)):
  if N not in R[i]:
    rslt.append(R[i])
if not rslt:
  print("none")
else:
  [print(r) for r in rslt]