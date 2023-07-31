# 残念ながらX
from itertools import groupby

N = int(input())
j = 0

fl = "".join(sorted([input() for _ in range(N)]))

print(sum([len(list(g))-1 for k, g in groupby(fl)]))


# by あかり
N = int(input())
l = set()
cnt = 0
for _ in range(N):
  flower = int(input())
  if flower in l:
    cnt += 1
  else:
    l.add(flower)
print(cnt)