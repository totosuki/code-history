N, M = map(int, input().split())
F = [int(input()) for _ in range(M)]
point = 0
for f in F:
  if point >= f:
    point -= f
    print(N, point)
  else:
    N -= f
    point += f // 10
    print(N, point)