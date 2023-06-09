N = int(input())
Y  = [int(input()) for _ in range(N)]
mame_count = [0 for _ in range(N)]
M = int(input())
addmame_list = [list(map(int, input().split())) for _ in range(M)]
for l in addmame_list:
  for i in range(l[0]-1, l[1]):
    mame_count[i] += l[2]
    if mame_count[i] > Y[i]:
      mame_count[i] = Y[i]

for count in mame_count:
  print(count)