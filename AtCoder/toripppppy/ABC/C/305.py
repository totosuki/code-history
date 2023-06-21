H, W = map(int, input().split())

grid = [input() for _ in range(H)]

set_grid = set(grid)

s = [s for s in set_grid if s != "."*W]

l = list(map(lambda x: x.count("#"), s))

answer_line = s[l.index(min(*l))]
mohan_line = s[l.index(max(*l))]

index = 0

for i, a in enumerate(zip(*map(list, [answer_line,mohan_line]))):
  if len(set(a)) != 1:
    index = i
    break

print(grid.index(answer_line)+1, index+1)