H, W = map(int, input().split())

grid = [input() for _ in range(H)]

set_grid = set(grid)

s = [s for s in set_grid if s != "."*W]

a = list(map(lambda x: x.count("#"), s))

answer_line = s[a.index(min(*a))]
mohan_line = s[a.index(max(*a))]

index = 0

for i, a in enumerate(zip(*map(list, [answer_line,mohan_line]))):
  if len(set(a)) != 1:
    index = i + 1
    break

print(grid.index(answer_line)+1, index)