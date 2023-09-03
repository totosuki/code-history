N = int(input())
tile = [[False] * 105 for _ in range(105)]

for _ in range(N):
  A, B, C, D = map(int, input().split())
  for row in range(C, D):
    for col in range(A, B):
      tile[row][col] = True
  

cnt = 0

for row in range(105):
  for col in range(105):
    if tile[row][col]:
      cnt += 1

print(cnt)