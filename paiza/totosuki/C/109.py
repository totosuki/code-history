import string
alphabet = string.ascii_letters
N = int(input())
S = [input() for _ in range(N)]
S_id = []
for s in S:
  i = 1
  while s[-i] not in alphabet:
    i += 1
  S_id.append(int(s[-i+1:]))
tmp = sorted(S_id)
sorted_S_id = []
for n in tmp:
  sorted_S_id.append(S_id.index(n))
for id in sorted_S_id:
  print(S[id])