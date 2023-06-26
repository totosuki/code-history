N = int(input())
S = input()
l = []
r = []
for i in range(N):
  if S[i] == "(":
    l.append(i)
  if S[i] == ")" and l:
    r.append[i]

tmp = min([len(l), len(r)])

prnt(S[:])